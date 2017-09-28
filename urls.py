# -*- coding: utf-8 -*-

"""net URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from inventory import views

# Must be list [], but not dict {}!
urlpatterns = [
    # url(r'inventory/', views.index)
    # url(r'', 'django.contrib.auth.views.login', {'template_name': 'inventory/login.html'}, name='login'),
    # Главная страница
    # Представление по умолчанию
    #url(r'^dashboard/$', views.dashboard, name="dashboard"),# AJAX для формы поиска
	# old # url(r'^inventory/search/$', views.search, name="search"),
	url(r'^search/$', views.search_list, name="search_list"),
	# url(r'^search$', views.search_list, name="search_list"),
	url(r'^node/(?P<host>[.\-\w]+)/$', views.node, name="node"),# Ссылка на карточку node
	url(r'^node/$', views.node, name="node"),# Ссылка на карточку node
	#url(r'^inventory/(?P<node>\w+)/(?P<host>\w+)/(?P<edit>\w+)/$', views.node, name="node"),# Ссылка на карточку node
    #url(r'^inventory/$', views.inventory, name="inventory"),# Вход и выход
	url(r'^new_node/$', views.new_node, name="new_node"), 	# Добавление новой ноды
	url(r'^new_link/$', views.new_link, name="new_link"),	# Добавление нового линка
	url(r'^new_site/$', views.new_site, name="new_site"),	# Добавление новой площадки
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'', views.search_index, name="search_index"),
]


