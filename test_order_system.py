import pytest
from order_system import ShoppingCart

@pytest.fixture
def cart():
    return ShoppingCart()

def test_add_single_product(cart):
    product = {"id": 1, "name": "Laptop", "price": 1000}
    cart.add_product(product, quantity=1)
    assert len(cart.items) == 1
    assert cart.items[0]["product"]["name"] == "Laptop"
    assert cart.items[0]["quantity"] == 1

def test_add_multiple_products(cart):
    product1 = {"id": 1, "name": "Laptop", "price": 1000}
    product2 = {"id": 2, "name": "Mouse", "price": 50}
    cart.add_product(product1, quantity=1)
    cart.add_product(product2, quantity=2)
    assert len(cart.items) == 2
    assert cart.calculate_total() == 1100

def test_calculate_total_no_taxes_no_discount(cart):
    cart.add_product({"id": 1, "name": "Laptop", "price": 1000}, quantity=1)
    cart.add_product({"id": 2, "name": "Mouse", "price": 50}, quantity=2)
    assert cart.calculate_total() == 1100

def test_calculate_total_with_taxes(cart):
    cart.add_product({"id": 1, "name": "Laptop", "price": 1000}, quantity=1)
    assert cart.calculate_total(tax=0.18) == 1180

def test_calculate_total_with_discount(cart):
    cart.add_product({"id": 1, "name": "Laptop", "price": 1000}, quantity=1)
    assert cart.calculate_total(discount=0.10) == 900
