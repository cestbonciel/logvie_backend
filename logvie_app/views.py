from django.shortcuts import render
from rest_framework.serializers import Serializer
from logvie_app.serializers import FavoriteSerializer, DiarySerializer
from rest_framework.views import APIView
from logvie_app import serializers
from rest_framework import status
from rest_framework.response import Response
from .models import Favorite, Diary

# Create your views here.

class FavoriteView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('uid') is None:
            if request.GET.get('user_id') is None: 
                favorites = Favorite.objects.all()
            else :
                userid = request.GET.get('user_id')
                favorites = Favorite.objects.filter(user_id=userid)
            # favorites = Favorite.objects.all()
            serializer = FavoriteSerializer(favorites, many=True)
            return Response({'count':favorites.count(),'data':serializer.data},status=status.HTTP_200_OK)
        else : 
            uid = kwargs.get('uid')
            favorite = Favorite.objects.get(id=uid)
            serializer = FavoriteSerializer(favorite)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FavoriteSerializer(data = request.data)
        if serializer.is_valid():
            userid = request.POST.get('user_id')
            movieid = request.POST.get('movie_id')
            favorites = Favorite.objects.filter(user_id=userid,movie_id=movieid)
            
            print("**",favorites.count())
            print(movieid,userid)
            
            if (favorites.count() < 1 ) :

                # 저장
                # return Response
                serializer.save()
                

            return Response({'result':'success','data':serializer.data},status=status.HTTP_200_OK)        
  
        else : 

            return Response({'result':'fail','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, **kwargs):
        if kwargs.get('uid') is None:
            return Response("uid is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            uid = kwargs.get('uid')
            favorite_object = Favorite.objects.get(id=uid)
            serializer = FavoriteSerializer(favorite_object,data = request.data)
            # Key - Value 유효한지의 유무 체크 
            if serializer.is_valid():
                serializer.save()
                return Response({'result':'success','data':serializer.data},status=status.HTTP_200_OK)
            else :
                return Response("uid is required", status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, **kwargs):
        if kwargs.get('uid') is None:
            return Response("uid is required.", status=status.HTTP_400_BAD_REQUEST)
        else : 
            uid = kwargs.get('uid')
            favorite_object = Favorite.objects.get(id=uid)
            favorite_object.delete()
            return Response({'Data is deleted!'},status=status.HTTP_200_OK)

# 다이어리뷰 - CRUD 처리 
class DiaryView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('uid') is None:
            if request.GET.get('user_id') is None: 
                diaries = Diary.objects.all()
            else :
                userid = request.GET.get('user_id')
                diaries = Diary.objects.filter(user_id=userid)
            # diaries = Diary.objects.all()
            serializer = DiarySerializer(diaries, many=True)
            return Response({'count':Diary.objects.all().count(),'data':serializer.data},status=status.HTTP_200_OK)
        else : 
            uid = kwargs.get('uid')
            diaries = Diary.objects.get(id=uid)
            serializer = DiarySerializer(diaries)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DiarySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result':'success','data':serializer.data},status=status.HTTP_200_OK)
        else : 
            return Response({'result':'fail','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, **kwargs):
        if kwargs.get('uid') is None:
            return Response("uid is required",status=status.HTTP_400_BAD_REQUEST)
        else:
            uid = kwargs.get('uid')
            diary_object = Diary.objects.get(id=uid)
            serializer = DiarySerializer(diary_object,data = request.data)
            # Key - Value 유효한지의 유무 체크 
            if serializer.is_valid():
                serializer.save()
                return Response({'result':'success','data':serializer.data},status=status.HTTP_200_OK)
            else :
                return Response("uid is required", status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, **kwargs):
        if kwargs.get('uid') is None:
            return Response("uid is required.", status=status.HTTP_400_BAD_REQUEST)
        else : 
            uid = kwargs.get('uid')
            diary_object = Diary.objects.get(id=uid)
            diary_object.delete()
            return Response({"Data is deleted!"},status=status.HTTP_200_OK)

class FavoriteViewDate(APIView):
    def get(self, request):
        uid = request.GET['user_id']
        pick_date1 = request.GET['pick_date']
        favorite = Favorite.objects.filter(pick_date=pick_date1, user_id=uid)
        serializer = FavoriteSerializer(favorite, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DiaryViewDate(APIView):
    def get(self, request):
        uid = request.GET['user_id']
        write_date1 = request.GET['writing_date']
        diary = Diary.objects.filter(writing_date=write_date1, user_id=uid)
        serializer = DiarySerializer(diary, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    