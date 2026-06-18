from fastapi import FastAPI
import models
from database import engine
from products import router as product_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Management API"
)

app.include_router(product_router)


@app.get("/")
def home():
    return {
        "message": "Product Management API Running"
    }