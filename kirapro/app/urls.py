from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PassengerViewSet, StationViewSet, TrainViewSet, CarViewSet, CashierViewSet, TicketViewSet, TicketSaleViewSet, EmploymentContractViewSet
from .views import UserViewSet
from . import views
# from .views import all_sales_report, sales_by_passenger, sales_to_city_in_period, sales_by_cashier
from .views import ticket_sales_report, passenger_ticket_sales_report
router = DefaultRouter()
router.register(r'passengers', PassengerViewSet)
router.register(r'stations', StationViewSet)
router.register(r'trains', TrainViewSet)
router.register(r'cars', CarViewSet)
router.register(r'cashiers', CashierViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'ticketsales', TicketSaleViewSet)
router.register(r'employmentcontracts', EmploymentContractViewSet)
router.register(r'users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    # path('tickets/sell/', views.sell_ticket, name='sell_ticket'),
    # path('tickets/sell/<int:ticket_id>/', views.get_ticket_sale, name='get_ticket_sale'),
    # path('all_sales_report/', all_sales_report, name='all_sales_report'),
    # path('sales_by_passenger/<int:passenger_id>/', sales_by_passenger, name='sales_by_passenger'),
    # path('sales_to_city_in_period/', sales_to_city_in_period, name='sales_to_city_in_period'),
    # path('sales_by_cashier/<int:cashier_id>/', sales_by_cashier, name='sales_by_cashier'),
    path('ticket_sales_report/', ticket_sales_report, name='ticket_sales_report'),
    path('passenger_ticket_sales_report/<int:passenger_id>/', passenger_ticket_sales_report, name='passenger_ticket_sales_report'),
    path('destination_ticket_sales_report/<str:city>/<str:start_date>/<str:end_date>/', views.destination_ticket_sales_report, name='destination_ticket_sales_report'),
    path('train_type_ticket_sales_report/<str:city>/<str:car_type>/', views.train_type_ticket_sales_report, name='train_type_ticket_sales_report'),
    path('cashier_sales_report/<int:cashier_id>/', views.cashier_sales_report, name='cashier_sales_report'),
    path('passenger_ticket_report/<int:passenger_id>/', views.passenger_ticket_report, name='passenger_ticket_report'),
    # path('destination_sales_report/', views.destination_sales_report, name='destination_sales_report'),
    # path('type_sales_report/', views.type_sales_report, name='type_sales_report'),
    # path('cashier_sales_report/<int:cashier_id>/', views.cashier_sales_report, name='cashier_sales_report'),
    # path('passenger_ticket_report/<int:ticket_id>/', views.passenger_ticket_report, name='passenger_ticket_report'),

    # Трудовой договор
    # path('employment-contracts/<int:contract_id>/', views.employment_contract_detail,
    #      name='employment_contract_detail'),
    #
    # # Изменение цены билета
    # path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
]