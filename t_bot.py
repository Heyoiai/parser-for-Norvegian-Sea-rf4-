import os
import dotenv

dotenv.load_dotenv()
# Проверить все переменные окружения
print(os.getenv('BOT_TOKEN'))
print(os.getenv('ADMIN_ID'))