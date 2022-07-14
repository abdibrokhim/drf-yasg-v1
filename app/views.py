from app.models import Article, Author
from app.serializers import ArticleSerializer, AuthorSerializer
from rest_framework import mixins
from rest_framework import generics

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ArticleList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    name = openapi.Parameter('name', openapi.IN_QUERY, description="ID", type=openapi.TYPE_STRING)
    description = openapi.Parameter('description', openapi.IN_QUERY, description="description".upper(), type=openapi.TYPE_STRING)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    id = openapi.Parameter('id', openapi.IN_QUERY, description="ID", type=openapi.TYPE_INTEGER)
    name = openapi.Parameter('name', openapi.IN_QUERY, description="NAME", type=openapi.TYPE_STRING)
    description = openapi.Parameter('description', openapi.IN_QUERY, description="description".upper(), type=openapi.TYPE_STRING)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # @swagger_auto_schema(request_body=ArticleSerializer)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AuthorList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    name = openapi.Parameter('name', openapi.IN_QUERY, description="NAME", type=openapi.TYPE_STRING)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(request_body=AuthorSerializer)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AuthorDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    id = openapi.Parameter('id', openapi.IN_QUERY, description="ID", type=openapi.TYPE_INTEGER)
    name = openapi.Parameter('name', openapi.IN_QUERY, description="NAME", type=openapi.TYPE_STRING)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description='UPDATE ARTICLE', request_body=AuthorSerializer)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[id],)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
