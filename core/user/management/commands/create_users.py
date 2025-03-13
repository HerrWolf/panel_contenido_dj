from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from core.user.models import User
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generate random users to populate the database'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=0,
                            help='Number of users to generate')

    def handle(self, *args, **options):
        count = options['count']

        # If count is not provided via argument, ask interactively
        if count == 0:
            count = int(input('How many users do you want to create? '))

        faker = Faker()
        groups = list(Group.objects.all())

        self.stdout.write(self.style.SUCCESS(f'Creating {count} users...'))

        for i in range(count):
            first_name = faker.first_name()
            last_name = faker.last_name()
            username = f"{first_name.lower()}.{last_name.lower()}"

            # Handle username duplicates
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{first_name.lower()}.{last_name.lower()}{counter}"
                counter += 1

            user = User.objects.create(
                username=username,
                email=f"{username}@example.com",
                first_name=first_name,
                last_name=last_name
            )

            # Set a password
            password = "password123"
            user.set_password(password)

            # Randomly assign groups if they exist
            if groups:
                num_groups = random.randint(0, min(3, len(groups)))
                selected_groups = random.sample(groups, num_groups)
                user.groups.set(selected_groups)

            user.save()

            self.stdout.write(f"Created user {i + 1}/{count}: {username}")

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} users!'))
        self.stdout.write(self.style.WARNING(f'Default password for all users: "password123"'))