# Ensure unique index on email for users collection in MongoDB
# This script can be run in mongosh or as a Django management command, but per instructions, we should use Django ORM for structure and data.
# However, Djongo does not natively support unique indexes on non-primary fields via ORM, so we use pymongo for index creation in a Django management command.

from django.core.management.base import BaseCommand
from djongo import connection

class Command(BaseCommand):
    help = 'Ensure unique index on email field in users collection.'

    def handle(self, *args, **options):
        db = connection.cursor().db_conn
        users_collection = db['octofit_tracker_user']
        result = users_collection.create_index(
            [('email', 1)],
            unique=True,
            name='unique_email_idx'
        )
        self.stdout.write(self.style.SUCCESS(f'Created unique index: {result}'))
