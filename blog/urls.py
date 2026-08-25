from django.urls import path
from .views import BlogHome

app_name = "blog"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
]