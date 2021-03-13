import random
import json


# def generate_customers(amount):
# def generate_products(amount):
# def generate_orders(amount,nproducts, ncustomers):

# ncustomers = 100000
# nproducts  = 100000
# norders    = 1000000


# with open("customers.json", "w+") as file:
#     customers = []
#     for i in range(ncustomers):
#         age = random.randrange(18, 60)
#         customer = {"customer_id": i, "customer_name": "c-"+str(i), "age": age}
#         customers.append(customer)
#     json.dump(customers, file)


# with open("products.json", "w+") as file:
#     products = []
#     for i in range(nproducts):
#         age = random.randrange(18, 60)
#         product = {"product_id": i, "product_name": "p-"+str(i)}
#         products.append(product)
#     json.dump(products, file)



with open("../json/orders.json", "r") as file:
    orders = json.loads(file.read())

with open("../json/products.json", "r") as file:
    products = json.loads(file.read())

with open("../json/customers.json", "r") as file:
    customers = json.loads(file.read())

with open("../json/ordersCouch.json", "w") as file:
    ordersCouch = []
    for order in orders:
        quantity = order["quantity"]
        product = products[order["product_id"]]
        customer = customers[order["customer_id"]]
        order_id = order["order_id"]
        order = {"order_id": order_id, "quantity": quantity, "product": product, "customer": customer}
        ordersCouch.append(order)
    json.dump(ordersCouch, file)



# generate_customers(ncustomers)
# generate_products(nproducts)
# generate_orders(norders,50000,10000)