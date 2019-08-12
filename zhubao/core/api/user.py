# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
#
# @api_view(['GET', 'POST', ])
# def index(request):
#     print('--------------------', request.query_params)
#     print('--------------------', request.data)
#     print('--------------------', request.user)
#     return Response({'data': 'zhubaoxiang', 'page': 1})

from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from django.contrib.auth.models import User, Group
from core.models import ComModel, ZhuModel, BaoModel
from core.api.serializers import ComSerializer
from django.db.models import Count
from django.views import View
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView


class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'


@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})


class CustomPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10000


class TestView(APIView):
    # queryset = ComModel.objects.all()
    # serializer_class = ComSerializer
    pagination_class = CustomPagination
    # authentication_classes = (BasicAuthentication, )
    # permission_classes = [IsAuthenticated]
    # parser_classes = (FormParser,)

    def get(self, request):
        queryset = ComModel.objects.all()
        serializer = ComSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = ComSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def put(self, request):
        data = request.data
        obj_id = data.pop('id')
        instance = ComModel.objects.get(id=obj_id)
        print("======================", instance.content)
        serializer = ComSerializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    # def get(self, request):
    #     queryset = ComModel.objects.all()
    #     print('++++++++++', queryset)
    #     print("=============", queryset[0].content)
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = ComSerializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     serializer = ComSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #     serializer = ComSerializer(data, many=True)
    #     return Response(serializer.data)
    #     if serializer.is_valid():
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)

    # def post(self, request):
    #     print("------------", request.data)
    #     return Response({"data": "zhaoerfang"})


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UserViewSet(viewsets.ModelViewSet):
    queryset = ZhuModel.objects.all()
    # queryset = Group.objects.all()
    serializer_class = ComSerializer
    pagination_class = StandardResultsSetPagination
    # lookup_field = 'id'
    # authentication_classes = [TokenAuthentication]

    @action(detail=False, methods=['get', 'put', 'post'])
    def createaa(self, request, pk=None):
        queryset = self.get_queryset().filter(name__id=8)
        print("----------------", type(queryset))
        data_list = list()
        for item in queryset:
            data = dict()
            print("----------------", type(item))
            data['name_id'] = item.name_id
            data['email'] = item.name.created
            data['address'] = item.name.bao.address
            data['content'] = item.name.content

            data_list.append(data)
        # cs = self.get_serializer(com, many=True)
        return Response(data_list)

    @action(detail=False, methods=['get', 'put', 'post'])
    def createbb(self, request, pk=None):
        queryset = BaoModel.objects.get(address='liuying')
        com_queryset = queryset.BAO.all()
        print("----------------", type(queryset))
        data_list = list()
        for item in com_queryset:
            data = dict()
            print("----------------", type(item))
            # data['name_id'] = item.BAO.ZHU.name_id
            data['email'] = item.email
            data['address'] = item.created
            data_list.append(data)
        # cs = self.get_serializer(com, many=True)
        return Response(data_list)

    @action(detail=False, methods=['get', 'put', 'post'])
    def hello(self, request):
        # queryset = ComModel.objects.values("bao_id").annotate(content_num=Count('bao_id')).values("bao_id", "content_num")
        queryset = ComModel.objects.filter(bao__age__gt=27)
        print("++++++++++", queryset)
        for item in queryset:
            print("=====", item.bao.address)
        return Response({'data': 'hello, I am hello'})

    # def list(self, request):
    #     data = {
    #         'data': 'hello, I am list',
    #         'basename': self.basename,
    #         'action': self.action,
    #         'detail': self.detail,
    #         'suffix': self.suffix,
    #         'name': self.name,
    #         'description ': self.description,
    #     }
    #     queryset = User.objects.all()
    #     print(queryset)
    #     return Response(data)

    def create(self, request):
        print("-----------", request.data)
        data = request.data
        serializer = ComSerializer(data=data)
        print(type(serializer))
        print("++++++++++", serializer)
        print("++++++++++", serializer.is_valid())
        serializer.save()

        return Response({'data': 'hello, I am create'})

    # def update(self, request):
    #     com = self.get_queryset()
    #     data = request.data
    #     serializer = self.get_serializer(com, data=data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # def get_queryset(self):
    #     content = self.request.query_params.get('content', None)
    #     print("-------------", content)
    #     if content:
    #         return ComModel.objects.filter(content=content)
    #     else:
    #         return ComModel.objects.all()
