from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import models after defining db
from models import Restaurant, Pizza, RestaurantPizza

# Define your routes here
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    formatted_restaurants = []
    for restaurant in restaurants:
        formatted_restaurants.append({
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        })
    return jsonify(formatted_restaurants)

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    formatted_pizzas = []
    for pizza in restaurant.pizzas:
        formatted_pizzas.append({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        })

    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': formatted_pizzas
    })

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    # Delete associated RestaurantPizzas
    RestaurantPizza.query.filter_by(restaurant_id=id).delete()

    # Delete the restaurant
    db.session.delete(restaurant)
    db.session.commit()

    return '', 204

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    formatted_pizzas = []
    for pizza in pizzas:
        formatted_pizzas.append({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        })
    return jsonify(formatted_pizzas)

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    # Check if the pizza ID and restaurant ID exist in the database
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')
    pizza = Pizza.query.get(pizza_id)
    if not pizza:
        return jsonify({'error': 'Pizza not found'}), 404
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    # Create the restaurant-pizza pair
    try:
        restaurant_pizza = RestaurantPizza(
            price=data.get('price'),
            pizza=pizza,
            restaurant=restaurant
        )
        db.session.add(restaurant_pizza)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'errors': ['validation errors']}), 400

    return jsonify({
        'id': pizza_id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    }), 201


if __name__ == '__main__':
    app.run(port=5555)