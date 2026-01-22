from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create_user(email="test@example.com", password="testpass", team=self.team)

    def test_user_creation(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.team, self.team)
        self.assertTrue(self.user.check_password("testpass"))

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Team Alpha")
        self.assertEqual(team.name, "Team Alpha")

class ActivityModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create_user(email="test2@example.com", password="testpass", team=self.team)
        self.activity = Activity.objects.create(user=self.user, activity_type="run", duration_minutes=30, date="2024-01-01")

    def test_activity_creation(self):
        self.assertEqual(self.activity.user, self.user)
        self.assertEqual(self.activity.activity_type, "run")

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, week_start="2024-01-01", week_end="2024-01-07")

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.team, self.team)
        self.assertEqual(self.leaderboard.total_points, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Pushups", description="Do pushups", difficulty="easy", duration_minutes=10)
        self.assertEqual(workout.name, "Pushups")
        self.assertEqual(workout.difficulty, "easy")

class APIRootTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        response = self.client.get(reverse('api_root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
