import random
import json


# def generate_customers(amount):
# def generate_products(amount):
# def generate_orders(amount,nproducts, ncustomers):

ncustomers = 1000
nproducts  = 1000
norders    = 100000


with open("customers.json", "w+") as file:
    customers = []
    for i in range(ncustomers):
        age = random.randrange(18, 60)
        customer = {"customer_id": i, "customer_name": "c-"+str(i), "age": age}
        customers.append(customer)
    json.dump(customers, file)


with open("products.json", "w+") as file:
    products = []
    for i in range(nproducts):
        age = random.randrange(18, 60)
        product = {"product_id": i, "product_name": "p-"+str(i)}
        products.append(product)
    json.dump(products, file)



with open("orders.json", "w+") as file:
    orders = []
    for i in range(norders):
        quantity = random.randrange(1, 100)
        product_id = random.randrange(1, nproducts)
        customer_id = random.randrange(1, ncustomers)
        product = products[product_id]
        customer = customers[customer_id]
        order = {"order_id": i, "quantity": quantity, "product": product, "customer": customer}
        orders.append(order)
    json.dump(orders, file)



# generate_customers(ncustomers)
# generate_products(nproducts)
# generate_orders(norders,50000,10000)