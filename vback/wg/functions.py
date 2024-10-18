from users.models import PUser
import subprocess
import os
from django.utils import timezone


def create_wg_config(user_id, iteration):
    # Функция для генерации пары ключе

    user = PUser.objects.all().filter(id=user_id)[0]
    name = f's1_{iteration}_{user.username[:5]}_{timezone.now().strftime("%H%M%S")}'
    os.system(f'bash ./media/vpns/wireguard-newuser.sh {name}')
    print('[INFO] create_wg_config')
    return name+'.conf'


def delete_wg_config(user_id, iteration):
    # Функция для генерации пары ключе

    user = PUser.objects.all().filter(id=user_id)[0]
    name = f's1_{iteration}_{user.username[:5]}_{timezone.now().strftime("%H%M%S")}'
    os.system(f'bash ./media/vpns/wireguard-deluser.sh {name}')
    print('[INFO] delete_wg_config')
    return name+'.conf'


if __name__ == '__main__':
    create_wg_config('fsdsds')
