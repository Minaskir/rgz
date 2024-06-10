from rest_framework import serializers
from .models import Passenger, Station, Train, Car, Cashier, Ticket, TicketSale, EmploymentContract

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CashierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashier
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketSale
        fields = '__all__'

class EmploymentContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentContract
        fields = '__all__'
