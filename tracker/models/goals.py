from django.db import models
from .user import CustomUser

class FitnessGoals(models.Model):
    GOAL_CHOICES = [
        ('lose','Lose Weight'),
        ('gain','Gain Weight'),
        ('fitness','Maintain Fitness'),
    ]
    STATUS_CHOICES = [
        ('active','Active'),
        ('paused','Paused'),
        ('completed','Completed')
    ]
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="goals")
    title = models.CharField(max_length=255)
    goal = models.CharField(max_length=20,choices=GOAL_CHOICES)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)
    start_weight = models.FloatField(default=0)
    current_weight = models.FloatField(default=0)
    target_weight = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} --- {self.title}"
    
    @property
    def progress_percentage(self):
        try:
            if self.goal == "lose" and self.start_weight!=self.target_weight:
                progress  = ((self.start_weight-self.current_weight)/
                             (self.start_weight-self.target_weight))*100
                
            elif self.goal == "gain" and self.start_weight!=self.target_weight:
                progress = ((self.current_weight-self.start_weight)/
                            (self.target_weight-self.start_weight))*100
                
            elif self.goal == 'fitness' and self.start_weight != 0:
                difference = abs(self.current_weight - self.target_weight)
                progress = max(0, 100 - (difference / self.start_weight) * 100)

            else:
                progress = 0
            
            return f"{round(progress,2)}"  
        
        except ZeroDivisionError:
            return 0              
                           
                
            
            
    

    
    