from shopping_cart import shoppingcart
import pytest
from item_database import *
from unittest.mock import Mock

@pytest.fixture
def cart():
    return shoppingcart(5) #All setup for the cart here

@pytest.mark.regression
def test_can_add_item_to_cart(cart):
    # cart=shoppingcart(5)
    cart.add("apple")
    assert cart.size()==1

@pytest.mark.regression
def test_when_item_added_then_cart_contains_item(cart):
    # cart=shoppingcart(5)
    cart.add("banana")
    assert "banana" in cart.get_items()
    
def test_when_add_more_than_max_items_should_fail(cart):
    # cart=shoppingcart(5)
    with pytest.raises(OverflowError):
        for _ in range(6):
            cart.add("apple")
def test_can__get_total_price(cart):
    # cart=shoppingcart(5)
    cart.add("banana")
    cart.add("apple")

    price_map={ "banana":1,"apple":2,}
#or
    # item_database = ItemDatabase()
    # def mock_get_item(item: str):
    #     if item == "apple":
    #         return 1.0
    #     if item == "orange":
    #         return 2.0
    # item_database.get = Mock(side_effect=mock_get_item)

    assert cart.get_total_price(price_map)

