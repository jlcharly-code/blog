from django.views.generic import ListView, DetailView
from .models import BlogPost

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)

class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'  # Le nom du fichier HTML pour l'article complet
    context_object_name = 'post'
    # Django utilise automatiquement le slug ou l'ID si tu ne specifies pas de field_name
    # Comme ton URL utilise <slug:slug>, Django le détectera automatiquement.