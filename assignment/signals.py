import django.dispatch
#two signals that we will require
account_created = django.dispatch.Signal("users")
month_changed = django.dispatch.Signal()
