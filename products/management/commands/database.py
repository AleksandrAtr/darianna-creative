from django.db import connection
from django.core.management.base import BaseCommand


# Define a custom management command to drop a table from the database
class Command(BaseCommand):
    help = 'Backup SQLite database'
    """
    A management command to drop a table from the database.
    """

    def handle(self, *args, **options):
        """
        Execute the command to drop a table from the database.

        Args:
            *args: Variable-length argument list.
            **options: Arbitrary keyword arguments.

        Returns:
            None
        """

        table_name = 'Category'

        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS %s;" % table_name)
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=%s;"
                , [table_name])
            if cursor.fetchone() is None:
                self.stdout.write(
                    self.style.SUCCESS(f"Table '{table_name}' 
                                       dropped successfully."))
            else:
                self.stdout.write(self.style.ERROR(
                    f"Failed to drop table '{table_name}'."))
