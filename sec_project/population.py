import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sec_project.settings')

import django
django.setup()

from first_app.models import User
from faker import Faker

fakegen = Faker("pl_PL")

def populate(N=10):

    for entry in range(N):

        fake_name = fakegen.first_name()
        fake_surname = fakegen.last_name()
        fake_mail = fakegen.email()

        User.objects.get_or_create(name = fake_name, surname = fake_surname, mail = fake_mail)

if __name__ == '__main__':
    print('creating')
    populate(30)
    print('done')

