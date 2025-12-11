from rest_framework import serializers
from .models.user import CustomUser
from .models.goals import FitnessGoals
from .models.activities import FitnessActivity
from .models.food import Food
from .models.meals import Meal
from .models.daily_progress import DailyProgress


# ---------------------- USER ----------------------
class UserSerializer(serializers.ModelSerializer):
    bmi = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['id','username','email','profile_photo',
                  'age','gender','weight','height','bmi']

    def get_bmi(self, obj):
        return obj.bmi
    
    def validate_height(self, value):
        if value is None:
            return value
        if value <= 0 or value > 300:
            raise serializers.ValidationError("Enter a realistic height in cm.")
        return value

    def validate_weight(self, value):
        if value is None:
            return value
        if value <= 0 or value > 500:
            raise serializers.ValidationError("Enter a realistic weight in kg.")
        return value


# ---------------------- GOALS ----------------------
class FitnessGoalSerializer(serializers.ModelSerializer):
    progress_percentage = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = FitnessGoals
        fields = ['id','user','title','goal','start_weight','target_weight','current_weight','status','progress_percentage']

    def get_progress_percentage(self, obj):
        return obj.progress_percentage

    def validate(self, data):
        goal = data.get('goal')
        start_weight = data.get('start_weight')
        target_weight = data.get('target_weight')
        current_weight = data.get('current_weight')
        
        if start_weight is None or target_weight is None or current_weight is None:
            raise serializers.ValidationError("Start weight, target weight, and current weight are required.")

        # weight loss
        if goal == 'lose':
            if target_weight >= start_weight:
                raise serializers.ValidationError("Target weight must be less than start weight.")
            if current_weight < target_weight or current_weight > start_weight:
                raise serializers.ValidationError("Current weight must be between start & target weight.")
        
        # weight gain
        if goal == 'gain':
            if target_weight <= start_weight:
                raise serializers.ValidationError("Target must be greater for weight gain.")
            if current_weight > target_weight or current_weight < start_weight:
                raise serializers.ValidationError("Current weight must be between start & target weight.")

        return data


# ---------------------- ACTIVITY ----------------------
class FitnessActivitySerializer(serializers.ModelSerializer):
    calories_burned = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)
    date = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])

    class Meta:
        model = FitnessActivity
        fields = ['id','user','activity','duration','date','calories_burned']
    
    def get_calories_burned(self,obj):
        return obj.calories_burned


# ---------------------- FOOD ----------------------
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


# ---------------------- MEAL ----------------------
class MealSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    food = serializers.StringRelatedField(read_only=True)
    
    food_id = serializers.PrimaryKeyRelatedField(
        queryset = Food.objects.all(),
        source = "food",
        write_only=True
    )

    total_protein = serializers.SerializerMethodField()
    total_carbs = serializers.SerializerMethodField()
    total_fats = serializers.SerializerMethodField()
    total_calories = serializers.SerializerMethodField()

    class Meta:
        model = Meal
        fields = ['id','user','meal_type','food','food_id','quantity','date',
                  'total_protein','total_carbs','total_fats','total_calories']

    def get_total_protein(self, obj):
        return obj.total_protein

    def get_total_carbs(self, obj):
        return obj.total_carbs

    def get_total_fats(self, obj):
        return obj.total_fats

    def get_total_calories(self, obj):
        return obj.total_calories


class DailyProgressSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    net_calories = serializers.SerializerMethodField()
    class Meta:
        model = DailyProgress
        fields = '__all__'
        read_only_fields = ['user','date','breakfast_calories','lunch_calories','dinner_calories',
                            'snack_calories','calories_consumed','calories_burned','net_calories']
    
    def get_net_calories(self,obj):
        return round(obj.net_calories,2)