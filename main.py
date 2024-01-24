from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    password: str

class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: str
    order_status: str

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

# Заглушки для баз данных
users = []
orders = []
products = []

# Маршруты для пользователей
@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"message": "User not found"}

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for user in users:
        if user.id == user_id:
            user.first_name = updated_user.first_name
            user.last_name = updated_user.last_name
            user.email = updated_user.email
            user.password = updated_user.password
            return {"message": "User updated successfully"}
    return {"message": "User not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "User deleted successfully"}
    return {"message": "User not found"}

# Маршруты для заказов
@app.get("/orders")
def get_orders():
    return orders

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order.id == order_id:
            return order
    return {"message": "Order not found"}

@app.post("/orders")
def create_order(order: Order):
    orders.append(order)
    return order

@app.put("/orders/{order_id}")
def update_order(order_id: int, updated_order: Order):
    for order in orders:
        if order.id == order_id:
            order.user_id = updated_order.user_id
            order.product_id = updated_order.product_id
            order.order_date = updated_order.order_date
            order.order_status = updated_order.order_status
            return {"message": "Order updated successfully"}
    return {"message": "Order not found"}

@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    for order in orders:
        if order.id == order_id:
            orders.remove(order)
            return {"message": "Order deleted successfully"}
    return {"message": "Order not found"}

# Маршруты для товаров
@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"message": "Product not found"}

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return product

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for product in products:
        if product.id == product_id:
            product.name = updated_product.name
            product.description = updated_product.description
            product.price = updated_product.price
            return {"message": "Product updated successfully"}
    return {"message": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product.id == product_id:
            products.remove(product)
            return {"message": "Product deleted successfully"}
    return {"message": "Product not found"}
