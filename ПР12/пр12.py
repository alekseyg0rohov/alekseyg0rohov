import tkinter as tk
import requests
import json

def nik():
    nik_name = repo_entry.get()
    try:
        response = requests.get(f"https://api.github.com/users/{nik_name}")
        response.raise_for_status()  # для проверки успешности запроса requests
        data = response.json()

        # Сохранение от фильтрованных данных
        filter = {
            'company': data.get('company'),
            'created_at': data.get('created_at'),
            'email': data.get('email'),
            'id': data.get('id'),
            'name': data.get('name'),
            'url': data.get('url')
        }

        # Сохранение от фильтрованных данных в JSON файл
        with open("info.json", "w") as file:
            json.dump(filter, file, indent=4)

        result_label.config(text="Данные сохранены в info.json")

    except requests.exceptions.RequestException as error: #Вывод ошибки при выполнении запроса HTTP
        result_label.config(text=f"Ошибка ввода: {error}")



seed = tk.Tk()
seed.geometry("450x250")
seed.resizable(False, False)
seed.title("Поиск данных репозитория")

repo_label = tk.Label(seed, text="Имя репозитория:")
repo_label.grid(row=0, column=0,padx=5, pady=5)

repo_entry = tk.Entry(seed)
repo_entry.grid(row=0, column=1,padx=5, pady=5)

get_info_button = tk.Button(seed, text="Поиск", command=nik)
get_info_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

result_label = tk.Label(seed, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

seed.mainloop()
