import json
import requests
user_data = requests.get('https://api.github.com/users/NixOS')# запрос
with open('file1.json', 'w') as typ: #открываем файл проеобразуем в json записываем в typ
    json.dump(user_data.json(), typ) # делаем копию в json файл
with open('file1.json', 'r') as typ2: #Читаем json
    file2 = json.load(typ2) #загружаем в переменную
    print('company:', file2.get('company'))
    print('created_at:', file2.get('created_at'))
    print('email:', file2.get('email'))
    print('id:', file2.get('id'))
    print('name:', file2.get('name'))
    print('url:', file2.get('url'))

