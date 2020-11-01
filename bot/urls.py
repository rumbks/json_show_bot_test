from django.urls import path

from . import views
urlpatterns = [
    path('', views.telegram_request_handler, name='telegram_request_handler'),
]