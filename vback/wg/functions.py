from users.models import PUser
import subprocess
import os


def create_wg_config(user_id):
    # Функция для генерации пары ключе

    user = PUser.objects.all().filter(id=user_id)[0]
    name = f's1_{user.username[:5]}_{user.tel[-4:]}'
    os.system(f'echo {name}')
    return name+'.conf'


def delete_wg_config(user_id):
    # Функция для генерации пары ключе

    user = PUser.objects.all().filter(id=user_id)[0]
    name = f's1_{user.username[:5]}_{user.tel[-4:]}'
    os.system(f'echo {name}_____DELETE___')
    return name+'.conf'


if __name__ == '__main__':
    create_wg_config('fsdsds')
