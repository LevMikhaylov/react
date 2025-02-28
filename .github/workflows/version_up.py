import os
import datetime

# Проверяем, существует ли файл version
if not os.path.exists('version'):
    with open('version', 'w') as f:
        f.write('1.0.0')

# Чтение текущей версии из файла
with open('version', 'r') as f:
    version = f.read().strip()

# Проверяем правильность формата версии
if not all(i.isdigit() for i in version.split('.')):
    print("Некорректный формат версии!")
    exit()

# Чтение параметра обновления
update_type = input("Введите параметр обновления (major, minor, patch): ")

# Разделение версии на компоненты
major, minor, patch = map(int, version.split('.'))

# Инкрементирование версии
if update_type == "major":
    major += 1
    minor = 0
    patch = 0
elif update_type == "minor":
    minor += 1
    patch = 0
elif update_type == "patch":
    patch += 1
else:
    print("Некорректный параметр обновления!")
    exit()

new_version = f"{major}.{minor}.{patch}"

# Запись новой версии в файл version
with open('version', 'w') as f:
    f.write(new_version)

# Запись в файл version_log
current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")[:-3]
with open('version_log', 'a') as f:
    f.write(f"[{new_version}] <- [{version}] [{current_time}] {update_type} update\n")

print(f"Версия обновлена на {new_version}")
