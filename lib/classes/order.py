
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        Order.all.append(self)

        coffee.orders(self)
        coffee.customers(customer)

        customer.orders(self)
        customer.coffees(coffee)



