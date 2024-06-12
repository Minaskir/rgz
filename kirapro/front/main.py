import flet as ft
import requests

BASE_URL = "http://localhost:8000/api/"

def main(page: ft.Page):
    page.title = "Покупка и управление билетами"
    page.theme_mode = 'light'
    page.scroll = "adaptive"

    # Функция для отправки POST запроса к API
    def post_data(endpoint, data):
        response = requests.post(f"{BASE_URL}{endpoint}/", json=data)
        return response.status_code == 201

    # Функция для отправки GET запроса к API
    def get_data(endpoint):
        response = requests.get(f"{BASE_URL}{endpoint}/")
        if response.status_code == 200:
            return response.json()
        else:
            return None

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

    # Просмотр билета
    def view_ticket(e):
        ticket_id = ticket_id_field.value
        ticket_data = get_data(f'tickets/{ticket_id}')
        if ticket_data:
            ticket_info.value = f"""
            ID билета: {ticket_data['id']}
            Поезд: {ticket_data['train']}
            Вагон: {ticket_data['car']}
            Номер места: {ticket_data['seat_number']}
            Пассажир: {ticket_data['passenger']}
            Кассир: {ticket_data['cashier']}
            Цена: {ticket_data['price']}
            Дата продажи: {ticket_data['sale_date']}
            """
        else:
            ticket_info.value = "Билет не найден"
        page.update()

    # UI элементы для добавления билета
    train_id_field = ft.TextField(label="ID поезда")
    car_id_field = ft.TextField(label="ID вагона")
    seat_number_field = ft.TextField(label="Номер места")
    passenger_id_field = ft.TextField(label="ID пассажира")
    cashier_id_field = ft.TextField(label="ID кассира")
    price_field = ft.TextField(label="Цена")
    sale_date_field = ft.TextField(label="Дата продажи (гггг-мм-дд)")

    add_ticket_button = ft.ElevatedButton(text="Добавить билет", on_click=add_ticket)

    # UI элементы для просмотра билета
    ticket_id_field = ft.TextField(label="ID билета")
    view_ticket_button = ft.ElevatedButton(text="Просмотр билета", on_click=view_ticket)
    ticket_info = ft.Text()

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
        add_ticket_button,
        ft.Divider(),
        ft.Text("Просмотр билета"),
        ticket_id_field,
        view_ticket_button,
        ticket_info,
        ft.Divider(),
    )

ft.app(target=main)




























