from django.urls import path
from . import views


urlpatterns = [
    path('', views.faq_list, name='faq_list'),    
    path('add/', views.add_faq, name='add_faq'),
]