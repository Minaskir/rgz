import flet as ft
import requests

BASE_URL = "http://localhost:8000/api/"

def main(page: ft.Page):
    page.title = "Покупка и управление билетами"
    page.theme_mode = 'light'

    def fetch_report(endpoint, params={}):
        try:
            response = requests.get(f"{BASE_URL}{endpoint}", params=params)
            if response.status_code == 200:
                return response.json()
            else:
                page.snack_bar = ft.SnackBar(content=ft.Text(f"Ошибка: {response.status_code} - {response.json().get('detail', 'Неизвестная ошибка')}"))
                page.snack_bar.open = True
                return []
        except requests.RequestException as e:
            page.snack_bar = ft.SnackBar(content=ft.Text(f"Ошибка при получении отчета: {str(e)}"))
            page.snack_bar.open = True
            return []

    def show_all_sales_report(e):
        report = fetch_report("all_sales_report/")
        display_report(report)

    def show_sales_by_passenger(e):
        passenger_id = passenger_id_report_field.value
        if passenger_id:
            report = fetch_report(f"sales_by_passenger/{passenger_id}/")
            display_report(report)
        else:
            page.snack_bar = ft.SnackBar(content=ft.Text("Пожалуйста, введите ID пассажира"))
            page.snack_bar.open = True

    def show_sales_to_city_in_period(e):
        city = city_report_field.value
        start_date = start_date_report_field.value
        end_date = end_date_report_field.value
        if city and start_date and end_date:
            report = fetch_report("sales_to_city_in_period/", {"city": city, "start_date": start_date, "end_date": end_date})
            display_report(report)
        else:
            page.snack_bar = ft.SnackBar(content=ft.Text("Пожалуйста, введите все данные для отчета"))
            page.snack_bar.open = True

    def show_sales_by_cashier(e):
        cashier_id = cashier_id_report_field.value
        if cashier_id:
            report = fetch_report(f"sales_by_cashier/{cashier_id}/")
            display_report(report)
        else:
            page.snack_bar = ft.SnackBar(content=ft.Text("Пожалуйста, введите ID кассира"))
            page.snack_bar.open = True

    def display_report(report):
        if report:
            report_text = "\n".join([str(ticket) for ticket in report])
        else:
            report_text = "Данные не найдены"
        report_output.value = report_text
        page.update()

    # UI elements for fetching reports
    passenger_id_report_field = ft.TextField(label="ID пассажира")
    city_report_field = ft.TextField(label="Город")
    start_date_report_field = ft.TextField(label="Начальная дата (гггг-мм-дд)")
    end_date_report_field = ft.TextField(label="Конечная дата (гггг-мм-дд)")
    cashier_id_report_field = ft.TextField(label="ID кассира")

    all_sales_report_button = ft.ElevatedButton(text="Отчет о всех продажах", on_click=show_all_sales_report)
    sales_by_passenger_report_button = ft.ElevatedButton(text="Отчет по пассажиру", on_click=show_sales_by_passenger)
    sales_to_city_in_period_report_button = ft.ElevatedButton(text="Отчет по городу и периоду", on_click=show_sales_to_city_in_period)
    sales_by_cashier_report_button = ft.ElevatedButton(text="Отчет по кассиру", on_click=show_sales_by_cashier)

    report_output = ft.Text("")

    # Adding elements to the page
    page.add(
        ft.Text("Отчеты"),
        all_sales_report_button,
        passenger_id_report_field,
        sales_by_passenger_report_button,
        city_report_field,
        start_date_report_field,
        end_date_report_field,
        sales_to_city_in_period_report_button,
        cashier_id_report_field,
        sales_by_cashier_report_button,
        report_output
    )

ft.app(target=main)




