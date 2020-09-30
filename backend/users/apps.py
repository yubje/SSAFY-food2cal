from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

class ProfileConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import users.signals