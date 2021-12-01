import logging


class OrderHelpers:

    def verify_order_has_party(self, order_json, expected_count, party_type, party_ids={}):

        parties_list = []
        amount_of_parties = 0

        for i in order_json['parties']:
            if str(i['type']):
                amount_of_parties += 1

        for i in range(0, amount_of_parties):
            if order_json['parties'][i]['type'] == party_type:
                parties_list.append(order_json['parties'][i])

        assert len(parties_list) == expected_count, f"Expected {expected_count} OHAs, but got {str(len(parties_list))}"

        if party_ids != {}:
            for party in parties_list:
                logging.info(f"Party IDs: {party_ids}")
                logging.info(f"Parties list: {parties_list}")
                logging.info(f"Party: {party}")
                logging.info(f"Party ID: {party['id']}")
                assert party['id'] in party_ids, \
                    f"Party: {party_type} with ID: {str(party['id'])} is not in expected party IDs list: {party_ids}"
