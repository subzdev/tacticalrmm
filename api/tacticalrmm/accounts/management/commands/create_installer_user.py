import uuid

from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = "Creates the installer user"

    def handle(self, *args, **kwargs):
        self.stdout.write("Checking is installer user has been created...")
        if User.objects.filter(is_installer_user=True).exists():
            self.stdout.write("Installer user already exists")
            return

        User.objects.create_user(  # type: ignore
            username=uuid.uuid4().hex,
            is_installer_user=True,
            password=User.objects.make_random_password(60),  # type: ignore
            block_dashboard_login=True,
        )
        self.stdout.write("Installer user has been created")
