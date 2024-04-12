from django.urls import path
from api import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
	path('register', views.UserRegister.as_view(), name='register'),
	path('user', views.UserView.as_view(), name='user'),
    path('worker', views.WorkerListView.as_view(), name='worker'),
    path('worker/<int:pk>', views.WorkerView.as_view(), name='worker'),
    path('work/', views.WorkListView.as_view(), name='work_list'),  
    path('work/<int:pk>/', views.WorkView.as_view(), name='work_detail'), 
    path('add_worker', views.AddWorker.as_view(), name='add_worker'),
    path('update_worker/<int:pk>', views.UpdateWorker.as_view(), name='update_worker'),
    path('delete_worker/<int:pk>', views.DeleteWorker.as_view(), name='delete_worker'),
]