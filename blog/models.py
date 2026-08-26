from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone
import unicodedata


User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(default=timezone.localdate)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # --- NETTOYAGE DU TEXTE ---
        if self.content:
            # 1. Normalisation Unicode : Décompose les caractères (ex: é -> e + accent)
            # 2. Encodage en ASCII : Supprime tout ce qui n'est pas ASCII (les accents disparaissent)
            # 3. Décodage : On recrée la chaîne de caractères
            
            # OPTION A : Garder les accents mais supprimer les caractères bizarres (guillemets Word, etc.)
            # On normalise, on garde tout, mais on supprime les caractères de contrôle
            normalized_content = unicodedata.normalize('NFKD', self.content)
            # Supprime les caractères de contrôle invisibles (sauf sauts de ligne et tabulations)
            cleaned_content = ''.join(
                c for c in normalized_content 
                if unicodedata.category(c)[0] != 'C' or c in '\n\r\t'
            )
            self.content = cleaned_content

            # OPTION B (Plus radicale) : Supprimer TOUTES les accents (é -> e)
            # Décommente les 2 lignes ci-dessous si tu veux que "café" devienne "cafe"
            # ascii_content = normalized_content.encode('ascii', 'ignore').decode('ascii')
            # self.content = ascii_content

        # Fin du nettoyage

        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)