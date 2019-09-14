**TASK-2:**

Expose the python function created for task 1 as an API through a simple web application
framework like flask/bottle or any other framework you are most comfortable with.

**Solution:**

**Web Framework Used**: Flask

**Code Walk-Through:**

1. **global_exception_handler.py**: Defined custom exception (ValidationError, KeyError)

2. **validate_request_body.py**: Responsible for validating all the request parameters keys as well as their 
expected datatype. If there is any mismatch it would throw  ValidationError with detailed error 
message for that particular parameter.

3. **app.py**: This contains core function which is responsible for accepting a request and returning response.

4. **test_app.py:** This contains unit test cases.

**Unit Testing:**


Request Body:

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
              ],
              "food_ids" : [1, 10]
            }

Headers:

    {"Content-Type": "application/json"}

End Point: 

    /get_meals

Few Test cases with request and response are below where data is passed as a request_body,

	Request Body	                                        Status-Code	    Response
			
	data["meal_data"], data["food_ids"] = [1, 10]               200	    {"meal_ids": [1, 3], "status": "Success"}
    
	data["meal_data"], data["food_ids"] = [1]                   200     {"meal_ids": [1, 2, 3], "status": "Success"}

	data["meal_data"]                                           400	    {"error_message": "food_ids is missing in request body", "status": "Failed"}

	data["meal_data"],data['food_ids'] = 1	                    400	    {"error_message": "food_ids data type mismatch, 
	                                                                        food_ids , expected to be <class 'list'>", 
	                                                                        "status": "Failed"}

	data["meal_data"] = 1,data['food_ids'] = [1]	            400	    {"error_message": "meal_data data type mismatch, 
	                                                                        meal_data expected to be <class 'list'>", 
	                                                                        "status": "Failed"}

	data["food_ids"] = [1, 10]                                  400	    {"error_message": "meal_data is missing in request body", "status": "Failed"}

	data = {}                                                   400	    {"error_message": "meal_data and food_ids are 
	                                                                        missing in request body","status": "Failed"}

	data["meal_data"]= [{"meal_data" : [{"id": 1,
	"foods": 
	[{"food_id": 1,"food_name": "Idli"},                         400	{"error_message": "meal_id key is not present 
	{"food_id": 10,"food_name": "Sambar"}]}]}],                             in meal_data","status": "Failed"}
	data["food_ids"] = [10]	                        

	data["meal_data"]= [{"meal_id": 1, 
	"food": [{"food_id": 1, "food_name": "Idli"},                400	{"error_message": "foods key is not present 
	{"food_id": 10, "food_name": "Sambar"}]}],                              in meal_data","status": "Failed"}
	data["food_ids"] = [10]	                                
	
	data["meal_data"]= 
	[{"meal_id": 1, "foods": [{"id": 1,                          400	{"error_message": "'food_id key is not present
	"food_name": "Idli"}, {"id": 10,                                         in meal_data[foods]'","status": "Failed"}
	"food_name": "Sambar"}]}],data["food_ids"] = [10]	


cmd to run pytest: 

        python3 -m pytest /HealthifyMe/task2/test_app.py

cmd to run flask app:

        