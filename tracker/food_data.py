from .models.food import Food

def load_food_data():
    food_data =[
        {"name": "Rice (Cooked)", "protein": 2.7, "carbs": 28.0, "fat": 0.3, "calories": 130},
        {"name": "Boiled Egg", "protein": 6.3, "carbs": 0.6, "fat": 5.3, "calories": 78},
        {"name": "Grilled Chicken Breast", "protein": 31.0, "carbs": 0.0, "fat": 3.6, "calories": 165},
        {"name": "Banana", "protein": 1.1, "carbs": 23.0, "fat": 0.3, "calories": 96},
        {"name": "Apple", "protein": 0.3, "carbs": 14.0, "fat": 0.2, "calories": 52},
        {"name": "Milk (Whole)", "protein": 3.3, "carbs": 4.8, "fat": 3.3, "calories": 61},
        {"name": "Oats", "protein": 13.0, "carbs": 68.0, "fat": 7.0, "calories": 389},
        {"name": "Paneer", "protein": 18.0, "carbs": 1.2, "fat": 20.0, "calories": 265},
        {"name": "Chapati", "protein": 3.0, "carbs": 18.0, "fat": 1.5, "calories": 97},
        {"name": "Dal (Cooked)", "protein": 9.0, "carbs": 26.0, "fat": 1.0, "calories": 150},
    ]
    
    for food in food_data:
        Food.objects.get_or_create(**food)
    print("Food Loaded")