from flask import Blueprint, request, jsonify
from services.customer_service import CustomerService

customer_bp = Blueprint("customer_bp", __name__)
service = CustomerService()


@customer_bp.route("/", methods=["POST"])
def create_customer():
    data = request.json

    # Basic input validation
    if not data or "id" not in data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        customer = service.create_customer(
            data["id"], data["name"], data["email"]
        )
        return jsonify(customer.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@customer_bp.route("/<customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = service.get_customer(customer_id)

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify(customer.to_dict()), 200


@customer_bp.route("/", methods=["GET"])
def get_all_customers():
    return jsonify(service.get_all_customers()), 200


@customer_bp.route("/<customer_id>", methods=["PUT"])
def update_customer(customer_id):
    data = request.json

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        customer = service.update_customer(
            customer_id, data["name"], data["email"]
        )
        return jsonify(customer.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@customer_bp.route("/<customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    try:
        service.delete_customer(customer_id)
        return jsonify({"message": "Customer deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
