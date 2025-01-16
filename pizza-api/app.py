from flask import Flask, jsonify, request

app = Flask(__name__)

# JSON data
pizzas = [
     {
    "id": 1,
    "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/97981/2-lou-malnatis-deep-dish-pizzas.bf0fe065d251a9cca3925b269d443a27.jpg?ixlib=react-9.0.2&auto=format&ar=1%3A1",
    "name": "Lou Malnati's Pizza",
    "dsc": "2 Lou Malnati's Deep Dish Pizzas",
    "price": 67.99,
    "rate": 4,
    "country": "Chicago, IL"
  },
  {
    "id": 2,
    "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/89781/choose-your-own-thin-crust-pizza-4-pack.b928a2008eab50c65dc87e59b5952190.jpg?ixlib=react-9.0.2&auto=format&ar=1%3A1",
    "name": "Bartolini’s",
    "dsc": "Choose Your Own Thin Crust Pizza - 4 Pack",
    "price": 139,
    "rate": 4,
    "country": "Chicago, IL"
  },
  {
    "id": 3,
    "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/131840/choose-your-own-new-haven-style-pizza-6-pack.ab82828afc6172cdd4017556c15e36dd.jpg?ixlib=react-9.0.2&auto=format&ar=1%3A1",
    "name": "Zuppardi's Apizza",
    "dsc": "New Haven-Style Pizza - 6 Pack (Choose Your Own)",
    "price": 79,
    "rate": 4,
    "country": "West Haven, CT"
  },
  {
    "id": 4,
    "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/106829/6-lou-malnatis-deep-dish-pizzas.f59993181da5d295668c8a6fb856055e.jpg?ixlib=react-9.0.2&auto=format&ar=1%3A1",
    "name": "Lou Malnati's Pizza",
    "dsc": "6 Lou Malnati's Deep Dish Pizzas",
    "price": 116.99,
    "rate": 4,
    "country": "Chicago, IL"
  },
  {
    "id": 5,
    "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/106027/wood-fired-pizzas-best-seller-4-pack.1653bb05922ba153ac178f8365d27f6d.jpg?ixlib=react-9.0.2&auto=format&ar=1%3A1",
    "name": "Pizzeria Bianco",
    "dsc": "Wood Fired Pizzas Best Seller - 4 Pack",
    "price": 129,
    "rate": 5,
    "country": "Phoenix, AZ"
  },
  {
    "id": 6,
    "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/133398/choose-your-own-deep-dish-pizza-3-pack.4111791511244a4946bb5c9ad2c17da9.jpg?ixlib=react-9.0.2&auto=format&ar=1%3A1",
    "name": "Bartolini’s",
    "dsc": "Choose Your Own Deep Dish Pizza - 3 Pack",
    "price": 139,
    "rate": 5,
    "country": "Chicago, IL"
  },
  {
    "id": 7,
    "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/132973/detroit-style-pizza-choose-your-own-3-pack.6b6f4909ffd4066d5471e70eac5c3d89.jpeg?ixlib=react-9.0.2&auto=format&ar=1%3A1",
    "name": "Emmy Squared",
    "dsc": "Detroit-Style Pizza - Choose Your Own 3 Pack",
    "price": 89,
    "rate": 4,
    "country": "Brooklyn, NY"
  },
  {
    "id": 8,
    "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/104938/brooklyn-pizza-choose-your-own-5-pack.edc4f476a75207d0af840ce6f225f2b3.jpg?ixlib=react-9.0.2&auto=format&ar=1%3A1",
    "name": "Paesan’s Pizza",
    "dsc": "Brooklyn Pizza - Choose Your Own 5 Pack",
    "price": 69,
    "rate": 4,
    "country": "Albany, NY"
  },
  {
    "id": 9,
    "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/89948/chicago-deep-dish-pizza-4-pack.49927daafa8c147fe9bb2a113e56668e.jpg?ixlib=react-9.0.2&auto=format&ar=1%3A1",
    "name": "My Pi Pizza",
    "dsc": "Chicago Deep Dish Pizza - 4 Pack",
    "price": 129,
    "rate": 5,
    "country": "Chicago, IL"
  },
  {
    "id": 10,
    "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/106828/4-lou-malnatis-deep-dish-pizzas.8c79eb7506b5752ab3387d8174246b17.jpg?ixlib=react-9.0.2&auto=format&ar=1%3A1",
    "name": "Lou Malnati's Pizza",
    "dsc": "4 Lou Malnati's Deep Dish Pizzas",
    "price": 96.99,
    "rate": 4,
    "country": "Chicago, IL"
  },
  {
    "id": 11,
    "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/131555/choose-your-own-pizza-3-pack.fcf7a43e38593007ef2857fe16d6dd26.png?ixlib=react-9.0.2&auto=format&ar=1%3A1",
    "name": "Tony's Pizza Napoletana",
    "dsc": "Choose Your Own Pizza - 3 Pack",
    "price": 99,
    "rate": 5,
    "country": "San Francisco, CA"
  },
  {
    "id": 12,
    "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/115101/plain-thin-crust-pizza-4-pack.5540e9d166db2f0853643c6517e4a225.jpg?ixlib=react-9.0.2&auto=format&ar=1%3A1",
    "name": "The Columbia Inn",
    "dsc": "Plain Thin Crust Pizza - 4 Pack",
    "price": 79,
    "rate": 5,
    "country": "Montville, NJ"
  }
    # Add the rest of the pizza data here...
]

# Route to get all pizzas
@app.route('/api/pizzas', methods=['GET'])
def get_pizzas():
    return jsonify(pizzas)

# Route to get a specific pizza by ID
@app.route('/api/pizzas/<int:pizza_id>', methods=['GET'])
def get_pizza(pizza_id):
    pizza = next((p for p in pizzas if p['id'] == pizza_id), None)
    if pizza:
        return jsonify(pizza)
    else:
        return jsonify({"message": "Pizza not found"}), 404

# Route to filter pizzas by country
@app.route('/api/pizzas/filter', methods=['GET'])
def filter_pizzas():
    country = request.args.get('country')
    if country:
        filtered_pizzas = [p for p in pizzas if p['country'] == country]
        return jsonify(filtered_pizzas)
    else:
        return jsonify({"message": "Please provide a country parameter"}), 400

# Start the server
if __name__ == '__main__':
    app.run(debug=True)