from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Artist, UserMeta
from django.contrib.auth.models import User

# Configuration de l'interface d'administration
admin.site.index_title = "Projet Réservations"
admin.site.site_header = "Projet Réservations HEADER"
admin.site.site_title = "Spectacles"

# Enregistrement du modèle Artist
admin.site.register(Artist)


# Création de l'inline pour le profil utilisateur
class UserMetaInline(admin.StackedInline):
    model = UserMeta
    can_delete = False
    verbose_name_plural = "Détails utilisateur"  # Plus lisible dans l'interface d'administration


# Extension de UserAdmin pour inclure l'inline UserMeta
class CustomUserAdmin(BaseUserAdmin):
    inlines = [UserMetaInline]


# Enregistrement du modèle User avec la classe CustomUserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
