import os
import random
import django
from faker import Faker
#
os.environ.setdefault('DJANGO_SETTINGS_MODULE','webbrain.settings')


django.setup()

from django.contrib.auth.models import User
from students.models import *

# user=User.objects.get(username='admin')

fakegen:Faker = Faker()


def populate(n=10):
    l = ['senior','middle','strong middle','strong junior']
    for i in range(n):
        name = fakegen.name()
        a = name.split()
        firstname,surname = a[0],a[1]
        degree = random.randint(1,5)
        Student.objects.create(name=firstname,
                                surname=surname,
                                degree=degree
                                )
    for i in range(n//2):
        name = fakegen.name()
        fullname = name
        seniority = random.choice(l)
        Teacher.objects.create(
                            fullname=fullname,
                            seniority=seniority
        )


if __name__=='__main__':
    print('Populating....')
    populate(20)
    print('Populating end')