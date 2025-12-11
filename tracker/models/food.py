from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    protein = models.FloatField(help_text="Protein per 100g (g)")
    carbs = models.FloatField(help_text="Carbs per 100g (g)")
    fat = models.FloatField(help_text="Fat per 100g (g)")
    calories = models.FloatField(help_text="Calories per 100g (kcal)")
    
    def __str__(self):
        return self.name
    
   
    