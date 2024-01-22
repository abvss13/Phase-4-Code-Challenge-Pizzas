from app import db
from sqlalchemy.orm import validates

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')

    @validates('name')
    def validate_name(self, key, value): 
        if len(value.strip()) > 50:
            raise ValueError("Restaurant name must not be more than 50 words.")
        return value

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza', back_populates='pizzas')
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')

    @validates('price')
    def validate_price(self, key, value):
        if value < 1 or value > 30:
            raise ValueError("Price must be between 1 and 30.")
        return value