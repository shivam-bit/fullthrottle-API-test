from django.db import models
import pytz
import datetime
from django.conf import settings
from django.utils.timezone import make_aware
# Create your models here.
class user(models.Model):
    TIMEZONES =  tuple(zip(pytz.all_timezones, pytz.all_timezones))
    real_name=models.CharField(max_length=100)
    tz=models.CharField(max_length=100,choices=TIMEZONES , default='UTC')
    def __str__(self):
        return self.real_name

class activity(models.Model):
    user_id=models.ForeignKey(user,related_name='activity_periods',on_delete=models.PROTECT)
    start_time= models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField(blank=True,null=True)
    class Meta:
        ordering=('-start_time',)
    def logout(self): 
        naive_datetime= datetime.datetime.now()
        aware_datetime= make_aware(naive_datetime)
        self.end_time= aware_datetime
        self.save()
    def __str__(self):
        return self.user_id.real_name
    
