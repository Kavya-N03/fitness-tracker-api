from rest_framework import viewsets,generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter,OrderingFilter
from django.utils import timezone
from .models.user import CustomUser
from .models.goals import FitnessGoals
from .models.activities import FitnessActivity
from .models.food import Food
from .models.meals import Meal
from .models.daily_progress import DailyProgress
from .serializers import (UserSerializer,FitnessGoalSerializer,FitnessActivitySerializer,
                         FoodSerializer,MealSerializer,DailyProgressSerializer)
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
    def perform_update(self, serializer):
        serializer.save()
    

class CurrentUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user


class FitnessGoalsView(viewsets.ModelViewSet):
    queryset = FitnessGoals.objects.all()
    serializer_class = FitnessGoalSerializer
    permission_classes=[IsAuthenticated]
        
    
    def get_queryset(self):
        return FitnessGoals.objects.filter(user=self.request.user)   
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    
class FitnessActivityView(viewsets.ModelViewSet):
    queryset = FitnessActivity.objects.all()
    serializer_class = FitnessActivitySerializer
    permission_classes=[IsAuthenticated]
    
    
    def get_queryset(self):
        return FitnessActivity.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class FoodView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['protein','fat','carbs','calories']
    
class MealsView(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes=[IsAuthenticated]
    
    
    def get_queryset(self):
        return Meal.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class DailyProgressView(viewsets.ModelViewSet):
    queryset = DailyProgress.objects.all()
    serializer_class = DailyProgressSerializer
    permission_classes=[IsAuthenticated]
    
    
    def get_queryset(self):
        return DailyProgress.objects.filter(user=self.request.user).order_by('-date')
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
       # Disable manual creation (POST)
    def create(self, request, *args, **kwargs):
        return Response(
            {"error": "DailyProgress is automatically created via signals."},
            status=400
        )
   
    # Custom endpoint: /daily-progress/today/
    @action(detail=False, methods=['get'])
    def today(self, request):
        user = request.user
        today = timezone.now().date()

        progress, created = DailyProgress.objects.get_or_create(
            user=user,
            date=today
        )

        serializer = self.get_serializer(progress)
        return Response(serializer.data)