from flask_api import status
from global_exception_handler import *


def validate_params(param, data_type, error_msg):
    if not type(param) == data_type:
        if param is not None:
            raise ValidationError(error_msg, status.HTTP_400_BAD_REQUEST)


def validate_keys(data, key, datatype):
    try:
        if data['meal_data']:
            validate_params(data[key], datatype, "%s data type mismatch, %s expected to be %s" % (key, key, datatype))
            return data[key]
    except ValidationError as err:
        raise ValidationError(err.msg, err.status_code)
    except Exception as _:
        raise ValidationError("%s is missing in request body" % key, status.HTTP_400_BAD_REQUEST)
