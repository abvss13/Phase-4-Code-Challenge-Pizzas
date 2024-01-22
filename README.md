# Flask Code Challenge - Pizza Restaurants

Welcome to the Flask Code Challenge! In this assessment, you'll be working with a Pizza Restaurant domain to build out a Flask API that allows users to interact with restaurant and pizza data.

## Requirements

Your task is to build a Flask API with the following features:

1. Create the necessary relationships:

   - A Restaurant has many Pizzas through RestaurantPizza
   - A Pizza has many Restaurants through RestaurantPizza
   - A RestaurantPizza belongs to a Restaurant and belongs to a Pizza
   
2. Add validations to the RestaurantPizza and Restaurant Models:

   - Ensure that RestaurantPizza `price` attribute has a value between 1 and 30
   - Ensure that Restaurant `name` attribute contains fewer than 50 characters
   - Ensure that Restaurant `name` attribute is unique

3. Set up the following routes with appropriate JSON data formats:

   - GET `/restaurants`: Returns a list of all restaurants in the following format:
   
       ```
       [
         {
           "id": 1,
           "name": "Dominion Pizza",
           "address": "Good Italian, Ngong Road, 5th Avenue"
         },
         {
           "id": 2,
           "name": "Pizza Hut",
           "address": "Westgate Mall, Mwanzi Road, Nrb 100"
         }
       ]
       ```

   - GET `/restaurants/:id`: Returns information about a single restaurant, including all pizzas offered by the restaurant, in the following format:

       ```
       {
         "id": 1,
         "name": "Dominion Pizza",
         "address": "Good Italian, Ngong Road, 5th Avenue",
         "pizzas": [
           {
             "id": 1,
             "name": "Cheese",
             "ingredients": "Dough, Tomato Sauce, Cheese"
           },
           {
             "id": 2,
             "name": "Pepperoni",
             "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
           }
         ]
       }
       ```

   - DELETE `/restaurants/:id`: Deletes a restaurant and all its associated pizzas from the database
   
   - GET `/pizzas`: Returns a list of all pizzas in the following format:
       
       ```
       [
         {
           "id": 1,
           "name": "Cheese",
           "ingredients": "Dough, Tomato Sauce, Cheese"
         },
         {
           "id": 2,
           "name": "Pepperoni",
           "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
         }
       ]
       ```
       
   - POST `/restaurant_pizzas`: Adds a new restaurant-pizza pair to the database. The route should accept an object with the following properties in the body of the request:
   
       ```
       {
         "price": 5,
         "pizza_id": 1,
         "restaurant_id": 3
       }
       ```
       
Upon successful creation, the response should display the information related to the pizza. If the creation is unsuccessful, the route should return JSON data with errors and corresponding HTTP status code.

## Usage

To use this API, first ensure that you have Flask and the necessary dependencies installed on your machine. Then, clone this repository and start the Flask application by running the following commands:

```
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```

The app should be running at `http://127.0.0.1:5000`. You can test the routes using a tool like Postman or cURL. See the rubric above for exact test cases.

## Author

This project was done by Abdullahi Abass.

## License

This project was licensed by MIT License.