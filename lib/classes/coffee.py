class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and not hasattr(self, 'name'):
            self._name = name
        else: 
            raise Exception('why u no work')
    
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer and isinstance(new_customer, Customer) and new_customer not in self._customers:
            self._customers.append(new_customer)
        return self._customers
        pass
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        price = 0
        for order in self._orders:
            price += order.price
        return price / len(self._orders)