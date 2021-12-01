import logging
from lib.OrderHelpers import OrderHelpers


def test_add_an_order(order):
    order = order.add_setup_and_create_order()
    oh = OrderHelpers()
    oh.verify_order_has_party(order, 1, 'BUYER', {111})
    oh.verify_order_has_party(order, 1, 'SUPPLIER', {222})


def test_create_an_order_with_oha(order):
    order = order.add_setup_and_create_order(True, 123)
    oh = OrderHelpers()
    oh.verify_order_has_party(order, 1, 'BUYER', {111})
    oh.verify_order_has_party(order, 1, 'SUPPLIER', {222})
    oh.verify_order_has_party(order, 1, 'OHA', {123})


def test_that_fails(order):
    # this test fails due to error in one of the library files
    # can you find out why?

    order = order.add_setup_and_create_order(True, 456)
    oh = OrderHelpers()
    oh.verify_order_has_party(order, 1, 'BUYER', {111})
    oh.verify_order_has_party(order, 1, 'SUPPLIER', {222})
    oh.verify_order_has_party(order, 1, 'OHA', {456})
