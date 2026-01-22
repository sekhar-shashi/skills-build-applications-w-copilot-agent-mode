from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        for team in Team.objects.all():
            if team.id:
                team.delete()
        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            User.objects.create_user(email='tony@marvel.com', password='ironman', team=marvel, username='Iron Man'),
            User.objects.create_user(email='steve@marvel.com', password='captain', team=marvel, username='Captain America'),
            User.objects.create_user(email='bruce@marvel.com', password='hulk', team=marvel, username='Hulk'),
            User.objects.create_user(email='clark@dc.com', password='superman', team=dc, username='Superman'),
            User.objects.create_user(email='bruce@dc.com', password='batman', team=dc, username='Batman'),
            User.objects.create_user(email='diana@dc.com', password='wonderwoman', team=dc, username='Wonder Woman'),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Morning Run', description='5km easy run', difficulty='easy', duration_minutes=30, suggested_for='all'),
            Workout.objects.create(name='HIIT Blast', description='High intensity interval training', difficulty='hard', duration_minutes=45, suggested_for='advanced'),
            Workout.objects.create(name='Yoga Flow', description='Flexibility and balance', difficulty='medium', duration_minutes=40, suggested_for='all'),
        ]

        # Create activities
        today = timezone.now().date()
        for user in users:
            Activity.objects.create(user=user, activity_type='Running', duration_minutes=30, distance_km=5, calories_burned=300, date=today)
            Activity.objects.create(user=user, activity_type='Cycling', duration_minutes=60, distance_km=20, calories_burned=600, date=today - timedelta(days=1))

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, total_points=150, week_start=today - timedelta(days=7), week_end=today)
        Leaderboard.objects.create(team=dc, total_points=120, week_start=today - timedelta(days=7), week_end=today)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
