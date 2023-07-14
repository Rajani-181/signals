from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("----------")
    print("Log in signal Run ")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)

# manual connect Route
#user_logged_in.connect(login_success, sender=User)

@receiver(user_logged_out,sender=User)
def logout_success(sender, request, user, **kwargs):
    print("----------")
    print("Log out signal Running ")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print("logged out successfully")

# user_logged_out.connect(logout_success, sender=User)

@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print("----------")
    print("Login failed Running ")
    print("sender:", sender)
    print("request:", request)
    print("credentials:", credentials)


