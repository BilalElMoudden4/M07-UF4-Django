from django.apps import AppConfig

class CrudConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crud'

    # Importa las clases necesarias desde models.py
    def ready(self):
        from .models import Usuari, Rol, db
