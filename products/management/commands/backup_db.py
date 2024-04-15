from django.core.management.base import BaseCommand
import shutil
import os


# Define a custom management command to backup the SQLite database
class Command(BaseCommand):
    help = 'Backup SQLite database'
    """
    A management command to backup the SQLite database.
    """

    def handle(self, *args, **options):
        """
        Execute the command to backup the SQLite database.

        Args:
            *args: Variable-length argument list.
            **options: Arbitrary keyword arguments.

        Returns:
            None
        """

        # Get the base directory of the project
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))))

        # Move up one level
        BASE_DIR = os.path.dirname(BASE_DIR)

        # Specify the paths for the database and backup
        database_path = os.path.join(BASE_DIR, 'db.sqlite3')
        backup_path = os.path.join(BASE_DIR, 'backup', 'db_backup.sqlite3')

        # Copy the database file to create a backup
        shutil.copyfile(database_path, backup_path)

        # Output success message
        self.stdout.write(self.style.SUCCESS(
            'Backup created successfully at {}'.format(backup_path)))
