from django.urls import path
from .views import BlogHome, PostDetailView  # <--- Ajoute PostDetailView ici

app_name = "blog"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    # Ajoute cette ligne pour gérer les détails des articles par slug
    path('post/<slug:slug>/', PostDetailView.as_view(), name="post_detail"),
]