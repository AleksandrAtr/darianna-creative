from django.db import connection
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        table_name = 'Category'
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS %s;" % table_name)
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=%s;", [table_name])
            if cursor.fetchone() is None:
                self.stdout.write(self.style.SUCCESS(f"Table '{table_name}' dropped successfully."))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to drop table '{table_name}'."))
