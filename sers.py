from rest_framework.serializers import ModelSerializer
from .models import *

class Userser(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class User1ser(ModelSerializer):
    class Meta:
        model = User1
        fields = "__all__"


class Studser(ModelSerializer):
    class Meta:
        model = Stud
        fields = '__all__'

class Likeser(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class Commentser(ModelSerializer):
    class Meta:
        model = CommentSheet
        fields = '__all__'

