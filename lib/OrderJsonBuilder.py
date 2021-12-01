class OrderJsonBuilder:

    order_dict = {
        "parties": [
            {
                "type": "BUYER",
                "id": 111
            },
            {
                "type": "SUPPLIER",
                "id": 222
            }
        ]
    }

    def add_party(self, party_dict):
        self.order_dict['parties'].append(party_dict)
        return self
