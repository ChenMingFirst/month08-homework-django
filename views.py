from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .sers import *
from django.core.paginator import Paginator
from .filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.

#
class UserView(APIView):
    def post(self, request):
        user_ser = Userser(data=request.data)
        print(user_ser)
        if user_ser.is_valid():
            user_ser.save()
            return Response({'message': '登录成功', 'code': 200})
        else:
            return Response({'message': '登录失败', 'code': 400})
    def get(self,request):
        user_list = User.objects.all()
        user_ser = Userser(user_list,many=True)
        return Response(user_ser.data)



class ChaView(APIView):
    def post(self,request):
        gt = request.data.get('gt')
        lt = request.data.get('lt')
        page = request.data.get('p')
        print(page)
        if all([gt,lt]):

            user_lsit = User.objects.filter(payment__gte=gt).filter(payment__lte = lt)
        elif gt:

            user_lsit = User.objects.filter(payment__gte=gt)
        elif lt:

            user_lsit = User.objects.filter(payment__lte = lt)
        else:
            user_lsit = User.objects.all()
        # user_ser = UserSerializers(user_lsit,many=True)
        # return Response({'data':user_ser.data})
        pageinfo = Paginator(user_lsit, 2)
        book_info = pageinfo.page(int(page))
        book_list = [i for i in pageinfo.page_range]
        ser_foods = Userser(book_info, many=True)
        res_data = {
            'all_page': pageinfo.num_pages,
            'data': ser_foods.data,
            'page': book_info.number,
            'page_list': book_list
        }
        return Response(status=200, data=res_data)



# 调用过滤器django-filters
class UserViewSet(ModelViewSet):
        queryset = User.objects.all()
        serializer_class = Userser
        filter_backends = (DjangoFilterBackend,)
        # filter_fields = ('payment')
        filter_class = UserFilter


# 展示课程，点击关注
class ShowKc(APIView):
    def get(self,request):
        lists = Stud.objects.all()
        list = Studser(lists,many=True)
        comment = CommentSheet.objects.all()
        comments = Commentser(comment,many=True)
        print(comments)
        return Response({'list':list.data,'comment':comments.data})

    def post(self,request):
        name = request.data.get('username')
        kid = request.data.get('kid')
        uid = User1.objects.filter(name=name).first()
        likes = Like.objects.filter(sid_id=kid,uid_id=uid.id)
        if not likes:
            Like.objects.create(sid_id=kid,uid_id=uid.id)
            return Response({'message': '关注成功', 'code': 200})
        return Response({'message': '关注失败', 'code':201})
        # else:
        # return Response({'message': '您已关注', 'code': 403})
#


# 对主评论
class Comment(APIView):
    def post(self,request):
        comment = request.data.get('comments')
        s_id = request.data.get('sid')
        sid = Stud.objects.filter(pk=s_id).first()
        print(s_id)
        print(comment)
        # print(sid.id)
        CommentSheet.objects.create(comment=comment,kc_id=sid.id)
        return Response({'msg':'发表成功'})