#!/bin/bash

# Скрипт для добавления нового клиента в WireGuard
# Использование: ./wireguard-newuser.sh client_name

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

# Функция поиска свободного IP-адреса
function find_free_ip() {
    for DOT_IP in {2..254}; do
        DOT_EXISTS=$(grep -c "${SERVER_WG_IPV4::-1}${DOT_IP}" "/etc/wireguard/${SERVER_WG_NIC}.conf")
        if [[ ${DOT_EXISTS} == '0' ]]; then
            echo "${DOT_IP}"
            return
        fi
    done

    echo "Ошибка: не найден свободный IP-адрес."
    exit 1
}

# Проверка, не существует ли клиент с таким именем
CLIENT_EXISTS=$(grep -c -E "^### Client ${CLIENT_NAME}\$" "/etc/wireguard/${SERVER_WG_NIC}.conf")
if [[ ${CLIENT_EXISTS} != 0 ]]; then
    echo "Клиент с именем ${CLIENT_NAME} уже существует. Выберите другое имя."
    exit 1
fi

# Поиск свободного IP-адреса
DOT_IP=$(find_free_ip)
BASE_IP=$(echo "$SERVER_WG_IPV4" | awk -F '.' '{ print $1"."$2"."$3 }')
CLIENT_WG_IPV4="${BASE_IP}.${DOT_IP}"

BASE_IP6=$(echo "$SERVER_WG_IPV6" | awk -F '::' '{ print $1 }')
CLIENT_WG_IPV6="${BASE_IP6}::${DOT_IP}"

# Генерация ключей для клиента
CLIENT_PRIV_KEY=$(wg genkey)
CLIENT_PUB_KEY=$(echo "${CLIENT_PRIV_KEY}" | wg pubkey)
CLIENT_PRE_SHARED_KEY=$(wg genpsk)

# Получаем путь к директории скрипта
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# Создание конфигурационного файла клиента с именем пользователя
echo "[Interface]
PrivateKey = ${CLIENT_PRIV_KEY}
Address = ${CLIENT_WG_IPV4}/32,${CLIENT_WG_IPV6}/128
DNS = ${CLIENT_DNS_1},${CLIENT_DNS_2}

[Peer]
PublicKey = ${SERVER_PUB_KEY}
PresharedKey = ${CLIENT_PRE_SHARED_KEY}
Endpoint = ${SERVER_PUB_IP}:${SERVER_PORT}
AllowedIPs = ${ALLOWED_IPS}" >"${SCRIPT_DIR}/${CLIENT_NAME}.conf"

# Добавление клиента в конфигурацию сервера
echo -e "\n### Client ${CLIENT_NAME}
[Peer]
PublicKey = ${CLIENT_PUB_KEY}
PresharedKey = ${CLIENT_PRE_SHARED_KEY}
AllowedIPs = ${CLIENT_WG_IPV4}/32,${CLIENT_WG_IPV6}/128" >>"/etc/wireguard/${SERVER_WG_NIC}.conf"

# Применение новой конфигурации
wg syncconf "${SERVER_WG_NIC}" <(wg-quick strip "${SERVER_WG_NIC}")

# Генерация QR-кода конфигурации клиента (если установлено qrencode)
if command -v qrencode &>/dev/null; then
    qrencode -t ansiutf8 -l L <"${SCRIPT_DIR}/${CLIENT_NAME}.conf"
    echo ""
fi

# Вывод пути к конфигурационному файлу клиента
echo "Конфигурационный файл клиента находится по пути: ${SCRIPT_DIR}/${CLIENT_NAME}.conf"