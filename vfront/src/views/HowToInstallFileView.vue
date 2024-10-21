<script setup lang="ts">

</script>

<template>
    <div class="hti_wrapper">
        <div class="hti">
            <h1>Инструкция по установке WireGuard</h1>

        <h2>Установка WireGuard на Windows</h2>
        <ol>
            <li>Перейдите на официальный сайт WireGuard и скачайте установочный файл для Windows по ссылке: <a href="https://www.wireguard.com/install/">WireGuard Install</a>.</li>
            <li>Запустите загруженный файл и следуйте инструкциям установщика.</li>
            <li>После завершения установки запустите приложение WireGuard.</li>
            <div class="screenshot">
                <img src="/public/tutorial/6.jpg" alt="Скриншот интерфейса программы WireGuard на Windows" />
                <p>Скриншот интерфейса программы WireGuard на Windows</p>
            </div>
            <li>Нажмите "Import tunnel(s) from file" и выберите файл конфигурации, предоставленный вам.</li>
            <div class="screenshot">
                <img src="/public/tutorial/7.png" alt="Скриншот процесса импорта конфигурации" />
                <p>Скриншот процесса импорта конфигурации</p>
            </div>
            <li>Нажмите "Activate", чтобы подключиться к VPN.</li>
            <div class="screenshot">
                <img src="/public/tutorial/8.jpg" alt="Скриншот активированного подключения" />
                <p>Скриншот активированного подключения</p>
            </div>
        </ol>

        <h2>Установка WireGuard на Android</h2>
        <ol>
            <li>Откройте Google Play Store и найдите приложение WireGuard. Нажмите "Установить".</li>
            <div class="screenshot">
                <img src="/tutorial/1.jpg" alt="Скриншот страницы приложения WireGuard в Google Play" />
                <p>Скриншот страницы приложения WireGuard в Google Play</p>
            </div>
            <li>Запустите приложение WireGuard после установки.</li>
            <div class="screenshot">
                <img src="/public/tutorial/2.png" alt="Скриншот интерфейса приложения WireGuard на Android" />
                <p>Скриншот интерфейса приложения WireGuard на Android</p>
            </div>
            <li>Нажмите на кнопку "Добавить туннель" и выберите "Импортировать из файла или архива".</li>
            <div class="screenshot">
                <img src="/public/tutorial/3.png" alt="Скриншот процесса импорта конфигурации на Android" />
                <p>Скриншот процесса импорта конфигурации на Android</p>
            </div>
            <li>Выберите файл конфигурации, предоставленный вам, и подтвердите импорт.</li>
            <div class="screenshot">
                <img src="/public/tutorial/4.jpg" alt="Скриншот выбора файла конфигурации" />
                <p>Скриншот выбора файла конфигурации</p>
            </div>
            <li>Нажмите на переключатель рядом с туннелем, чтобы активировать подключение.</li>
            <div class="screenshot">
                <img src="/public/tutorial/5.png" alt="Скриншот активированного подключения на Android" />
                <p>Скриншот активированного подключения на Android</p>
            </div>
        </ol>

        <p>Теперь вы успешно настроили WireGuard на вашем устройстве!</p>
        <p>Если вы хотите установить WireGuard на Linux, роутер или телевизор, обратитесь в нашу <a href="https://t.me/paia1nik">поддержку</a> для получения дополнительной помощи.</p>
        </div>

    </div>
</template>

<style lang="scss" scoped>

.hti_wrapper {
    width: 1200px;
    margin: 0 auto;
    margin-top: 20px;
    margin-bottom: 20px;
}

</style>