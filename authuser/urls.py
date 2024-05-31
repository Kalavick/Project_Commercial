from django.urls import path
from authuser import views
from django.http import HttpResponseRedirect

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.user_logout, name='logout'),  # Updated to match the view name
    path('app/', views.authuser, name='app'),
    path('', lambda request: HttpResponseRedirect('/app/')),  # Redirect root to /app/
]
