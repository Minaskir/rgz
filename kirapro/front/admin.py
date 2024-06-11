import flet as ft
import requests

API_URL = "http://localhost:8000/api"

def main(page: ft.Page):
    page.title = "Администратор"

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
        name = name_field.value
        departure_station_id = departure_station_field.value
        arrival_station_id = arrival_station_field.value

        data = {"number": number, "name": name, "departure_station": departure_station_id, "arrival_station": arrival_station_id}
        response = requests.post(f"{API_URL}/trains/", json=data)
        if response.status_code == 201:
            load_trains()
        else:
            print("Failed to create train:", response.text)

    def create_car(e):
        number = car_number_field.value
        type = car_type_field.value
        train_id = car_train_field.value

        data = {"number": number, "type": type, "train": train_id}
        response = requests.post(f"{API_URL}/cars/", json=data)
        if response.status_code == 201:
            load_cars()
        else:
            print("Failed to create car:", response.text)

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

    name_field = ft.TextField(label="Название станции")
    city_field = ft.TextField(label="Город")
    create_station_button = ft.ElevatedButton(text="Добавить станцию", on_click=create_station)

    number_field = ft.TextField(label="Номер поезда")
    name_field = ft.TextField(label="Название поезда")
    departure_station_field = ft.TextField(label="ID станции отправления")
    arrival_station_field = ft.TextField(label="ID станции прибытия")
    create_train_button = ft.ElevatedButton(text="Добавить поезд", on_click=create_train)

    car_number_field = ft.TextField(label="Номер вагона")
    car_type_field = ft.TextField(label="Тип вагона")
    car_train_field = ft.TextField(label="ID поезда")
    create_car_button = ft.ElevatedButton(text="Добавить вагон", on_click=create_car)

    station_list = ft.Column()
    train_list = ft.Column()
    car_list = ft.Column()

    load_stations()
    load_trains()
    load_cars()

    page.add(
        ft.Column([name_field, city_field]),
        create_station_button,
        station_list,
        ft.Column([number_field, name_field, departure_station_field, arrival_station_field]),
        create_train_button,
        train_list,
        ft.Column([car_number_field, car_type_field, car_train_field]),
        create_car_button,
        car_list,
    )

ft.app(target=main)















