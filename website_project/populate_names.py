import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website_project.settings')

import django
django.setup()

# Fake pop script
import random
from webapp.models import User
from faker import Faker

fakegen = Faker()

def populate(N = 5):
    for entry in range(N):
        # Create fake data for entry
        fake_first_name = fakegen.company()
        fake_last_name = fakegen.company()
        fake_email = fakegen.email()


        # Create the new users entry
        users = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]



if __name__ == '__main__':
    print ('Populating Scripts')
    populate(20)
    print ('Populating Done!')
