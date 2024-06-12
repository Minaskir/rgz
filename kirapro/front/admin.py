
import flet as ft
import requests

API_URL = "http://localhost:8000/api"

def main(page: ft.Page):
    page.title = "Администратор"
    page.theme_mode = 'light'

    def fetch_stations():
        response = requests.get(f"{API_URL}/stations/")
        return response.json()

    def fetch_trains():
        response = requests.get(f"{API_URL}/trains/")
        return response.json()

    def fetch_cars():
        response = requests.get(f"{API_URL}/cars/")
        return response.json()

    def create_station(e):
        name = name_field.value
        city = city_field.value

        data = {"name": name, "city": city}
        response = requests.post(f"{API_URL}/stations/", json=data)
        if response.status_code == 201:
            load_stations()
        else:
            print("Failed to create station:", response.text)

    def create_train(e):
        number = number_field.value
        train_name = train_name_field.value
        departure_station_id = departure_station_field.value
        arrival_station_id = arrival_station_field.value

        data = {"number": number, "name": train_name, "departure_station": departure_station_id, "arrival_station": arrival_station_id}
        response = requests.post(f"{API_URL}/trains/", json=data)
        if response.status_code == 201:
            load_trains()
        else:
            print("Failed to create train:", response.text)

    def create_car(e):
        number = car_number_field.value
        car_type = car_type_field.value
        train_id = car_train_field.value

        data = {"number": number, "type": car_type, "train": train_id}
        response = requests.post(f"{API_URL}/cars/", json=data)
        if response.status_code == 201:
            load_cars()
        else:
            print("Failed to create car:", response.text)

    def update_ticket_price(e):
        ticket_id = ticket_id_field.value
        new_price = new_price_field.value

        data = {"price": new_price}
        response = requests.patch(f"{API_URL}/tickets/{ticket_id}/", json=data)
        if response.status_code == 200:
            page.snack_bar = ft.SnackBar(content=ft.Text("Цена билета успешно обновлена"))
        else:
            page.snack_bar = ft.SnackBar(content=ft.Text("Ошибка при обновлении цены билета"))
        page.snack_bar.open = True

    def create_contract(e):
        cashier_id = contract_cashier_id_field.value
        position = contract_position_field.value
        start_date = contract_start_date_field.value
        end_date = contract_end_date_field.value

        data = {
            "cashier": cashier_id,
            "position": position,
            "start_date": start_date,
            "end_date": end_date,
        }
        response = requests.post(f"{API_URL}/employmentcontracts/", json=data)
        if response.status_code == 201:
            page.snack_bar = ft.SnackBar(content=ft.Text("Трудовой договор успешно добавлен"))
        else:
            page.snack_bar = ft.SnackBar(content=ft.Text("Ошибка при добавлении трудового договора"))
        page.snack_bar.open = True

    def update_contract_position(e):
        contract_id = contract_id_field.value
        new_position = new_position_field.value

        data = {"position": new_position}
        response = requests.patch(f"{API_URL}/employmentcontracts/{contract_id}/", json=data)
        if response.status_code == 200:
            page.snack_bar = ft.SnackBar(content=ft.Text("Должность успешно обновлена"))
        else:
            page.snack_bar = ft.SnackBar(content=ft.Text("Ошибка при обновлении должности"))
        page.snack_bar.open = True

    def load_stations():
        stations = fetch_stations()
        station_list.controls = [ft.Text(f"{station['name']} ({station['city']})") for station in stations]
        page.update()

    def load_trains():
        trains = fetch_trains()
        train_list.controls = [ft.Text(f"{train['number']} - {train['name']}") for train in trains]
        page.update()

    def load_cars():
        cars = fetch_cars()
        car_list.controls = [ft.Text(f"{car['number']} - {car['type']}") for car in cars]
        page.update()

    ticket_id_field = ft.TextField(label="ID билета")
    new_price_field = ft.TextField(label="Новая цена")
    update_price_button = ft.ElevatedButton(text="Изменить цену билета", on_click=update_ticket_price)

    name_field = ft.TextField(label="Название станции")
    city_field = ft.TextField(label="Город")
    create_station_button = ft.ElevatedButton(text="Добавить станцию", on_click=create_station)

    number_field = ft.TextField(label="Номер поезда")
    train_name_field = ft.TextField(label="Название поезда")
    departure_station_field = ft.TextField(label="ID станции отправления")
    arrival_station_field = ft.TextField(label="ID станции прибытия")
    create_train_button = ft.ElevatedButton(text="Добавить поезд", on_click=create_train)

    car_number_field = ft.TextField(label="Номер вагона")
    car_type_field = ft.TextField(label="Тип вагона")
    car_train_field = ft.TextField(label="ID поезда")
    create_car_button = ft.ElevatedButton(text="Добавить вагон", on_click=create_car)

    contract_cashier_id_field = ft.TextField(label="ID кассира")
    contract_position_field = ft.TextField(label="Должность")
    contract_start_date_field = ft.TextField(label="Дата начала (гггг-мм-дд)")
    contract_end_date_field = ft.TextField(label="Дата окончания (гггг-мм-дд)")
    create_contract_button = ft.ElevatedButton(text="Добавить трудовой договор", on_click=create_contract)

    contract_id_field = ft.TextField(label="ID договора")
    new_position_field = ft.TextField(label="Новая должность")
    update_contract_position_button = ft.ElevatedButton(text="Изменить должность", on_click=update_contract_position)

    station_list = ft.Column()
    train_list = ft.Column()
    car_list = ft.Column()

    load_stations()
    load_trains()
    load_cars()

    page.add(
        ft.Column(
            [
                ft.Text("Изменение цены билета"),
                ticket_id_field,
                new_price_field,
                update_price_button,
                ft.Text("Добавление станции"),
                name_field,
                city_field,
                create_station_button,
                station_list,
                ft.Text("Добавление поезда"),
                number_field,
                train_name_field,
                departure_station_field,
                arrival_station_field,
                create_train_button,
                train_list,
                ft.Text("Добавление вагона"),
                car_number_field,
                car_type_field,
                car_train_field,
                create_car_button,
                car_list,
                ft.Text("Добавление трудового договора"),
                contract_cashier_id_field,
                contract_position_field,
                contract_start_date_field,
                contract_end_date_field,
                create_contract_button,
                ft.Text("Изменение должности в трудовом договоре"),
                contract_id_field,
                new_position_field,
                update_contract_position_button,
            ],
            scroll="adaptive",
            expand=True,
        )
    )

ft.app(target=main)





















