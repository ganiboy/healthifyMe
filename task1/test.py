from solution import get_matching_meals

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
    },
]


def test_positive():
    assert get_matching_meals(meal_data, [1, 10]) == [1, 3]
    assert get_matching_meals(meal_data, [1]) == [1, 2, 3]
    assert get_matching_meals(meal_data, [11]) == [2, 3]
    assert get_matching_meals(meal_data, [10]) == [1, 3, 4]
    assert get_matching_meals(meal_data, [1, 11]) == [2, 3]
    assert get_matching_meals(meal_data, [1, 10, 11]) == [3]


def test_negative_test_cases():

        assert get_matching_meals(meal_data, []) == []
        assert get_matching_meals(meal_data, None) == []
        assert get_matching_meals(None, None) == []
        assert get_matching_meals(None, [11]) == []
        assert get_matching_meals([], [11]) == []
        assert get_matching_meals([{}], [11]) == "'meal_id key is not present in meal_data'"

        assert get_matching_meals([
            {"id": 1,"foods": [{"food_id": 1,"food_name": "Idli"},{"food_id": 10,"food_name": "Sambar"}]}], [11]) == \
            "'meal_id key is not present in meal_data'"

        assert get_matching_meals([
            {"meal_id": 1, "food": [{"food_id": 1, "food_name": "Idli"},
                                    {"food_id": 10, "food_name": "Sambar"}]}], [11]) == \
                                        "'foods key is not present in meal_data'"

        assert get_matching_meals([
            {"meal_id": 1, "foods": [{"id": 1, "food_name": "Idli"},
                                    {"id": 10, "food_name": "Sambar"}]}], [11]) == \
                                    "'food_id key is not present in meal_data[foods]'"

        assert get_matching_meals([
            {"id": 1, "foods": [{"food_id": 1, "food_name": "Idli"}, {"food_id": 10, "food_name": "Sambar"}]}], []) == \
               []

