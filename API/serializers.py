from rest_framework import serializers
from .models import user,activity

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model= user
        fields=['id','real_name','tz']
class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model= activity
        fields=['id','user_id','start_time']
class logoutSerializer(serializers.ModelSerializer):
    class Meta:
        model= activity
        fields=['user_id','start_time','end_time']
        read_only_fields = ['end_time']
        extra_kwargs = {'user_id': {'write_only': True}}
class detailActivity(serializers.ModelSerializer):
    activity_periods=logoutSerializer(read_only=True,many=True)
    class Meta:
        model= user
        fields= ['id','real_name','tz','activity_periods']