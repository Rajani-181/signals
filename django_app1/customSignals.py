from django.dispatch import receiver, Signal

# Custom signals
# 1. we have create signals
# 2. we have to send signal manually
# 3. we have to create receiver function for receiving function

# creating signal
notification = Signal(['request', 'user'])


#receiver function
@receiver(notification)
def show_notification(sender, **kwargs):
    print("sender: ", sender)
    print(f'kwargs: {kwargs}')
    print("notification: ", notification)




