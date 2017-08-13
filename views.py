# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.


from django.views.generic.edit import FormView

# спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm
# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login

# Выход
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

# Редирект
from django.shortcuts import redirect

#Поддержка CSRF для AJAX POST
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
#Для отключения проверки CSRF
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

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
#@csrf_exempt
def search(request):
	if request.method == "GET":
		src_ask = request.GET['q']
		# Запрос в БД с поиском src_ask
		# __icontains - регистронезависимоя проверка на вхождение: https://djbook.ru/rel1.9/ref/models/querysets.html#std:fieldlookup-icontains 
		get_nodes = Nodes.objects.all().filter(hostname__icontains=""+src_ask+"")
		#result = get_nodes.ip
		return HttpResponse(get_nodes, content_type="text/html")
		#return render(request, 'inventory/inventory.html', {'result': result})
	#if request.method == "GET":
		#search_request = request.POST['search_request']
		#two = request.GET['sity']
		#result = [one, two]
		#Запрос в БД по текущему реквесту
		#result = "hi"
        # то, что прийдет в result  - отправим в БД
	        #return HttpResponse(result, content_type="text/html")
	        #return render_to_response("inventory/inventory.html", request)


			
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
