from sqlalchemy.orm import Session
from ..models.order import Order, OrderItem, OrderStatus
from ..models.product import Product
from ..schemas.order import OrderCreate
from ..crud.carts import get_cart_items, clear_cart, calculate_cart_total

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def get_orders_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Order).filter(Order.user_id == user_id).offset(skip).limit(limit).all()

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).offset(skip).limit(limit).all()

def create_order(db: Session, order: OrderCreate, user_id: int):
    # Get total from items or calculate from cart
    total_amount = calculate_cart_total(db, user_id)
    
    # Create order
    db_order = Order(
        user_id=user_id,
        total_amount=total_amount,
        status=OrderStatus.PENDING,
        shipping_address=order.shipping_address,
        shipping_city=order.shipping_city,
        shipping_state=order.shipping_state,
        shipping_country=order.shipping_country,
        shipping_postal_code=order.shipping_postal_code,
        payment_method=order.payment_method,
        payment_status="pending"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    # Create order items from cart
    cart_items = get_cart_items(db, user_id)
    for cart_item in cart_items:
        product = db.query(Product).filter(Product.id == cart_item.product_id).first()
        if product:
            unit_price = product.price - product.discount_amount
            total_price = unit_price * cart_item.quantity
            
            db_order_item = OrderItem(
                order_id=db_order.id,
                product_id=cart_item.product_id,
                quantity=cart_item.quantity,
                unit_price=unit_price,
                total_price=total_price
            )
            db.add(db_order_item)
            
            # Update product stock
            product.stock_quantity -= cart_item.quantity
            
    db.commit()
    
    # Clear the cart after order is created
    clear_cart(db, user_id)
    
    return db_order

def update_order_status(db: Session, order_id: int, status: OrderStatus):
    db_order = get_order(db, order_id)
    if not db_order:
        return None
    
    db_order.status = status
    db.commit()
    db.refresh(db_order)
    return db_order

def update_payment_status(db: Session, order_id: int, payment_status: str):
    db_order = get_order(db, order_id)
    if not db_order:
        return None
    
    db_order.payment_status = payment_status
    db.commit()
    db.refresh(db_order)
    return db_order