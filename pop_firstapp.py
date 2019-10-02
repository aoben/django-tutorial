
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

##Fake pop script
import random
from firstapp.models import AccessRecord, Topic, Webpage
from faker import Faker 

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()

    return t

def populate(N=5):

    for entry in range(N):

        #get the topic for the entry
        top = add_topic()

        #create the fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url = fake_url, name=fake_name)[0]

        #create a fake access record for that webpage

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("population complete!")