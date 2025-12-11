from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UsersView,FitnessGoalsView,FitnessActivityView,FoodView,MealsView,DailyProgressView,CurrentUserView
routers = DefaultRouter()

routers.register('users',UsersView,basename="users"),
routers.register('goals',FitnessGoalsView,basename="goals"),
routers.register('activities',FitnessActivityView,basename="activities")
routers.register('foods',FoodView,basename="foods")
routers.register('meals',MealsView,basename="meals")
routers.register('daily_progress',DailyProgressView,basename="daily_progress")

urlpatterns=[
    path('users/me/',CurrentUserView.as_view()),
    path('',include(routers.urls))  ,
]