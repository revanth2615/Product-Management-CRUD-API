from sqlalchemy.orm import Session
import models
import schemas

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def get_products(db: Session):
    return db.query(models.Product).all()


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()


def update_product(
    db: Session,
    product_id: int,
    product: schemas.ProductCreate
):
    db_product = get_product(db, product_id)

    if not db_product:
        return None

    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity

    db.commit()
    db.refresh(db_product)

    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)

    if not db_product:
        return None

    db.delete(db_product)
    db.commit()

    return db_product