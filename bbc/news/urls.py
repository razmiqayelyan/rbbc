from django.urls import path, include
from .views import *
urlpatterns = [
	path('', index, name='index'),
	path('login/', login, name='login'),
	path('logout/', logout, name='logout'),
	path('detail/<int:pk>/',NewsDetail.as_view(), name='detail'),
	path('delete/<int:pk>/', delete, name='delete')
]