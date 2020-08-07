from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password= models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)
    payment = models.IntegerField(default=0)  # 工资
    city = models.CharField(max_length=20)

    class Meta:
        db_table = 'homework_user'


class User1(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'homework_user1'


class Stud(models.Model):
    name = models.CharField(max_length=10)
    class Meta:
        db_table = 'homework_stud'



class Like(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    sid = models.ForeignKey(Stud,on_delete=models.CASCADE,related_name='stud')
    class Meta:
        db_table = 'homework_like'



class CommentSheet(models.Model):
    comment = models.TextField()
    kc = models.ForeignKey(Stud,on_delete=models.CASCADE)
    class Meta:
        db_table = 'homework_comment'

