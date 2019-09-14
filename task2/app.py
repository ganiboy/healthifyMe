from flask import Flask
from flask import request, json, Response
from flask_api import status
from datetime import date
import logging
from validate_request_body import *
import sys
import os
sys.path.append(os.getcwd() + '/task1')
from solution import get_matching_meals
from global_exception_handler import KeyError, ValidationError


app = Flask(__name__)
log_file = str(date.today()) + '.log'

logging.basicConfig(filename=log_file, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/get_meals', methods=["POST"])
def get_meal_id():
    try:
        data = request.data
        logging.debug(json.loads(data))
        data = json.loads(data)
        if not data:
            raise ValidationError("meal_data and food_ids are missing in request body", status.HTTP_400_BAD_REQUEST)

        meal_data = validate_keys(data, 'meal_data', list)
        food_ids = validate_keys(data, 'food_ids', list)
        meal_ids = get_matching_meals(meal_data, food_ids)
        if type(meal_ids) != list:
            raise KeyError(meal_ids, status.HTTP_400_BAD_REQUEST)

        logging.debug(json.dumps({"meal_ids": meal_ids, "status": "Success"}))
        response = Response(
            response=json.dumps({"meal_ids": meal_ids, "status": "Success"}),
            status=status.HTTP_200_OK,
            mimetype='application/json'
        )
        return response
    except ValidationError as error:
        logging.debug(json.dumps({"error_message": error.msg, "status": "Failed"}))
        return Response(
            response=json.dumps({"error_message": error.msg, "status": "Failed"}),
            status=error.status_code,
            mimetype='application/json'
        )
    except KeyError as error:
        logging.debug(json.dumps({"error_message": str(error.msg), "status": "Failed"}))
        return Response(
            response=json.dumps({"error_message": str(error.msg), "status": "Failed"}),
            status=status.HTTP_400_BAD_REQUEST,
            mimetype='application/json'
        )

    except Exception as _:
        logging.debug(json.dumps({"error_message": "Internal Server Error"}))
        return Response(
            response=json.dumps({"error_message": "Internal Server Error"}),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            mimetype='application/json'
        )


if __name__ == '__main__':
    app.run('0.0.0.0')
