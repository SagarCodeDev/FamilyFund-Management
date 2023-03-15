from django.apps import AppConfig
from .signals import account_created, month_changed
from .reciever import connect_users, update_account


class AssignmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assignment'

    def ready(self):
        from assignment import signals
        #Linked both of the signals to the recievers
        account_created.connect(connect_users)
        month_changed.connect(update_account)
