from django.db import models
from django.db.models.fields import CharField

# Create your models here.

# class Login(models.Model):
#     user_id  = models.UUIDField(primary_key=True)
#     user_nickName = models.CharField(max_length=128,null=False)
    
#     class Meta:
#         db_table = "logins"

class Favorite(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    movie_id = models.IntegerField(null=False)
    user_id = models.CharField(max_length=128,null=False)
    pick_date = models.DateField(null=False,auto_now_add=True)
    # movie_id1 = models.IntegerField(null=False)
    class Meta:
        db_table = "favorites"
        ordering = ['-id']
class Diary(models.Model):
    
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=128,null=False)
    writing_date = models.CharField(max_length=128,null=False)
    movie_title = models.CharField(max_length=128,null=False)
    diary_text = models.TextField(null=False)
    photo = models.CharField(max_length=128, null=False)
    mood = models.IntegerField(null=False)
    # movie_id1 = models.IntegerField(null=False)
    
    class Meta:
        db_table = "diaries"
        ordering = ['-id']