# content of tests/conftest.py
import pytest
from lib.OrderService import OrderService


@pytest.fixture
def order():

    order = OrderService()
    yield order

