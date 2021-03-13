import random
import json


def generate_customers(amount):
    with open("../json/customers.json", "w") as file:
        customers = []
        for i in range(amount):
            age = random.randrange(18, 60)
            customer = {"customer_id": i, "customer_name": "c-"+str(i), "age": age}
            customers.append(customer)
        json.dump(customers, file)


def generate_products(amount):
    with open("../json/products.json", "w") as file:
        products = []
        for i in range(amount):
            age = random.randrange(18, 60)
            product = {"product_id": i, "product_name": "p-"+str(i)}
            products.append(product)
        json.dump(products, file)



def generate_orders(amount,nproducts, ncustomers):
    with open("../json/orders.json", "w") as file:
        orders = []
        for i in range(amount):
            quantity = random.randrange(1, 100)
            product_id = random.randrange(1, nproducts)
            customer_id = random.randrange(1, ncustomers)
            order = {"order_id": i, "quantity": quantity, "product_id": product_id, "customer_id": customer_id}
            orders.append(order)
        json.dump(orders, file)

ncustomer = 250000
nproducts = 250000
norders   = 1500000

generate_customers(ncustomer)
generate_products(nproducts)
generate_orders(norders,nproducts,ncustomer)