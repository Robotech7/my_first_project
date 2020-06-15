from django.urls import path

from .views import Login, SignUp, Logout, ProfileView

app_name = 'login_register'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('SignUp/', SignUp.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile')
]
