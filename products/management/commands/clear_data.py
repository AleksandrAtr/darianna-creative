from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Clears all items from a specified model'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared all items'))
