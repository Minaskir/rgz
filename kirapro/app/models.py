from django.db import models

class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

class Station(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Train(models.Model):
    number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    departure_station = models.ForeignKey(Station, related_name='departure_trains', on_delete=models.CASCADE)
    arrival_station = models.ForeignKey(Station, related_name='arrival_trains', on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class Car(models.Model):
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    train = models.ForeignKey(Train, related_name='cars', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number} - {self.type}'

class Cashier(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

class Ticket(models.Model):
    train = models.ForeignKey(Train, related_name='tickets', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='tickets', on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    passenger = models.ForeignKey(Passenger, related_name='tickets', on_delete=models.CASCADE)
    cashier = models.ForeignKey(Cashier, related_name='tickets', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateField()

    def __str__(self):
        return f'Ticket {self.id} for {self.passenger}'

class TicketSale(models.Model):
    ticket = models.OneToOneField(Ticket, related_name='sale', on_delete=models.CASCADE)
    sale_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Sale for Ticket {self.ticket.id}'

class EmploymentContract(models.Model):
    cashier = models.OneToOneField(Cashier, related_name='employment_contract', on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Contract for {self.cashier}'
