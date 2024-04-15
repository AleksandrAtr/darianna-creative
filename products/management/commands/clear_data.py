from django.core.management.base import BaseCommand
from products.models import Product, Category


# Define a custom management command to clear all items from specified models
class Command(BaseCommand):
    help = 'Clears all items from a specified model'
    """
    A management command to clear all items from specified models.
    """

    def handle(self, *args, **options):
        """
        Execute the command to clear all items from specified models.

        Args:
            *args: Variable-length argument list.
            **options: Arbitrary keyword arguments.

        Returns:
            None
        """

        # Clear all items from the Category and Product models
        Category.objects.all().delete()

        Product.objects.all().delete()

        # Output success message
        self.stdout.write(self.style.SUCCESS('Successfully cleared all items'))
