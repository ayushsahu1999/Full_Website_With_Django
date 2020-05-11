import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advcbv.settings')
import random
import django
django.setup()

# Fake pop script
import random
from basic_app.models import School, Student
from faker import Faker

fakegen = Faker()

def populate(N = 5):
    for entry in range(N):
        # Create fake data for entry
        fake_school_name = fakegen.company()
        fake_principal = fakegen.name()
        fake_location = fakegen.street_name()
        fake_student_name = fakegen.name()
        fake_age = random.randint(4, 15)

        # Create the new schools entry
        schools = School.objects.get_or_create(name=fake_school_name, principal=fake_principal, location=fake_location)[0]

        # Create the new students entry
        students = Student.objects.get_or_create(name=fake_student_name, age=fake_age, school=schools)



if __name__ == '__main__':
    print ('Populating Scripts')
    populate(20)
    print ('Populating Done!')
