from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.utils import timezone

from .models.activities import FitnessActivity
from .models.meals import Meal
from .models.daily_progress import DailyProgress

def get_progress(user):
    today = timezone.now().date()
    progress,created = DailyProgress.objects.get_or_create(
        user=user,
        date = today
    )
    return progress

def calculate_meal_type_total(user,meal_type):
    meals = Meal.objects.filter(
        user=user,
        meal_type=meal_type,
        date = timezone.now().date()
    )
    total = sum([meal.total_calories for meal in meals])
    return total

@receiver([post_save,post_delete],sender = Meal)
def update_meal_calories(sender , instance ,**kwargs):
    user = instance.user
    meal_type = instance.meal_type
    progress = get_progress(user)
    
    if meal_type == "breakfast":
        progress.breakfast_calories = calculate_meal_type_total(user,"breakfast")
    elif meal_type == "lunch":
        progress.lunch_calories = calculate_meal_type_total(user,"lunch")
    elif meal_type == "dinner":
        progress.dinner_calories = calculate_meal_type_total(user,"dinner")
    elif meal_type == "snacks":
        progress.snack_calories = calculate_meal_type_total(user, "snacks")
        
    progress.update_total_and_net()
    progress.save()
    
@receiver([post_save,post_delete],sender=FitnessActivity)
def update_burned_calories(sender,instance,**kwargs):
    user = instance.user
    progress = get_progress(user)
    
    activities = FitnessActivity.objects.filter(
        user=user,
        date = timezone.now().date()
    )
    progress.calories_burned = sum([a.calories_burned for a in activities])
    progress.update_total_and_net()
    progress.save()