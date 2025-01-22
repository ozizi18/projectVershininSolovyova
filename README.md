# projectVershininSolovyova
этот бот поможет вам не забыть через сколько ваше день рождения.
Будет написано на языке программирование python3.
python3 -m venv venv
активация виртуального окружения
source venv/bin/activate

## Установка
установка всех зависимостей 
python_bot.py
### Выжные моменты:в
git clone https://github.com/Kamilfo-Developer/telegram-support-bot.git
cd telegram-support-bot
BOT_TOKEN=<Токен Вашего бота>
OWNER_PASSWORD=<Пароль для инициализации владельца бота>
DEFAULT_LANGUAGE_CODE=ru
docker-compose up -d
Запуск с помощью исходного кода
git clone https://github.com/Kamilfo-Developer/telegram-support-bot.git
poetry install
poetry shell
BOT_TOKEN=<Токен Вашего бота>
OWNER_PASSWORD=<Пароль для инициализации владельца бота>
DEFAULT_LANGUAGE_CODE=ru
cd bot/db/migrations
alembic upgrade head
cd ../../..
python -m bot
