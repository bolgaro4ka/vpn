from users.models import PUser
from django.utils import timezone
import time
import threading


def null_if_expired_pay():
    print('[INFO] start null_if_expired_pay')
    i = 0
    while True:
        i += 1
        for user in PUser.objects.all():
            try:
                if user.paid and user.paid_date and user.paid_date + timezone.timedelta(minutes=1) < timezone.now():
                    user.paid = False
                    user.save()

            except Exception as e:
                print(e)

        time.sleep(20)


def run_in_new_null_if_expired_pay():
    thread = threading.Thread(target=null_if_expired_pay)
    thread.daemon = True  # Set the thread as a daemon thread
    thread.start()
