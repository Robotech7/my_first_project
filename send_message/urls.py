from django.urls import path

from .views import SendMessageView

app_name = 'send_message'
urlpatterns = [
    path('', SendMessageView.as_view(), name='msg'),
]
