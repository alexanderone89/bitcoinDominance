<b>Тестовое задание реализовано  в виде небольшого микросервиса на FastApi, проект состоит из следующих файлов:</b>
<ul>
<li>
	config.py - для реализации класса настроек проекта (API ключ для доступа к API сайта coinmarketcap.com и название файла для хранения значений биткоина)
</li>
<li>
	http_client.py - файл, где реализованы основные методы для работы с внешним API (coinmarketcap.com)
</li>
<li>
	init.py - инициализация класса работы с внешним API
</li>
<li>
	main.py - главный файл-точка входа для работы нашего сервиса
</li>
<li>router.py - файл с ендпоинтами к методам класса
</li>
<li>
	sheduler.py - файл для реализации работы фонового процесса для записи полученных данных из внешнего API (coinmarketcap.com)
</li>
</ul>

<b>Для запуска проекат необходимо:</b>
<ul>
	<li>Иметь установленный Python3.9+</li>
<li>Клонировать репозиторий:</li>
git clone https://github.com/alexanderone89/bitcoinDominance.git
<li>Установить необходимые библиотеки:</li>
pip install -r requirements.txt
<li>Запуск проекта:</li>
uvicorn main:app --host 0.0.0.0 --port 8000
</ul>
