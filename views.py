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
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

# Редирект
from django.shortcuts import redirect

#Поддержка CSRF для AJAX POST
#from django.shortcuts import render_to_response
#from django.template.context_processors import csrf
#Для отключения проверки CSRF
#from django.views.decorators.csrf import csrf_exempt

#from django.utils.decorators import method_decorator

#Попытка реализации полнотекстового поиска: http://proft.me/2011/01/22/polnotekstovyj-poisk-v-django/
from django.db.models import Q

# Импортируем модель
from inventory.models import Nodes

# Depricated
# Возвращаем основной дашборд инвентори
def dashboard(request):
	if not request.user.is_authenticated():
		return redirect('/login/')
	else:
		context = {
			'value': "Саммори по сети",
			'node': 'кол-во устройств',
			'port': 'кол-во свободных портов'
		}
		return render(request, 'inventory/dashboard.html', context)

# Модуль поиска по БД
def inventory(request):
	if not request.user.is_authenticated():
		return redirect('/login/')
	else:
		context = {
			'value': "Тут будет поиск по БД",
		}
		return render(request, 'inventory/inventory.html', context)

# AJAX для inventory
def search(request):
	if request.method == "GET":
		srch_ask = request.GET['q']
		# Запрос в БД с поиском src_ask
		# __icontains - регистронезависимоя проверка на вхождение: https://djbook.ru/rel1.9/ref/models/querysets.html#std:fieldlookup-icontains 
		result = Nodes.objects.all().filter(Q(hostname__icontains=""+srch_ask+"") | Q(ip__icontains=""+srch_ask+"") | Q(region__icontains=""+srch_ask+"") | Q(sity__icontains=""+srch_ask+"") | Q(description__icontains=""+srch_ask+""))
		#return HttpResponse(get_nodes, content_type="text/html")
		return render(request, 'inventory/search_result.html', {'result': result})
		#result = [one, two]


			
def hello(request):
	if not request.user.is_authenticated():
		return redirect('/login/')
	else:
		return redirect('/dashboard/')




# Авторизация
class LoginFormView(FormView):
	form_class = AuthenticationForm
	# Аналогично регистрации, только используем шаблон аутентификации.
	template_name = "inventory/login.html"
	# В случае успеха перенаправим на страницу управления.
	success_url = "/dashboard/"

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


	
		
# Добавляем новую ноду
def new_node(request):
	data = {
			'description': "Добавление нового устрйства",
		}
	return render(request, 'inventory/new_node.html', data)

	
def new_site(request):
	data = {
			'description': "Добавление новой площадки",
		}
	return render(request, 'inventory/new_site.html', data)

def new_link(request):
	data = {
			'description': "Добавление нового канала",
		}
	return render(request, 'inventory/new_link.html', data)
	
# В даный момент эта вьюха доступна без авторизации...	
# Так же надо предусмотреть права доступа на редактирование
def node(request, node, host, edit=None):
	host_data = result = Nodes.objects.get(hostname = host) # Получаем из БД всю инфу о ноде
	# neighbors_data = Neighbors.objects.get(hostname = host) # Получаем из БД всю инфу о соседях ноды
	data = {
			'host': host_data,
			#'neighbors': neighbors_data,
		}
	if edit==None:
		return render(request, 'inventory/node.html', data)
	else:
		return render(request, 'inventory/edit_node.html', data)
