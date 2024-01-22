from app import db, app
from models import Restaurant, Pizza, RestaurantPizza
from faker import Faker
import random

from random import randint

with app.app_context():
    db.create_all()

    restaurant1 = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
    restaurant2 = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")

    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    restaurant_pizza1 = RestaurantPizza(price=5, pizza=pizza1, restaurant=restaurant1)
    restaurant_pizza2 = RestaurantPizza(price=7, pizza=pizza2, restaurant=restaurant1)

    db.session.add_all([restaurant1, restaurant2, pizza1, pizza2, restaurant_pizza1, restaurant_pizza2])
    db.session.commit()