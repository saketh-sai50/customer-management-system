from models.customer import Customer

# In-memory storage (used instead of real DB)
customers = {}

class CustomerService:

    def create_customer(self, customer_id, name, email):
        if customer_id in customers:
            raise ValueError("Customer already exists")

        customer = Customer(customer_id, name, email)
        customers[customer_id] = customer
        return customer

    def get_customer(self, customer_id):
        return customers.get(customer_id)

    def get_all_customers(self):
        return [cust.to_dict() for cust in customers.values()]

    def update_customer(self, customer_id, name, email):
        if customer_id not in customers:
            raise ValueError("Customer not found")

        customer = customers[customer_id]
        customer.name = name
        customer.email = email
        return customer

    def delete_customer(self, customer_id):
        if customer_id not in customers:
            raise ValueError("Customer not found")

        del customers[customer_id]
