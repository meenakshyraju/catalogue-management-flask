from flask import Flask, request, jsonify, render_template
from service.catalogue_service import CatalogueService
from dto.catalogue import Catalogue
from util.validators import (
    validate_catalogue_name,
    validate_description,
    validate_date_format,
    validate_catalogue_id
)
from exception.catalogue_custom_exceptions import CatalogueException

app = Flask(__name__)
service = CatalogueService()

# ---------------------- UI ROUTES ---------------------- #
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create")
def create_page():
    return render_template("create.html")

@app.route("/update")
def update_page():
    return render_template("update.html")

@app.route("/delete")
def delete_page():
    return render_template("delete.html")

@app.route("/view")
def view_page():
    return render_template("view_all.html")

# ---------------------- API ROUTES ---------------------- #

@app.route("/catalogues", methods=["POST"])
def create_catalogue():
    try:
        data = request.get_json()
        validate_catalogue_name(data.get("catalogue_name"))
        validate_description(data.get("catalogue_description"))
        validate_date_format(data.get("start_date"))
        validate_date_format(data.get("end_date"))

        catalogue = Catalogue(
            catalogue_name=data.get("catalogue_name"),
            catalogue_description=data.get("catalogue_description"),
            start_date=data.get("start_date"),
            end_date=data.get("end_date")
        )

        service.create_catalogue(catalogue)
        return jsonify({"message": "Catalogue created successfully"}), 201

    except CatalogueException as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Error creating catalogue: {str(e)}"}), 500

@app.route("/catalogues/<int:catalogue_id>", methods=["GET"])
def get_catalogue_by_id(catalogue_id):
    try:
        validate_catalogue_id(catalogue_id)
        result = service.get_catalogue_by_id(catalogue_id)
        return jsonify(result), 200

    except CatalogueException as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Error fetching catalogue: {str(e)}"}), 500

@app.route("/catalogues", methods=["GET"])
def get_all_catalogues():
    try:
        result = service.get_all_catalogues()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": f"Error fetching catalogues: {str(e)}"}), 500

@app.route("/catalogues/<int:catalogue_id>", methods=["PUT"])
def update_catalogue_by_id(catalogue_id):
    try:
        data = request.get_json()
        validate_catalogue_id(catalogue_id)
        validate_catalogue_name(data.get("catalogue_name"))
        validate_description(data.get("catalogue_description"))
        validate_date_format(data.get("start_date"))
        validate_date_format(data.get("end_date"))

        updated_catalogue = Catalogue(
            catalogue_name=data.get("catalogue_name"),
            catalogue_description=data.get("catalogue_description"),
            start_date=data.get("start_date"),
            end_date=data.get("end_date")
        )

        service.update_catalogue_by_id(catalogue_id, updated_catalogue)
        return jsonify({"message": "Catalogue updated successfully"}), 200

    except CatalogueException as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Error updating catalogue: {str(e)}"}), 500

@app.route("/catalogues/<int:catalogue_id>", methods=["DELETE"])
def delete_catalogue_by_id(catalogue_id):
    try:
        validate_catalogue_id(catalogue_id)
        service.delete_catalogue_by_id(catalogue_id)
        return jsonify({"message": "Catalogue deleted successfully"}), 200

    except CatalogueException as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Error deleting catalogue: {str(e)}"}), 500

# ---------------------- Run Server ---------------------- #

if __name__ == "__main__":
    """
    Entry point to run the Flask app.
    """
    app.run(debug=True, host="0.0.0.0")
