from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PassengerViewSet, StationViewSet, TrainViewSet, CarViewSet, CashierViewSet, TicketViewSet, TicketSaleViewSet, EmploymentContractViewSet

router = DefaultRouter()
router.register(r'passengers', PassengerViewSet)
router.register(r'stations', StationViewSet)
router.register(r'trains', TrainViewSet)
router.register(r'cars', CarViewSet)
router.register(r'cashiers', CashierViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'ticketsales', TicketSaleViewSet)
router.register(r'employmentcontracts', EmploymentContractViewSet)

urlpatterns = [
    path('', include(router.urls)),
]