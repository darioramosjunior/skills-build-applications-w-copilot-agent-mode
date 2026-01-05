from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User = get_user_model()
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass', team=dc),
        ]

        # Create activities
        activities = [
            app_models.Activity.objects.create(user=users[0], type='run', duration=30, distance=5),
            app_models.Activity.objects.create(user=users[1], type='cycle', duration=45, distance=15),
            app_models.Activity.objects.create(user=users[2], type='swim', duration=60, distance=2),
            app_models.Activity.objects.create(user=users[3], type='run', duration=25, distance=4),
        ]

        # Create workouts
        workouts = [
            app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes'),
            app_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes'),
        ]

        # Create leaderboard
        app_models.Leaderboard.objects.create(user=users[0], points=100)
        app_models.Leaderboard.objects.create(user=users[1], points=90)
        app_models.Leaderboard.objects.create(user=users[2], points=95)
        app_models.Leaderboard.objects.create(user=users[3], points=85)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
