from flask import Flask
from routes.products_routes import products
from routes.categories_routes import categories

app = Flask(__name__)

app.register_blueprint(products)
app.register_blueprint(categories)

if __name__ == "__main__":
    app.run('0.0.0.0', 8086)
