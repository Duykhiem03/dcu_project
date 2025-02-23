from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('history', views.history, name='history'),
    path('order', views.order, name='order'),
    path('checkout/<int:order_id>', views.checkout, name='checkout'),
    path('summary/<int:order_id>', views.order_summary, name='summary'),
]