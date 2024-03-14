from django.apps import AppConfig


class VotreApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    
    def ready(self):
        import membre.signals  # Importez le fichier contenant vos signaux

        
