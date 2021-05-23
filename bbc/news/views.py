from django.shortcuts import render, redirect
from .models import Newspaper
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import DetailView
# Create your views here.
def index(request):
	news = Newspaper.objects.all()
	if request.method == 'POST':
		title = request.POST['Title']
		text = request.POST['Text']
		image = request.FILES.get('Image')
		if image == None:
			add_news = Newspaper.objects.create(title=title, text=text)
		else:
			add_news = Newspaper.objects.create(title=title, text=text, image=image)
		add_news.save()
	return render(request, 'index.html', {'news':news})

def login(request):
	if request.method == 'POST':
		try:
			username = request.POST['Username_up']
			password = request.POST['Password_up']
			email = request.POST['Email_up']
			if User.objects.filter(username=username).exists():
				messages.warning(request, 'Username Taken')
				return redirect('login')

			user = User.objects.create_user(username=username, email=email, password=password)
			user.save()
			messages.warning(request, 'User Created Successfully')
		except:
			username = request.POST['Username']
			password = request.POST['Password']
			user = auth.authenticate(username=username, password=password)
			if user == None:
				messages.warning(request, 'Login or Password is not Correct')
			else:
				auth.login(request, user)
				return redirect('index')

	return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('index')

class NewsDetail(DetailView):
	model = Newspaper
	template_name = 'single.html'
	context_object_name = 'new'

def delete(request, pk):
	news = Newspaper.objects.get(id=pk)
	news.delete()
	return redirect('index')
