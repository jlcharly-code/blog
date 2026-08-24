from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    text = models.TextField(blank=True, verbose_name="Contenu")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
		   if not self.slug:
                    self.slug = slugify(self.title)

                    super().save(*args, **kwargs)

