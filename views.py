# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
# Для постраничного пролистывания
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views.generic.edit import FormView

# спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login

# Выход
from django.contrib.auth import logout

#
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic.base import View



# Редирект
from django.shortcuts import redirect


#Попытка реализации полнотекстового поиска: http://proft.me/2011/01/22/polnotekstovyj-poisk-v-django/
from django.db.models import Q

# Декоратор для проверки авторизации пользователя
# Перед методом, необходимо указать @login_required, url для перенаправления LOGIN_URL
from django.contrib.auth.decorators import login_required


# Импортируем модель
from inventory.models import Nodes



# AJAX для inventory
#def search(request):
#	if request.method == "GET":
#		srch_ask = request.GET['q']
		# Запрос в БД с поиском src_ask
		# __icontains - регистронезависимоя проверка на вхождение: https://djbook.ru/rel1.9/ref/models/querysets.html#std:fieldlookup-icontains 
#		result = Nodes.objects.all().filter(Q(hostname__icontains=""+srch_ask+"") | Q(ip__icontains=""+srch_ask+"") | Q(region__icontains=""+srch_ask+"") | Q(sity__icontains=""+srch_ask+"") | Q(description__icontains=""+srch_ask+""))
		#return HttpResponse(get_nodes, content_type="text/html")
#		return render(request, 'inventory/search_result.html', {'result': result})
		#result = [one, two]


# Тупо рендерим вьюху
@login_required
def search_index(request):
	data = {
			'request': 'hello',
		}
	return render(request, 'inventory/search_index.html', data )

@login_required
def search_list(request):
	if request.method == "GET":
		srch_ask = request.GET['request']
		# __icontains - регистронезависимоя проверка на вхождение: https://djbook.ru/rel1.9/ref/models/querysets.html#std:fieldlookup-icontains 
		result = Nodes.objects.all().filter(Q(hostname__icontains=""+srch_ask+"") | Q(ip__icontains=""+srch_ask+"") | Q(regione=srch_ask) | Q(sity=srch_ask) | Q(description__icontains=""+srch_ask+""))
		# Т.к. regione and sity теперь не CharField/TextField а ForeignKey к ним нельзя применять медод __icontains. Найти решение.
		data = {
			'result': result,
			'request': srch_ask,
		}
		return render(request, 'inventory/search_list.html', data)
	
# Представление карточки устройства 
# Предосмотреть права доступа к редактированию
@login_required
def node(request, host, edit=None):
	host_data =  Nodes.objects.get(hostname = host) # Получаем из БД всю инфу о ноде
	# neighbors_data = Neighbors.objects.get(hostname = host) # Получаем из БД всю инфу о соседях ноды
	data = {
			'host': host_data,
			#'neighbors': neighbors_data,
		}
	if edit==None:
		return render(request, 'inventory/node.html', data)
	else:
		return render(request, 'inventory/edit_node.html', data)
		
		
		
# Добавляем новую ноду
@login_required
def new_node(request):
	data = {
			'description': "Добавление нового устрйства",
		}
	return render(request, 'inventory/new_node.html', data)

@login_required	
def new_site(request):
	data = {
			'description': "Добавление новой площадки",
		}
	return render(request, 'inventory/new_site.html', data)

@login_required
def new_link(request):
	data = {
			'description': "Добавление нового канала",
		}
	return render(request, 'inventory/new_link.html', data)
	
	

		
		
		
		
		
		
		
		

# Авторизация
class LoginFormView(FormView):
	form_class = AuthenticationForm
	# Аналогично регистрации, только используем шаблон аутентификации.
	template_name = "inventory/login.html"
	# В случае успеха перенаправим на страницу управления.
	success_url = "/"

	def form_valid(self, form):
		# Получаем объект пользователя на основе введённых в форму данных.
		self.user = form.get_user()
		# Выполняем аутентификацию пользователя.
		login(self.request, self.user)
		return super(LoginFormView, self).form_valid(form)

# Выход пользователя
class LogoutView(View):
	def get(self, request):
		# Выполняем выход для пользователя, запросившего данное представление.
		logout(request)
		# После чего, перенаправляем пользователя на главную страницу.
		return HttpResponseRedirect("/login/")
