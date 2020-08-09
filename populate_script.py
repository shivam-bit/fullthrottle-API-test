import os,django
import pytz
import datetime
import random
import factory 
import factory.django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","FullThrottle.settings")
django.setup()
from django.conf import settings
from django.utils.timezone import make_aware
from API.models import user,activity

# export DJANGO_SETTINGS_MODULE=FullThrottle.settings

class userFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=user
    real_name=factory.Faker('name')
    @factory.lazy_attribute
    def tz(self):
        TIMEZONES =  tuple(pytz.all_timezones)
        i=random.randint(0,(len(TIMEZONES)-1))
        return TIMEZONES[i]
class loginFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=activity
    user_id=factory.SubFactory(userFactory)
    @factory.lazy_attribute
    def end_time(self):
        naive_date = datetime.datetime.now() + datetime.timedelta(minutes=15)
        aware_datetime=make_aware(naive_date)
        return aware_datetime
def create_users(n):
    for _ in range(n):
        loginFactory.create()
print("Enter number of dummy data that you want to insert :")
n=int(input())
create_users(n)
print(n,"ENTRIES POPULATED SUCCESSFULLY ! ")