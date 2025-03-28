import os
import datetime
import sys

# Проверяем, существует ли файл version
if not os.path.exists('version'):
    with open('version', 'w') as f:
        f.write('1.5.1')

# Чтение текущей версии из файла
with open('version', 'r') as f:
    version = f.read().strip()

# Проверка правильности формата версии
if not all(i.isdigit() for i in version.split('.')):
    print("Некорректный формат версии!")
    exit()

# Чтение параметра обновления через аргумент командной строки
if len(sys.argv) < 2:
    print("Не указан параметр обновления (major, minor, patch)!")
    exit()

update_type = sys.argv[1]

# Разделение версии на компоненты
major, minor, patch = map(int, version.split('.'))

# Инкрементирование версии
if update_type == "major":
    print(f"Update type: {update_type}")
    major += 1
    minor = 0
    patch = 0
elif update_type == "minor":
    print(f"Update type: {update_type}")
    minor += 1
    patch = 0
elif update_type == "patch":
    print(f"Update type: {update_type}")
    patch += 1
else:
    print("Некорректный параметр обновления!")
    exit()

new_version = f"{major}.{minor}.{patch}"

# Запись новой версии в файл version
with open('version', 'w') as f:
    f.write(new_version)

# Define the log file path
log_file_path = 'version_log'

# Запись в файл version_log
current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")[:-3]
with open(log_file_path, 'a') as f:
    f.write(f"[{new_version}] <- [{version}] [{current_time}] {update_type} update\n")

if len(sys.argv) == 3 and sys.argv[2] == "version":
    print(new_version)
else:
    print(f"Версия обновлена на {new_version}")
