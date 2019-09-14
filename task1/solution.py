

def get_matching_meals(meal_data, food_ids):
    """
    Returns all the meal IDs in meal_data that have all of the given food IDs.
    :param meal_data: list of dictionary of meals
    :param food_ids: list of food IDs.
    :return: list of int: The matching meal IDs
    """
    try:
        if not food_ids or not meal_data:
            return []
        meal_plan = []
        for i in meal_data:
            foods = []
            if 'meal_id' not in i.keys():
                raise KeyError("meal_id key is not present in meal_data")
            if 'foods' not in i.keys():
                raise KeyError("foods key is not present in meal_data")
            for j in i['foods']:
                if 'food_id' not in j.keys():
                    raise KeyError("food_id key is not present in meal_data[foods]")
                if j['food_id'] in food_ids:
                    foods.append(j['food_id'])
            if foods == food_ids:
                meal_plan.append(i['meal_id'])
        return meal_plan
    except KeyError as error:
        return str(error)
