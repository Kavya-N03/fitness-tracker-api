from django.contrib import admin
from .models.user import CustomUser
from .models.goals import FitnessGoals
from .models.activities import FitnessActivity
from .models.food import Food
from .models.meals import Meal
from .models.daily_progress import DailyProgress
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Food)
admin.site.register(Meal)
admin.site.register(DailyProgress)
admin.site.register(FitnessGoals)
admin.site.register(FitnessActivity)