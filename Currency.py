from customtkinter import *
import requests
# python -m pip install requests

set_appearance_mode("dark")
set_default_color_theme("blue")

window = CTk()
window.title("Конвертер валют")
window.geometry("380x420")

# Валюти
currencies = ["USD", "EUR", "UAH", "GBP", "PLN"]


def convert():
    # Отримати дані
    amount = entry.get()
    from_cur = from_menu.get()
    to_cur = to_menu.get()

    if amount == "":
        result.configure(text="Веддіть суму!")
        return


    try:
        data = requests.get(
            f"https://open.er-api.com/v6/latest/{from_cur}"
        ).json()


        # Конвертація
        rate = data["rates"][to_cur]
        total = float(amount) * rate

        result.configure (text=f"{amount} {from_cur} = {round(total, 2)} {to_cur}")



    except:
        result.configure(text="Помилка!")


# Заголовок "КОНВЕРТЕР ВАЛЮТ"
CTkLabel(window, text="КОНВЕРТЕР ВАЛЮТ", font=("Arial", 24, "bold")).pack(pady=15)
# Поле введення "Введіть суму"
entry = CTkEntry(window, width=220, placeholder_text="Введіть суму")
entry.pack(pady=10)
# Список валют
from_menu = CTkOptionMenu(window, values=currencies)
from_menu.pack(pady=10)
from_menu.set("USD")

# Список валют
to_menu = CTkOptionMenu(window, values=currencies)
to_menu.pack(pady=10)
to_menu.set("UAH")
# Кнопка "Конвертувати"
CTkButton(window, text="Конвертувати", command=convert).pack(pady=15)


# Текст "Введіть дані"
result = CTkLabel(window, text="Веддіть дані", font=("Arial", 24, "bold"))
result.pack(pady=20)

window.mainloop()