**_TASK-1:_**

Given a meals dataset as a list of dictionaries (check sample_mealdata.py for example), find all the meal IDs that 
contain all the given food IDs.

Your solution must be implemented in the function get_matching_meals in solution.py.

**Solution:**

**solution.py** contains the method **get_matching_meals** which takes meal_data, food_ids as inputs 
and returns list of meal_id.

**Unit Testing:**

Unit test cases for the above function is present in test.py


**Sample meal data:**

    meal_data = [
    {
        'meal_id': 1,
        'foods': [
            {
                'food_id': 1,
                'food_name': 'Idli'
            },
            {
                'food_id': 10,
                'food_name': 'Sambar'
            },
        ]
    },
    {
        'meal_id': 2,
        'foods': [
            {
                'food_id': 1,
                'food_name': 'Idli'
            },
            {
                'food_id': 11,
                'food_name': 'Chutney'
            },
        ]
    },
    {
        'meal_id': 3,
        'foods': [
            {
                'food_id': 1,
                'food_name': 'Idli'
            },
            {
                'food_id': 10,
                'food_name': 'Sambar'
            },
            {
                'food_id': 11,
                'food_name': 'Chutney'
            },
        ]
    },
    {
        'meal_id': 4,
        'foods': [
            {
                'food_id': 2,
                'food_name': 'Dosa'
            },
            {
                'food_id': 10,
                'food_name': 'Sambar'
            },
        ]
    }]
    
Few Positive test cases along with results for the above meal data,

    meal_data, food_id          Output

    meal_data, [1, 10]          [1, 3]
    meal_data, [1]              [1, 2, 3]
    meal_data, [11]             [2, 3]
    meal_data, [10]             [1, 3, 4]
    meal_data, [1, 11]          [2, 3]
    meal_data, [1, 10, 11]      [3]
    
    
Few Negative test cases,

    meal_data, food_id                                        Output                    
                                                          
        meal_data, []                                           []                    
        meal_data, None                                         []                 
        None, None                                              []                    
        None, [11]                                              []                 
        [], [11]                                                []                    
    [{"id": 1,"foods": []}],[11]                    'meal_id key is not present in meal_data'
    [{"meal_id": 1, "food": []}], [11]              'foods key is not present in meal_data'
    
    [{"meal_id": 1,                                 'food_id key is not present in meal_data[foods]'
    "foods": [{"id": 1, "food_name": "Idli"}],[1]
    
    [{"meal_id": 1,                                 'food_id key is not present in meal_data[foods]'
    "foods": [{"id": 1, "food_name": "Idli"}],[]                []

    
cmd to run pytest: 
        
        cd /healthifyMe/task1
        python3 -m pytest test.py