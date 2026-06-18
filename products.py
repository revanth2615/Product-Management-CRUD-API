from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.ProductResponse)
def add_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(db, product)


@router.get("/", response_model=list[schemas.ProductResponse])
def get_all_products(
    db: Session = Depends(get_db)
):
    return crud.get_products(db)


@router.get("/{id}", response_model=schemas.ProductResponse)
def get_product_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    product = crud.get_product(db, id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.put("/{id}", response_model=schemas.ProductResponse)
def update_product(
    id: int,
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    updated_product = crud.update_product(
        db,
        id,
        product
    )

    if not updated_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return updated_product


@router.delete("/{id}")
def delete_product(
    id: int,
    db: Session = Depends(get_db)
):
    deleted_product = crud.delete_product(
        db,
        id
    )

    if not deleted_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Product deleted successfully"
    }