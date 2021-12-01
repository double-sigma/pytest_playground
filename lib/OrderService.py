import logging
from random import randint
from lib.OrderJsonBuilder import OrderJsonBuilder


class OrderService:

    def create_order(self, order_body):
        order_id = randint(100, 999)
        logging.info(f"CREATED ORDER {order_id}")

        order_body['id'] = order_id

        return order_body

    def add_setup(self):
        logging.info("ADDED SETUP")

    def add_setup_and_create_order(self, with_oha=False, oha_id=None):
        self.add_setup()

        oj = OrderJsonBuilder()

        if with_oha:
            oj.add_party(
                {
                    "type": "OHA",
                    "id": oha_id
                }
            )

        order_dict = oj.order_dict

        order = self.create_order(order_dict)
        return order
