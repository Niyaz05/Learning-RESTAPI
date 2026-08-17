from fastapi import FastAPI, HTTPException
app = FastAPI()


products = [
    {
        "id": 1,
        "name": "Rice",
        "description": "Basmati Rice",
        "price": 60,
        "quantity": 100,
        "category": "Grocery"
    },
    {
        "id": 2,
        "name": "Oil",
        "description": "Sunflower Oil",
        "price": 140,
        "quantity": 50,
        "category": "Grocery"
    },
    {
        "id": 3,
        "name" : "Wheat",
        "description": "Ashirvad",
        "price" : 120,
        "quantity": 60,
        "category": "Grocery"
    }
]
@app.get("/")
def home():
    return {"message" : "go to products"}

@app.get("/products") #this method returns all the products listed above
def get_products():
    return products

@app.get("/products/{id}") #this is called a path parameter
def get_product(id: int):
    for product in products:
        if product["id"]==id:
            return product

    # return {"message" : "Product not found"} this is not good practice and its better to use a HTTP exception

    raise HTTPException(status_code = 404, detail="Product not found") #since 400 status level codes are client side errors, this can be used

#if you change the python file name, then change the run command to uvicorn [new file name]:app --reload