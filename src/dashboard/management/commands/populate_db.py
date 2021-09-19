from django.core.management.base import BaseCommand
from dashboard.models import UserData
from django.contrib.auth.models import User
from random import randint


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        print("Deleting UserData and User models from the database...")
        UserData.objects.all().delete()
        User.objects.all().delete()

        print("Creating new Person and User models...")
        User.objects.create_user(username='user', password="password")
        user = User.objects.get(username='user')

        # Create the people for the database
        UserData.objects.create(user=user, name="Ryan", eye_breaks=randint(0, 100), total_break_time=randint(100, 500), liters_drunk=randint(10, 23), minutes_walked=randint(20, 59))
        UserData.objects.create(user=user, name="Gertrude", eye_breaks=randint(0, 100), total_break_time=randint(100, 500), liters_drunk=randint(10, 23), minutes_walked=randint(20, 59))
        UserData.objects.create(user=user, name="Sbeve", eye_breaks=randint(0, 100), total_break_time=randint(100, 500), liters_drunk=randint(10, 23), minutes_walked=randint(20, 59))

        # Create an admin
        User.objects.create_superuser(
            username='admin',
            email='email@gmail.com',
            password='password'
        )

        # Let the user know how to use the information
        print("\nDatabase population completed. \nUser\n\tUsername: user\n\tPassword: password\n\nAdmin\n\tUsername: admin\n\tPassword: password\n")
