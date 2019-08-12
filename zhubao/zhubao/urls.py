"""zhubao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from core import views
from core.api import user
router = routers.DefaultRouter()


schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    # path(r'test', user.TestView.as_view()),
    path('view/', user.view),
    path(r'test/', user.TestView.as_view()),
    path(r'test/zhu', views.index),
    url(r'^schema/$', schema_view),
    path(r'api-doc/', include_docs_urls("API文档")),
    # path(r'test/<int:pk>/', user.TestView.as_view()),
]

router.register(r'users', user.UserViewSet, basename="users")
urlpatterns += router.urls

