from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        Method called when the application is loaded.

        Imports signals module to ensure signal handlers are registered.
        """
        import checkout.signals