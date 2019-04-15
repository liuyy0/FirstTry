"""books_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 出版社
    url(r'^publisher/', views.show_publisher),
    url(r'^add_publisher/', views.add_publisher),
    url(r'^del_publisher/', views.del_publisher),
    url(r'^edit_publisher/', views.edit_publisher),
    # 图书
    url(r'^show_books/', views.show_books),
    url(r'^add_books/', views.add_books),
    url(r'^del_books/', views.del_books),
    url(r'^edit_books/', views.edit_books),
    # 作者
    url(r'^show_authors/', views.show_authors),
    url(r'^add_authors/', views.add_authors),
    url(r'^del_authors/', views.del_authors),
    url(r'^edit_authors/', views.edit_authors),

]
