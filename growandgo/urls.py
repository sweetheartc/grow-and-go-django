
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('menu/', views.menu_view, name='menu'),
    path('market/', views.market_view, name='market'),
    path('farmers/', views.farmers_view, name='farmers'),
    path('farmers/nueva-ecija/', views.nueva_ecija_view, name='nueva-ecija'),
    path('farmers/negros-occidental/', views.negros_occidental_view, name='negros-occidental'),
    path('profile/', views.profile_view, name='profile'),
]
