from django.urls import path
from app import views

urlpatterns = [
    path('list-article/', views.ArticleList.as_view()),
    path('list-article/<int:pk>', views.ArticleDetail.as_view()),

    path('list-author/', views.AuthorList.as_view()),
    path('list-author/<int:pk>', views.AuthorDetail.as_view()),
]