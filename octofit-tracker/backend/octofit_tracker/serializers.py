from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), source='team', write_only=True, required=False
    )
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'team', 'team_id', 'is_active', 'date_joined']
        read_only_fields = ['id', 'date_joined']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'activity_type', 'duration_minutes', 'distance_km', 'calories_burned', 'date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), source='team', write_only=True
    )
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'team_id', 'total_points', 'week_start', 'week_end']
        read_only_fields = ['id']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'duration_minutes', 'suggested_for']
        read_only_fields = ['id']
