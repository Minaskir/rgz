# import flet as ft
# import requests
#
# BASE_URL = "http://localhost:8000/api/"
#
# def main(page: ft.Page):
#     page.title = "Отчеты о продажах билетов"
#     page.theme_mode = 'light'
#     page.scroll = "adaptive"
#
#     # Функция для отправки GET запроса к API
#     def get_data(endpoint):
#         response = requests.get(f"{BASE_URL}{endpoint}/")
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return None
#
#     # Отчет о всех продажах билетов на железнодорожные перевозки
#     def ticket_sales_report(e):
#         ticket_sales = get_data('ticket_sales_report/')
#         if ticket_sales:
#             report_text = ""
#             for sale in ticket_sales:
#                 report_text += f"""
#                 Номер билета: {sale['ticket']['id']}
#                 Фамилия: {sale['ticket']['passenger']['last_name']}
#                 Имя: {sale['ticket']['passenger']['first_name']}
#                 Отчество: {sale['ticket']['passenger']['middle_name']}
#                 Начальная станция: {sale['ticket']['train']['departure_station']['name']}
#                 Конечная станция: {sale['ticket']['train']['arrival_station']['name']}
#                 Дата отправления: {sale['ticket']['departure_date']}
#                 Время отправления: {sale['ticket']['departure_time']}
#                 Время прибытия: {sale['ticket']['arrival_time']}
#                 Номер поезда: {sale['ticket']['train']['number']}
#                 Номер вагона: {sale['ticket']['car']['number']}
#                 Номер места: {sale['ticket']['seat_number']}
#                 Тип вагона: {sale['ticket']['car']['type']}
#                 Фамилия кассира: {sale['ticket']['cashier']['last_name']}
#                 Имя кассира: {sale['ticket']['cashier']['first_name']}
#                 Отчество кассира: {sale['ticket']['cashier']['middle_name']}
#                 Цена билета: {sale['ticket']['price']}
#                 Дата продажи: {sale['sale_date']}
#                 """
#             ticket_sales_info.value = report_text
#         else:
#             ticket_sales_info.value = "Отчет не найден"
#         page.update()
#
#     # Отчет о продажах билетов на различные железнодорожные поездки, совершенных определенным пассажиром
#     def passenger_ticket_sales_report(e):
#         passenger_id = passenger_id_field.value
#         passenger_sales = get_data(f'passenger_ticket_sales_report/{passenger_id}')
#         if passenger_sales:
#             report_text = ""
#             for sale in passenger_sales:
#                 report_text += f"""
#                 Номер билета: {sale['ticket']['id']}
#                 Дата отправления: {sale['ticket']['departure_date']}
#                 Время отправления: {sale['ticket']['departure_time']}
#                 Время прибытия: {sale['ticket']['arrival_time']}
#                 Номер поезда: {sale['ticket']['train']['number']}
#                 Номер вагона: {sale['ticket']['car']['number']}
#                 Номер места: {sale['ticket']['seat_number']}
#                 Тип вагона: {sale['ticket']['car']['type']}
#                 Цена билета: {sale['ticket']['price']}
#                 Дата продажи: {sale['sale_date']}
#                 """
#             passenger_sales_info.value = report_text
#         else:
#             passenger_sales_info.value = "Отчет не найден"
#         page.update()
#
#     # Отчет о продажах билетов в определенный населенный пункт в определенный период
#     def destination_sales_report(e):
#         destination = destination_field.value
#         start_date = start_date_field.value
#         end_date = end_date_field.value
#         destination_sales = get_data(f'destination_sales_report/{destination}?start_date={start_date}&end_date={end_date}')
#         if destination_sales:
#             report_text = ""
#             for sale in destination_sales:
#                 report_text += f"""
#                 Номер билета: {sale['ticket']['id']}
#                 Дата отправления: {sale['ticket']['departure_date']}
#                 Время отправления: {sale['ticket']['departure_time']}
#                 Время прибытия: {sale['ticket']['arrival_time']}
#                 Номер поезда: {sale['ticket']['train']['number']}
#                 Номер вагона: {sale['ticket']['car']['number']}
#                 Номер места: {sale['ticket']['seat_number']}
#                 Тип вагона: {sale['ticket']['car']['type']}
#                 Цена билета: {sale['ticket']['price']}
#                 Дата продажи: {sale['sale_date']}
#                 """
#             destination_sales_info.value = report_text
#         else:
#             destination_sales_info.value = "Отчет не найден"
#         page.update()
#
#     # Отчет о продажах билетов на поезд в определенный населенный пункт в определенном типе вагона и поезда
#     def type_sales_report(e):
#         destination = type_destination_field.value
#         car_type = car_type_field.value
#         type_sales = get_data(f'type_sales_report/{destination}/{car_type}')
#         if type_sales:
#             report_text = ""
#             for sale in type_sales:
#                 report_text += f"""
#                 Номер билета: {sale['ticket']['id']}
#                 Дата отправления: {sale['ticket']['departure_date']}
#                 Время отправления: {sale['ticket']['departure_time']}
#                 Время прибытия: {sale['ticket']['arrival_time']}
#                 Номер поезда: {sale['ticket']['train']['number']}
#                 Номер вагона: {sale['ticket']['car']['number']}
#                 Номер места: {sale['ticket']['seat_number']}
#                 Тип вагона: {sale['ticket']['car']['type']}
#                 Цена билета: {sale['ticket']['price']}
#                 Дата продажи: {sale['sale_date']}
#                 """
#             type_sales_info.value = report_text
#         else:
#             type_sales_info.value = "Отчет не найден"
#         page.update()
#
#     # Отчет о продажах билетов, реализованных определенным кассиром
#     def cashier_sales_report(e):
#         cashier_id = cashier_id_field.value
#         cashier_sales = get_data(f'cashier_sales_report/{cashier_id}')
#         if cashier_sales:
#             report_text = ""
#             for sale in cashier_sales:
#                 report_text += f"""
#                 Номер билета: {sale['ticket']['id']}
#                 Дата отправления: {sale['ticket']['departure_date']}
#                 Время отправления: {sale['ticket']['departure_time']}
#                 Время прибытия: {sale['ticket']['arrival_time']}
#                 Номер поезда: {sale['ticket']['train']['number']}
#                 Номер вагона: {sale['ticket']['car']['number']}
#                 Номер места: {sale['ticket']['seat_number']}
#                 Тип вагона: {sale['ticket']['car']['type']}
#                 Цена билета: {sale['ticket']['price']}
#                 Дата продажи: {sale['sale_date']}
#                 """
#             cashier_sales_info.value = report_text
#         else:
#             cashier_sales_info.value = "Отчет не найден"
#         page.update()
#
#     # Отчет о билете на поезд определенного пассажира
#     def passenger_ticket_report(e):
#         ticket_id = passenger_ticket_id_field.value
#         ticket_data = get_data(f'passenger_ticket_report/{ticket_id}')
#         if ticket_data:
#             report_text = f"""
#             Номер билета: {ticket_data['ticket']['id']}
#             Дата отправления: {ticket_data['ticket']['departure_date']}
#             Время отправления: {ticket_data['ticket']['departure_time']}
#             Время прибытия: {ticket_data['ticket']['arrival_time']}
#             Номер поезда: {ticket_data['ticket']['train']['number']}
#             Номер вагона: {ticket_data['ticket']['car']['number']}
#             Номер места: {ticket_data['ticket']['seat_number']}
#             Тип вагона: {ticket_data['ticket']['car']['type']}
#             Цена билета: {ticket_data['ticket']['price']}
#             Дата продажи: {ticket_data['sale_date']}
#             """
#             passenger_ticket_info.value = report_text
#         else:
#             passenger_ticket_info.value = "Билет не найден"
#         page.update()
#
#     # UI элементы для отчетов
#     ticket_sales_report_button = ft.ElevatedButton(text="Отчет о продажах билетов", on_click=ticket_sales_report)
#     ticket_sales_info = ft.Text()
#
#     passenger_id_field = ft.TextField(label="ID пассажира")
#     passenger_ticket_sales_report_button = ft.ElevatedButton(text="Отчет о продажах пассажира", on_click=passenger_ticket_sales_report)
#     passenger_sales_info = ft.Text()
#
#     destination_field = ft.TextField(label="Населенный пункт")
#     start_date_field = ft.TextField(label="Дата начала (гггг-мм-дд)")
#     end_date_field = ft.TextField(label="Дата окончания (гггг-мм-дд)")
#     destination_sales_report_button = ft.ElevatedButton(text="Отчет о продажах по пункту", on_click=destination_sales_report)
#     destination_sales_info = ft.Text()
#
#     type_destination_field = ft.TextField(label="Населенный пункт")
#     car_type_field = ft.TextField(label="Тип вагона")
#     type_sales_report_button = ft.ElevatedButton(text="Отчет по типу вагона", on_click=type_sales_report)
#     type_sales_info = ft.Text()
#
#     cashier_id_field = ft.TextField(label="ID кассира")
#     cashier_sales_report_button = ft.ElevatedButton(text="Отчет о продажах кассира", on_click=cashier_sales_report)
#     cashier_sales_info = ft.Text()
#
#     passenger_ticket_id_field = ft.TextField(label="ID билета")
#     passenger_ticket_report_button = ft.ElevatedButton(text="Отчет о билете пассажира", on_click=passenger_ticket_report)
#     passenger_ticket_info = ft.Text()
#
#     # Размещение UI элементов на странице
#     page.add(
#         ft.Text("Отчет о продажах билетов"),
#         ticket_sales_report_button,
#         ticket_sales_info,
#         ft.Divider(),
#         ft.Text("Отчет о продажах билетов пассажира"),
#         passenger_id_field,
#         passenger_ticket_sales_report_button,
#         passenger_sales_info,
#         ft.Divider(),
#         ft.Text("Отчет о продажах в населенный пункт"),
#         destination_field,
#         start_date_field,
#         end_date_field,
#         destination_sales_report_button,
#         destination_sales_info,
#         ft.Divider(),
#         ft.Text("Отчет по типу вагона"),
#         type_destination_field,
#         car_type_field,
#         type_sales_report_button,
#         type_sales_info,
#         ft.Divider(),
#         ft.Text("Отчет о продажах кассира"),
#         cashier_id_field,
#         cashier_sales_report_button,
#         cashier_sales_info,
#         ft.Divider(),
#         ft.Text("Отчет о билете пассажира"),
#         passenger_ticket_id_field,
#         passenger_ticket_report_button,
#         passenger_ticket_info,
#         ft.Divider(),
#     )
#
# ft.app(target=main)

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

    # Функция для добавления билета
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

    # Функция для просмотра билета
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

    # Функция для обработки отчетов
    def format_ticket_data(tickets):
        if not tickets:
            return "Отчет не найден"

        return '\n'.join([f"""
            ID билета: {ticket['id']}
            Поезд: {ticket['train']}
            Вагон: {ticket['car']}
            Номер места: {ticket['seat_number']}
            Пассажир: {ticket['passenger']}
            Кассир: {ticket['cashier']}
            Цена: {ticket['price']}
            Дата продажи: {ticket['sale_date']}
            """ for ticket in tickets])

    # Отчет обо всех продажах билетов
    def view_all_ticket_sales_report(e):
        report_data = get_data('ticket_sales_report')
        report_info.value = format_ticket_data(report_data)
        page.update()

    # Отчет о продажах билетов на различные железнодорожные поездки, совершенных определенным пассажиром
    def view_passenger_ticket_sales_report(e):
        passenger_id = passenger_id_report_field.value
        report_data = get_data(f'passenger_ticket_sales_report/{passenger_id}')
        report_info.value = format_ticket_data(report_data)
        page.update()

    # Отчет о продажах билетов в определенный населенный пункт в определенный период
    def view_destination_ticket_sales_report(e):
        city = city_field.value
        start_date = start_date_field.value
        end_date = end_date_field.value
        report_data = get_data(f'destination_ticket_sales_report/{city}/{start_date}/{end_date}')
        report_info.value = format_ticket_data(report_data)
        page.update()

    # Отчет о продажах билетов на поезд в определенный населенный пункт в определенном типе вагона и поезда
    def view_train_type_ticket_sales_report(e):
        city = city_train_field.value
        car_type = car_type_field.value
        report_data = get_data(f'train_type_ticket_sales_report/{city}/{car_type}')
        report_info.value = format_ticket_data(report_data)
        page.update()

    # Отчет о продажах билетов, реализованных определенным кассиром
    def view_cashier_sales_report(e):
        cashier_id = cashier_id_report_field.value
        report_data = get_data(f'cashier_sales_report/{cashier_id}')
        report_info.value = format_ticket_data(report_data)
        page.update()

    # Отчет о билете на поезд определенного пассажира
    def view_passenger_ticket_report(e):
        passenger_id = passenger_id_ticket_field.value
        report_data = get_data(f'passenger_ticket_report/{passenger_id}')
        report_info.value = format_ticket_data(report_data)
        page.update()

    # Функция для показа информации о программе
    def show_about_dialog(e):
        about_dialog.open = True
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

    # UI элементы для отчетов
    report_info = ft.Text()

    # UI элементы для отчета обо всех продажах билетов
    all_ticket_sales_report_button = ft.ElevatedButton(text="Отчет обо всех продажах билетов",
                                                       on_click=view_all_ticket_sales_report)

    # UI элементы для отчета о продажах билетов на различные железнодорожные поездки, совершенных определенным пассажиром
    passenger_id_report_field = ft.TextField(label="ID пассажира для отчета")
    passenger_ticket_sales_report_button = ft.ElevatedButton(text="Отчет о продажах билетов определенного пассажира",
                                                             on_click=view_passenger_ticket_sales_report)

    # UI элементы для отчета о продажах билетов в определенный населенный пункт в определенный период
    city_field = ft.TextField(label="Город назначения")
    start_date_field = ft.TextField(label="Начальная дата (гггг-мм-дд)")
    end_date_field = ft.TextField(label="Конечная дата (гггг-мм-дд)")
    destination_ticket_sales_report_button = ft.ElevatedButton(
        text="Отчет о продажах билетов в определенный населенный пункт за период",
        on_click=view_destination_ticket_sales_report)

    # UI элементы для отчета о продажах билетов на поезд в определенный населенный пункт в
    city_train_field = ft.TextField(label="Город назначения")
    car_type_field = ft.TextField(label="Тип вагона")
    train_type_ticket_sales_report_button = ft.ElevatedButton(text="Отчет о продажах билетов по типу вагона и поезда",
                                                              on_click=view_train_type_ticket_sales_report)

    # UI элементы для отчета о продажах билетов, реализованных определенным кассиром
    cashier_id_report_field = ft.TextField(label="ID кассира для отчета")
    cashier_sales_report_button = ft.ElevatedButton(text="Отчет о продажах билетов кассиром",
                                                    on_click=view_cashier_sales_report)

    # UI элементы для отчета о билете на поезд определенного пассажира
    passenger_id_ticket_field = ft.TextField(label="ID пассажира для билета")
    passenger_ticket_report_button = ft.ElevatedButton(text="Билет на поезд определенного пассажира",
                                                       on_click=view_passenger_ticket_report)

    # UI элементы для кнопки "О программе"
    about_button = ft.ElevatedButton(text="О программе", on_click=show_about_dialog)
    about_dialog = ft.AlertDialog(
        title=ft.Text("О программе"),
        content=ft.Text(
            "Программа для управления и продажи железнодорожных билетов.\n\nАвторы: Иванов Иван, Петров Петр."),
        actions=[
            ft.TextButton("Закрыть", on_click=lambda e: setattr(about_dialog, 'open', False))
        ],
        open=False
    )

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
        ft.Text("Отчеты"),
        all_ticket_sales_report_button,
        passenger_id_report_field,
        passenger_ticket_sales_report_button,
        city_field,
        start_date_field,
        end_date_field,
        destination_ticket_sales_report_button,
        city_train_field,
        car_type_field,
        train_type_ticket_sales_report_button,
        cashier_id_report_field,
        cashier_sales_report_button,
        passenger_id_ticket_field,
        passenger_ticket_report_button,
        report_info,
        ft.Divider(),
        about_button,
        about_dialog,
    )
ft.app(target=main)









