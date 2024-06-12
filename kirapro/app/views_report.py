from django.http import JsonResponse
from .models import Ticket

def ticket_sales_report(request):
    tickets = Ticket.objects.select_related('train', 'car', 'passenger', 'cashier').all()
    data = [{
        'id': ticket.id,
        'train': ticket.train.number,
        'car': ticket.car.number,
        'seat_number': ticket.seat_number,
        'passenger': {
            'first_name': ticket.passenger.first_name,
            'last_name': ticket.passenger.last_name,
            'middle_name': ticket.passenger.middle_name
        },
        'cashier': {
            'first_name': ticket.cashier.first_name,
            'last_name': ticket.cashier.last_name,
            'middle_name': ticket.cashier.middle_name
        },
        'price': str(ticket.price),
        'sale_date': ticket.sale_date,
    } for ticket in tickets]
    return JsonResponse(data, safe=False)

def passenger_ticket_sales_report(request, passenger_id):
    tickets = Ticket.objects.filter(passenger_id=passenger_id).select_related('train', 'car', 'cashier')
    data = [{
        'id': ticket.id,
        'train': ticket.train.number,
        'car': ticket.car.number,
        'seat_number': ticket.seat_number,
        'price': str(ticket.price),
        'sale_date': ticket.sale_date,
    } for ticket in tickets]
    return JsonResponse(data, safe=False)

def destination_sales_report(request, destination):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    tickets = Ticket.objects.filter(
        train__arrival_station__city=destination,
        sale_date__range=[start_date, end_date]
    ).select_related('train', 'car', 'passenger', 'cashier')
    data = [{
        'id': ticket.id,
        'train': ticket.train.number,
        'car': ticket.car.number,
        'seat_number': ticket.seat_number,
        'price': str(ticket.price),
        'sale_date': ticket.sale_date,
    } for ticket in tickets]
    return JsonResponse(data, safe=False)

def type_sales_report(request, destination, car_type):
    tickets = Ticket.objects.filter(
        train__arrival_station__city=destination,
        car__type=car_type
    ).select_related('train', 'car', 'passenger', 'cashier')
    data = [{
        'id': ticket.id,
        'train': ticket.train.number,
        'car': ticket.car.number,
        'seat_number': ticket.seat_number,
        'price': str(ticket.price),
        'sale_date': ticket.sale_date,
    } for ticket in tickets]
    return JsonResponse(data, safe=False)


def cashier_sales_report(request, cashier_id):
    tickets = Ticket.objects.filter(cashier_id=cashier_id).select_related('train', 'car', 'passenger')
    data = [{
        'id': ticket.id,
        'train': ticket.train.number,
        'car': ticket.car.number,
        'seat_number': ticket.seat_number,
        'price': str(ticket.price),
        'sale_date': ticket.sale_date,
    } for ticket in tickets]
    return JsonResponse(data, safe=False)


def passenger_ticket_report(request, ticket_id):
    try:
        ticket = Ticket.objects.select_related('train', 'car', 'passenger', 'cashier').get(id=ticket_id)
        data = {
            'id': ticket.id,
            'train': ticket.train.number,
            'car': ticket.car.number,
            'seat_number': ticket.seat_number,
            'passenger': {
                'first_name': ticket.passenger.first_name,
                'last_name': ticket.passenger.last_name,
                'middle_name': ticket.passenger.middle_name
            },
            'cashier': {
                'first_name': ticket.cashier.first_name,
                'last_name': ticket.cashier.last_name,
                'middle_name': ticket.cashier.middle_name
            },
            'price': str(ticket.price),
            'sale_date': ticket.sale_date,
        }
        return JsonResponse(data, safe=False)
    except Ticket.DoesNotExist:
        return JsonResponse({'error': 'Ticket not found'}, status=404)

