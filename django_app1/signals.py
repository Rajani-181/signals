from django.contrib.auth.signals import user_logged_in, user_logged_out, \
    user_login_failed
from django.contrib.auth.models import User
from django.core.signals import request_started, request_finished, \
    got_request_exception
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_init, post_init, \
    pre_delete, post_delete, pre_migrate, post_migrate
from django.db.backends.signals import connection_created
from django_app1.models import Post


# Login and Logout signals
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("----------")
    print("Log in signal Run ")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)


# manual connect Route
# user_logged_in.connect(login_success, sender=User)

@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    print("----------")
    print("Log out signal Running ")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print("logged out successfully")


# user_logged_out.connect(logout_success, sender=User)

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("----------")
    print("Login failed Running ")
    print("sender:", sender)
    print("request:", request)
    print("credentials:", credentials)


# Model signals
# 1. pre_init(sender,args,**kwargs)
# 2. post_init(sender,instance)
# 3. pre_save(sender,instance,raw,using,update_fields)
# 4. post_save(sender,instance,created,raw,using,update_fields)
# 5. pre_delete(sender,instance,using)
# 6. post_delete(sender,instance,using)

@receiver(pre_save, sender=Post)
def at_beginning_save(sender, instance, **kwargs):
    print("----------")
    print("pre save Running ")
    print("sender:", sender)
    print("request:", instance)
    print(f'kwargs: {kwargs}')


@receiver(post_save, sender=Post)
def at_ending_save(sender, instance, **kwargs):
    print("----------")
    print("post save Running ")
    print("sender:", sender)
    print("request:", instance)
    print(f'kwargs: {kwargs}')


@receiver(pre_delete, sender=Post)
def at_ending_save(sender, instance, **kwargs):
    print("----------")
    print("pre delete Running ")
    print("sender:", sender)
    print("request:", instance)
    print(f'kwargs: {kwargs}')


@receiver(post_delete, sender=Post)
def at_ending_save(sender, instance, **kwargs):
    print("----------")
    print("post delete Running ")
    print("sender:", sender)
    print("request:", instance)
    print(f'kwargs: {kwargs}')


@receiver(pre_init, sender=Post)
def at_ending_save(sender, *args, **kwargs):
    print("----------")
    print("pre init Running ")
    print("sender:", sender)
    print("request:", args)
    print(f'kwargs: {kwargs}')


@receiver(post_init, sender=Post)
def at_ending_save(sender, *args, **kwargs):
    print("----------")
    print("post init Running ")
    print("sender:", sender)
    print("request:", args)
    print(f'kwargs: {kwargs}')


# Request signals
# 1. request_started(sender,environ)
# 2. request_finished(sender)
# 3. got_request_expection(sender,request,**kwargs)

@receiver(request_started)
def request_start(sender, environ, **kwargs):
    print("----------")
    print("request started")
    print("sender:", sender)
    print("request:", environ)
    print(f'kwargs {kwargs}')


@receiver(request_finished)
def request_end(sender, **kwargs):
    print("----------")
    print("request ending")
    print("sender:", sender)
    print(f'kwargs {kwargs}')


@receiver(got_request_exception)
def at_ending_save(sender, request, **kwargs):
    print("----------")
    print("request exception")
    print("sender:", sender)
    print("request:", request)
    print(f'kwargs {kwargs}')


# Management signals
# 1. pre_migrate(sender,app_config,verbosity,interactive,using,plan,apps)
# 2. post_migrate(sender,app_config,verbosity,interactive,using,plan,apps)

@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan,
                       apps, **kwargs):
    print("---------------------")
    print("pre migrate running")
    print("sender:", sender)
    print("app_config:", app_config)
    print("verbosity:", verbosity)
    print("interactive:", interactive)
    print("using:", using)
    print("plan:", plan)
    print("apps:", apps)


@receiver(post_migrate)
def after_install_app(sender, app_config, verbosity, interactive, using, plan,
                      apps, **kwargs):
    print("---------------------")
    print("post migrate running")
    print("sender:", sender)
    print("app_config:", app_config)
    print("verbosity:", verbosity)
    print("interactive:", interactive)
    print("using:", using)
    print("plan:", plan)
    print("apps:", apps)


# Database wrapper signals
# django.db.backends.signals
# 1. connection_created(sender,connection, **kwargs)

@receiver(connection_created)
def at_ending_save(sender, connection, **kwargs):
    print("----------")
    print("database connection running")
    print("sender:", sender)
    print("connection:", connection)
    print(f'kwargs {kwargs}')
