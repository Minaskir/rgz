import flet as ft
import requests

BASE_URL = "http://localhost:8000/api/"

def main(page: ft.Page):
    page.title = "Покупка и управление билетами"
    page.theme_mode = 'light'

    # Функция для отправки POST запроса к API
    def post_data(endpoint, data):
        response = requests.post(f"{BASE_URL}{endpoint}/", json=data)
        return response.status_code == 201

    # Добавление билета
    def add_ticket(e):
        train_id = train_id_field.value
        car_id = car_id_field.value
        seat_number = seat_number_field.value
        passenger_id = passenger_id_field.value
        cashier_id = cashier_id_field.value
        price = price_field.value
        sale_date = sale_date_field.value

        data = {
            "train": train_id,
            "car": car_id,
            "seat_number": seat_number,
            "passenger": passenger_id,
            "cashier": cashier_id,
            "price": price,
            "sale_date": sale_date
        }

        if post_data('tickets', data):
            page.snack_bar = ft.SnackBar(content=ft.Text("Билет успешно добавлен"))
        else:
            page.snack_bar = ft.SnackBar(content=ft.Text("Ошибка при добавлении билета"))
        page.snack_bar.open = True

    # UI элементы для добавления билета
    train_id_field = ft.TextField(label="ID поезда")
    car_id_field = ft.TextField(label="ID вагона")
    seat_number_field = ft.TextField(label="Номер места")
    passenger_id_field = ft.TextField(label="ID пассажира")
    cashier_id_field = ft.TextField(label="ID кассира")
    price_field = ft.TextField(label="Цена")
    sale_date_field = ft.TextField(label="Дата продажи (гггг-мм-дд)")

    add_ticket_button = ft.ElevatedButton(text="Добавить билет", on_click=add_ticket)

    # Размещение UI элементов на странице
    page.add(
        ft.Text("Добавление билета"),
        train_id_field,
        car_id_field,
        seat_number_field,
        passenger_id_field,
        cashier_id_field,
        price_field,
        sale_date_field,
        add_ticket_button
    )

ft.app(target=main)



















