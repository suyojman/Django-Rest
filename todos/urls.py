from django.urls import path
from . import views

urlpatterns = [

	path('', views.TodoListView.as_view(), name='list_todo'),
	path('<int:pk>/', views.TodoDetailView.as_view(), name='detail_todo'),

]