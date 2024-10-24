from users.models import PUser
from django.utils import timezone
import time
import threading
from wg.functions import delete_wg_config, create_wg_config
from rest_framework.response import Response


def null_if_expired_pay():
    print('[INFO] start null_if_expired_pay')
    i = 0
    while True:
        i += 1
        for user in PUser.objects.all():
            try:
                if user.paid and user.paid_date and ((user.paid_date + timezone.timedelta(days=32)) < timezone.now()):
                    user.paid = False
                    for iteration in range(user.number_of_files):
                        delete_wg_config(user.id, iteration)
                    user.file_path = None
                    user.save()

                if user.auto_pay and (not user.paid):
                    tariff = user.tariff

                    if (user.wallet < tariff.ppm+((user.number_of_files-1)*100)):
                        continue

                    user.wallet -= tariff.ppm+((user.number_of_files-1)*100)
                    user.paid = True
                    user.paid_date = timezone.now()
                    user.file_path = ''

                    for iteration in range(user.number_of_files):
                        user.file_path += create_wg_config(user.id, iteration) + ';'

                    user.save()

            except Exception as e:
                print(e)

        time.sleep(5)


def run_in_new_null_if_expired_pay():
    thread = threading.Thread(target=null_if_expired_pay)
    thread.daemon = True  # Set the thread as a daemon thread
    thread.start()
