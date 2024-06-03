from django.urls import path
from authuser import views
from django.http import HttpResponseRedirect

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    path('app/', views.authuser, name='home'),
    

    #path('register/', views.register, name='register'),
    path('', lambda request: HttpResponseRedirect('/app/')),  # Redirect root to /app/
]
