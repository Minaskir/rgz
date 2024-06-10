from rest_framework import viewsets
from .models import Passenger, Station, Train, Car, Cashier, Ticket, TicketSale, EmploymentContract
from .serializers import PassengerSerializer, StationSerializer, TrainSerializer, CarSerializer, CashierSerializer, TicketSerializer, TicketSaleSerializer, EmploymentContractSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CashierViewSet(viewsets.ModelViewSet):
    queryset = Cashier.objects.all()
    serializer_class = CashierSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketSaleViewSet(viewsets.ModelViewSet):
    queryset = TicketSale.objects.all()
    serializer_class = TicketSaleSerializer

class EmploymentContractViewSet(viewsets.ModelViewSet):
    queryset = EmploymentContract.objects.all()
    serializer_class = EmploymentContractSerializer
