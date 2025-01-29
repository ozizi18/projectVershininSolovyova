# Tarot Astrology Bot

Этот бот на основе Telegram помогает пользователям получать советы и информацию о таро, астрологии и отношениях. Он использует нейросеть для генерации ответов на вопросы пользователей.

## Описание

Бот предоставляет интерфейс для общения с нейросетью, которая может отвечать на вопросы о таро, астрологии, нумерологии и других темах, связанных с духовностью и личностным развитием. Пользователи могут задавать вопросы и получать ответы в реальном времени.

## Функции

- Ответы на вопросы о таро и астрологии.
- Поддержка общения на русском языке.
- Использование прокси для работы в регионах с ограничениями.

## Установка

### Предварительные требования

- Python 3.7 или выше
- Установленные библиотеки: `aiogram`, `requests`

### Установка зависимостей

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ozizi18/projectVershininSolovyova.git
   cd projectVershininSolovyova
   ```

2. Создайте виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

### Настройка

1. Получите токен вашего бота от [BotFather](https://t.me/botfather).
2. Откройте файл `bot.py` и замените `YOUR_BOT_TOKEN` на ваш токен.

### Запуск

Запустите бота с помощью следующей команды:
```bash
python bot.py
```

## Использование

После запуска бота, вы можете начать общение с ним, отправив команду `/start`. Бот ответит приветственным сообщением и предложит задать вопрос.

## Лицензия

Этот проект лицензирован под MIT License - смотрите файл [LICENSE](LICENSE) для подробностей.

## Контрибьюция

Если вы хотите внести свой вклад в проект, пожалуйста, создайте форк репозитория, внесите изменения и создайте pull request.

## Связь

Если у вас есть вопросы или предложения, вы можете связаться со мной через [viperrpank@icloud.com](mailto:viperrpank@icloud.com).
```