from django.urls import path
from . import views

app_name = 'logvie_app'

urlpatterns = [
    path('favorites_date', views.FavoriteViewDate.as_view()),
   
    path('favorites/', views.FavoriteView.as_view()),
    path('favorites/<int:uid>',views.FavoriteView.as_view()),
    
    path('diaries_date', views.DiaryViewDate.as_view()),

    path('diaries/',views.DiaryView.as_view()),
    path('diaries/<int:uid>',views.DiaryView.as_view()) 
]

