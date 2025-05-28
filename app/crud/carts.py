from sqlalchemy.orm import Session
from ..models.cart import CartItem
from ..models.product import Product
from ..schemas.cart import CartItemCreate, CartItemUpdate

def get_cart_items(db: Session, user_id: int):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()

def get_cart_item(db: Session, cart_item_id: int, user_id: int):
    return db.query(CartItem).filter(
        CartItem.id == cart_item_id,
        CartItem.user_id == user_id
    ).first()

def get_cart_item_by_product(db: Session, user_id: int, product_id: int):
    return db.query(CartItem).filter(
        CartItem.user_id == user_id,
        CartItem.product_id == product_id
    ).first()

def create_cart_item(db: Session, cart_item: CartItemCreate, user_id: int):
    # Check if item already exists in cart
    db_cart_item = get_cart_item_by_product(db, user_id, cart_item.product_id)
    
    if db_cart_item:
        # Update quantity if item already exists
        db_cart_item.quantity += cart_item.quantity
    else:
        # Create new cart item
        db_cart_item = CartItem(
            user_id=user_id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity
        )
        db.add(db_cart_item)
    
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item

def update_cart_item(db: Session, cart_item_id: int, cart_item: CartItemUpdate, user_id: int):
    db_cart_item = get_cart_item(db, cart_item_id, user_id)
    if not db_cart_item:
        return None
    
    db_cart_item.quantity = cart_item.quantity
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item

def delete_cart_item(db: Session, cart_item_id: int, user_id: int):
    db_cart_item = get_cart_item(db, cart_item_id, user_id)
    if not db_cart_item:
        return None
    
    db.delete(db_cart_item)
    db.commit()
    return db_cart_item

def clear_cart(db: Session, user_id: int):
    db_cart_items = get_cart_items(db, user_id)
    for item in db_cart_items:
        db.delete(item)
    db.commit()
    return True

def calculate_cart_total(db: Session, user_id: int):
    cart_items = get_cart_items(db, user_id)
    total = 0.0
    
    for item in cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if product:
            price = product.price - product.discount_amount
            total += price * item.quantity
    
    return total