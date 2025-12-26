from flask import Flask
from routes.customer_routes import customer_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprint for customer routes
    app.register_blueprint(customer_bp, url_prefix="/api/customers")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
