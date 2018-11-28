from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "insights_ansible_runner_poc.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
