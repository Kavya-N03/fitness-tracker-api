from django.db import models
from .user import CustomUser
from django.utils import timezone

class FitnessActivity(models.Model):

    ACTIVITY_CHOICES = [
        ('walk','Walking'),
        ('run','Running'),
        ('swim','Swimming'),
        ('cycle','Cycling'),
        ('yoga','Yoga')
    ]

    MET_VALUES = {
        'run': 10,
        'walk': 3.5,
        'swim': 9,
        'yoga': 2.5,
        'cycle': 8
    }

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="activities")
    activity = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    duration = models.PositiveIntegerField(help_text="Duration in Minutes")
    date = models.DateField(default=timezone.localdate)

    def __str__(self):
        return f"{self.user.username} --- {self.activity}"

    @property
    def calories_burned(self):
        met = self.MET_VALUES.get(self.activity, 1)

        if self.user.weight and self.duration:
            hours = self.duration / 60
            calories = met * self.user.weight * hours
            return round(calories, 2)

        return 0
