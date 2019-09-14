import json
from app import *


data = {
  "meal_data": [
    {
      "meal_id": 1,
      "foods": [
        {
          "food_id": 1,
          "food_name": "Idli"
        },
        {
          "food_id": 10,
          "food_name": "Sambar"
        }
      ]
    },
    {
      "meal_id": 2,
      "foods": [
        {
          "food_id": 1,
          "food_name": "Idli"
        },
        {
          "food_id": 11,
          "food_name": "Chutney"
        }
      ]
    },
    {
      "meal_id": 3,
      "foods": [
        {
          "food_id": 1,
          "food_name": "Idli"
        },
        {
          "food_id": 10,
          "food_name": "Sambar"
        },
        {
          "food_id": 11,
          "food_name": "Chutney"
        }
      ]
    },
    {
      "meal_id": 4,
      "foods": [
        {
          "food_id": 2,
          "food_name": "Dosa"
        },
        {
          "food_id": 10,
          "food_name": "Sambar"
        }
      ]
    }
  ]
}


def test_positive_cases():
    client = app.test_client()
    url = '/get_meals'
    # test 1
    data["food_ids"] = [1, 10]
    response = client.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert json.loads(response.data) == {"meal_ids": [1, 3], "status": "Success"}

    # test 2
    data["food_ids"] = [1]
    response = client.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert json.loads(response.data) == {"meal_ids": [1, 2, 3], "status": "Success"}


def test_not_passing_food_id():
    client = app.test_client()
    url = '/get_meals'
    del data['food_ids']
    response = client.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert json.loads(response.data) == {"error_message": "food_ids is missing in request body", "status": "Failed"}


def test_passing_different_datatype_food_id():
    client = app.test_client()
    url = '/get_meals'

    data['food_ids'] = 1
    response = client.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert json.loads(response.data) == {"error_message": "food_ids data type mismatch, food_ids "
                                                          "expected to be <class 'list'>", "status": "Failed"}


def test_passing_different_datatype_meals():
    client = app.test_client()
    url = '/get_meals'
    data['meal_data'] = 1
    response = client.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert json.loads(response.data) == {"error_message": "meal_data data type mismatch, "
                                                          "meal_data expected to be <class 'list'>", "status": "Failed"}


def test_not_passing_meals():
    client = app.test_client()
    url = '/get_meals'
    del data['meal_data']
    data["food_ids"] = [1, 10]
    response = client.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert json.loads(response.data) == {"error_message": "meal_data is missing in request body", "status": "Failed"}


def test_not_passing_meals_and_food_id():
    client = app.test_client()
    url = '/get_meals'
    data = {}
    response = client.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert json.loads(response.data) == {"error_message": "meal_data and food_ids are missing in request body",
                                         "status": "Failed"}


def test_not_passing_meal_id():
    client = app.test_client()
    url = '/get_meals'
    data = {"meal_data" : [{"id": 1,"foods": [{"food_id": 1,"food_name": "Idli"},{"food_id": 10,"food_name": "Sambar"}]}]}
    data["food_ids"] = [10]
    response = client.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert json.loads(response.data) == {"error_message": "'meal_id key is not present in meal_data'",
                                         "status": "Failed"}


def test_not_passing_foods_key():
    client = app.test_client()
    url = '/get_meals'
    data = {"meal_data" : [{"meal_id": 1, "food": [{"food_id": 1, "food_name": "Idli"}, {"food_id": 10, "food_name": "Sambar"}]}]}
    data["food_ids"] = [10]
    response = client.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert json.loads(response.data) == {"error_message": "'foods key is not present in meal_data'",
                                         "status": "Failed"}


def test_not_passing_food_id_key():
    client = app.test_client()
    url = '/get_meals'
    data = {"meal_data" : [{"meal_id": 1, "foods": [{"id": 1, "food_name": "Idli"},{"id": 10, "food_name": "Sambar"}]}]}
    data["food_ids"] = [10]
    response = client.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert json.loads(response.data) == {"error_message": "'food_id key is not present in meal_data[foods]'",
                                         "status": "Failed"}
