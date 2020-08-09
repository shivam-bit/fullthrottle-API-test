from django.shortcuts import render
from .models import user,activity
from .serializers import userSerializer,loginSerializer,logoutSerializer,detailActivity
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status



class userView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class= userSerializer
    queryset= user.objects.all()
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class loginView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=loginSerializer
    queryset= activity.objects.all()
    def post(self,request):
        return self.create(request)
class logoutView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=logoutSerializer
    queryset= activity.objects.all()
    def get_object(self, userId):
        try:
            return activity.objects.get(user_id=userId,end_time=None)
        except activity.DoesNotExist:
            return Response({'ok':False,'message':'No active sessions'},status=status.HTTP_400_BAD_REQUEST)
        except activity.MultipleObjectsReturned:
            return Response({'ok':False,'message':'Multiple login sessions found'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self,request):
        return self.list(request)
    def post(self,request):
        session=self.get_object(request.data['user_id'])
        if isinstance(session,activity):
            session.logout()
            return Response({'ok':True},status=status.HTTP_202_ACCEPTED)
        else:
            return session

class detailView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=detailActivity
    queryset= user.objects.all()
    def get(self,request):
        usersList=self.list(request)
        usersList.data={"ok":True,"members":usersList.data}
        return usersList
