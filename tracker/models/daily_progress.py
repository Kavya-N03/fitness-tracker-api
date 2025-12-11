from django.db import models
from django.utils import timezone
from .user import CustomUser

class DailyProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="daily_progress")
    date = models.DateField(default=timezone.now)

    # Weight fields (optional)
    start_weight = models.FloatField(null=True, blank=True)
    end_weight = models.FloatField(null=True, blank=True)

    # Calories per meal type
    breakfast_calories = models.FloatField(default=0)
    lunch_calories = models.FloatField(default=0)
    dinner_calories = models.FloatField(default=0)
    snack_calories = models.FloatField(default=0)

    # Totals
    calories_consumed = models.FloatField(default=0)
    calories_burned = models.FloatField(default=0)
    net_calories = models.FloatField(default=0)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user.username} --- {self.date}"

    def update_total_and_net(self):
        self.calories_consumed = (
            self.breakfast_calories +
            self.lunch_calories +
            self.dinner_calories +
            self.snack_calories
        )
        self.net_calories = self.calories_consumed - self.calories_burned
        self.save()
        

     

        
