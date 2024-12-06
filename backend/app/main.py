from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import auth, merchants, products, reviews, location

app = FastAPI(title="Business Platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(merchants.router, prefix="/api/merchants", tags=["merchants"])
app.include_router(products.router, prefix="/api/products", tags=["products"])
app.include_router(reviews.router, prefix="/api/reviews", tags=["reviews"])
app.include_router(location.router, prefix="/api/location", tags=["location"])

@app.get("/")
async def root():
    return {"message": "Business Platform API"}