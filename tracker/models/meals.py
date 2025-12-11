from django.db import models
from django.utils import timezone
from .user import CustomUser
from .food import Food

class Meal(models.Model):
    MEAL_TYPE = [
        ('breakfast','Breakfast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),
        ('snacks','Snacks')
    ]
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="meals")
    meal_type = models.CharField(max_length=20,choices=MEAL_TYPE)
    food = models.ForeignKey(Food,on_delete=models.CASCADE,related_name="meals")
    quantity = models.FloatField(help_text="Quantity in grams",default=100)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.user.username} --- {self.meal_type}"
    
    
    @property
    def total_protein(self):
        return round((self.food.protein)*(self.quantity)/100,2)
    
    @property
    def total_carbs(self):
        return round((self.food.carbs)*(self.quantity)/100,2)
    
    @property
    def total_fats(self):
        return round((self.food.fat)*(self.quantity)/100,2)  
    
    @property
    def total_calories(self):
        return round((self.food.calories)*(self.quantity)/100,2)