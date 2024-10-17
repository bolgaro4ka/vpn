#!/bin/bash

# Скрипт для удаления клиента из WireGuard
# Использование: ./wireguard-removeuser.sh client_name

# Проверка наличия имени пользователя
if [ -z "$1" ]; then
    echo "Ошибка: укажите имя клиента."
    exit 1
fi

CLIENT_NAME=$1

# Проверка, установлен ли WireGuard и загружены ли параметры
if [[ ! -e /etc/wireguard/params ]]; then
    echo "Ошибка: не найдена конфигурация WireGuard. Убедитесь, что WireGuard установлен и настроен."
    exit 1
fi

# Загрузка параметров WireGuard
source /etc/wireguard/params

# Проверка, существует ли клиент с указанным именем
CLIENT_EXISTS=$(grep -c -E "^### Client ${CLIENT_NAME}\$" "/etc/wireguard/${SERVER_WG_NIC}.conf")
if [[ ${CLIENT_EXISTS} == 0 ]]; then
    echo "Клиент с именем ${CLIENT_NAME} не найден."
    exit 1
fi

# Удаление блока клиента из конфигурации сервера
sed -i "/^### Client ${CLIENT_NAME}\$/,/^$/d" "/etc/wireguard/${SERVER_WG_NIC}.conf"

# Получаем путь к директории скрипта
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# Удаление конфигурационного файла клиента с именем пользователя
rm -f "${SCRIPT_DIR}/${CLIENT_NAME}.conf"

# Применение изменений
wg syncconf "${SERVER_WG_NIC}" <(wg-quick strip "${SERVER_WG_NIC}")

echo "Клиент ${CLIENT_NAME} успешно удалён."