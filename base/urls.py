from django.urls import path
from . import views


urlpatterns = [
    path("home", views.home, name="home"),
    path("", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("store", views.store, name="store"),
    path("product", views.product, name="product"),
    path("checkout", views.checkout, name="checkout"),
    path('logout/', views.logout, name='logout'),
]