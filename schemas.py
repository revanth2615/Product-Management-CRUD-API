from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)

class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True