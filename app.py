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
from util.db_connection_util import get_db_connection
import logging
from logging.handlers import RotatingFileHandler
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
service = CatalogueService()

# ----------------- Logging Configuration ----------------- #
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler = RotatingFileHandler('logs/app.log', maxBytes=1000000, backupCount=3)
log_handler.setLevel(logging.INFO)
log_handler.setFormatter(log_formatter)
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)

# ----------------- Swagger Configuration ----------------- #
swagger = Swagger(app)

# ---------------------- UI ROUTES ---------------------- #
@app.route("/")
def home():
    return render_template("login.html")

@app.route("/index")
def index_page():
    return render_template("index.html")

@app.route("/login-page")
def login_page():
    return render_template("login.html")

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

# ---------------------- CATALOGUE API ROUTES ---------------------- #
@app.route("/catalogues", methods=["POST"])
@swag_from({
    'responses': {
        201: {"description": "Catalogue created successfully"},
        400: {"description": "Validation error"},
        500: {"description": "Internal server error"}
    },
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'catalogue_name': {'type': 'string'},
                    'catalogue_description': {'type': 'string'},
                    'start_date': {'type': 'string'},
                    'end_date': {'type': 'string'}
                },
                'required': ['catalogue_name', 'catalogue_description', 'start_date', 'end_date']
            }
        }
    ]
})
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
        return jsonify({"status": "success", "message": "Catalogue created successfully"}), 201

    except CatalogueException as e:
        return jsonify({"status": "fail", "error": str(e)}), 400
    except Exception as e:
        return jsonify({"status": "fail", "error": f"Error creating catalogue: {str(e)}"}), 500


@app.route("/catalogues/<int:catalogue_id>", methods=["GET"])
@swag_from({
    'parameters': [
        {
            'name': 'catalogue_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Catalogue ID to retrieve'
        }
    ],
    'responses': {
        200: {"description": "Catalogue fetched successfully"},
        404: {"description": "Catalogue not found"}
    }
})
def get_catalogue_by_id(catalogue_id):
    try:
        validate_catalogue_id(catalogue_id)
        result = service.get_catalogue_by_id(catalogue_id)
        return jsonify({"status": "success", "data": result}), 200

    except CatalogueException as e:
        return jsonify({"status": "fail", "error": str(e)}), 404
    except Exception as e:
        return jsonify({"status": "fail", "error": f"Error fetching catalogue: {str(e)}"}), 500


@app.route("/catalogues", methods=["GET"])
@swag_from({
    'parameters': [
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': 'Page number for pagination'
        },
        {
            'name': 'limit',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': 'Number of items per page'
        },
        {
            'name': 'id',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'Search by catalogue ID'
        }
    ],
    'responses': {
        200: {"description": "List of catalogues returned"},
        500: {"description": "Error fetching catalogues"}
    }
})
def get_all_catalogues():
    try:
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 5))
        search_id = request.args.get("id")

        all_catalogues = service.get_all_catalogues()

        if search_id:
            all_catalogues = [
                cat for cat in all_catalogues
                if str(cat.get("catalogue_id")) == str(search_id)
            ]

        total = len(all_catalogues)
        start = (page - 1) * limit
        end = start + limit
        paginated = all_catalogues[start:end]

        return jsonify({
            "status": "success",
            "data": paginated,
            "total": total
        }), 200

    except Exception as e:
        return jsonify({"status": "fail", "error": f"Error fetching catalogues: {str(e)}"}), 500


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
        return jsonify({"status": "success", "message": "Catalogue updated successfully"}), 200

    except CatalogueException as e:
        return jsonify({"status": "fail", "error": str(e)}), 400
    except Exception as e:
        return jsonify({"status": "fail", "error": f"Error updating catalogue: {str(e)}"}), 500


@app.route("/catalogues/<int:catalogue_id>", methods=["DELETE"])
def delete_catalogue_by_id(catalogue_id):
    try:
        validate_catalogue_id(catalogue_id)
        service.delete_catalogue_by_id(catalogue_id)
        return jsonify({"status": "success", "message": "Catalogue deleted successfully"}), 200

    except CatalogueException as e:
        return jsonify({"status": "fail", "error": str(e)}), 404
    except Exception as e:
        return jsonify({"status": "fail", "error": f"Error deleting catalogue: {str(e)}"}), 500


@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            return jsonify({
                "status": "success",
                "message": "Login successful!",
                "token": "demo-token"
            }), 200
        else:
            return jsonify({
                "status": "fail",
                "error": "Invalid username or password"
            }), 401
    except Exception as e:
        return jsonify({
            "status": "fail",
            "error": str(e)
        }), 500


# ---------------------- RUN FLASK SERVER ---------------------- #
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
