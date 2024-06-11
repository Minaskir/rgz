from rest_framework import viewsets
from .models import Passenger, Station, Train, Car, Cashier, Ticket, TicketSale, EmploymentContract
from .serializers import PassengerSerializer, StationSerializer, TrainSerializer, CarSerializer, CashierSerializer, TicketSerializer, TicketSaleSerializer, EmploymentContractSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TicketSale
from .serializers import TicketSaleSerializer

import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ticket, TicketSale
from .serializers import TicketSaleSerializer

logger = logging.getLogger(__name__)

@api_view(['GET'])
def all_sales_report(request):
    logger.info("Fetching all sales report")
    sales = TicketSale.objects.select_related('ticket__passenger', 'ticket__train__departure_station', 'ticket__train__arrival_station', 'ticket__car', 'ticket__cashier').all()
    if sales.exists():
        serializer = TicketSaleSerializer(sales, many=True)
        return Response(serializer.data)
    else:
        logger.info("No sales found")
        return Response({"detail": "No sales found"}, status=404)

@api_view(['GET'])
def sales_by_passenger(request, passenger_id):
    logger.info(f"Fetching sales report for passenger ID: {passenger_id}")
    sales = TicketSale.objects.filter(ticket__passenger_id=passenger_id).select_related('ticket__passenger', 'ticket__train__departure_station', 'ticket__train__arrival_station', 'ticket__car', 'ticket__cashier')
    if sales.exists():
        serializer = TicketSaleSerializer(sales, many=True)
        return Response(serializer.data)
    else:
        logger.info(f"No sales found for passenger ID: {passenger_id}")
        return Response({"detail": "No sales found for this passenger"}, status=404)

@api_view(['GET'])
def sales_to_city_in_period(request):
    city = request.GET.get('city')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    logger.info(f"Fetching sales report to city: {city} from {start_date} to {end_date}")
    sales = TicketSale.objects.filter(ticket__train__arrival_station__city=city, sale_date__range=[start_date, end_date]).select_related('ticket__passenger', 'ticket__train__departure_station', 'ticket__train__arrival_station', 'ticket__car', 'ticket__cashier')
    if sales.exists():
        serializer = TicketSaleSerializer(sales, many=True)
        return Response(serializer.data)
    else:
        logger.info(f"No sales found to city: {city} in the specified period")
        return Response({"detail": "No sales found to this city in the specified period"}, status=404)

@api_view(['GET'])
def sales_by_cashier(request, cashier_id):
    logger.info(f"Fetching sales report for cashier ID: {cashier_id}")
    sales = TicketSale.objects.filter(ticket__cashier_id=cashier_id).select_related('ticket__passenger', 'ticket__train__departure_station', 'ticket__train__arrival_station', 'ticket__car', 'ticket__cashier')
    if sales.exists():
        serializer = TicketSaleSerializer(sales, many=True)
        return Response(serializer.data)
    else:
        logger.info(f"No sales found for cashier ID: {cashier_id}")
        return Response({"detail": "No sales found for this cashier"}, status=404)




@api_view(['POST'])
def sell_ticket(request):
    serializer = TicketSaleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_ticket_sale(request, ticket_id):
    try:
        ticket_sale = TicketSale.objects.get(ticket_id=ticket_id)
    except TicketSale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TicketSaleSerializer(ticket_sale)
    return Response(serializer.data)


@api_view(['PUT', 'GET'])
def employment_contract_detail(request, contract_id):
    try:
        contract = EmploymentContract.objects.get(pk=contract_id)
    except EmploymentContract.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = EmploymentContractSerializer(contract, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = EmploymentContractSerializer(contract)
    return Response(serializer.data)


@api_view(['PUT', 'GET'])
def ticket_detail(request, ticket_id):
    try:
        ticket = Ticket.objects.get(pk=ticket_id)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = TicketSerializer(ticket)
    return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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
