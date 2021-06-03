from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# from .models import Jet_detail
from datetime import datetime

from django.db.models.fields import CharField


# Create your models here.
class Jet_detail(models.Model):
    jet_name = models.CharField(max_length=200)
    jet_type = models.CharField(max_length=200)
    jet_capacity = models.CharField(max_length=200)
    active = models.BooleanField(blank=True)
    jet_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.jet_name


class Flight_details(models.Model):
    flight_no = models.ForeignKey(Jet_detail, on_delete=models.DO_NOTHING)
    from_city = models.CharField(max_length=200, blank=False)
    to_city = models.CharField(max_length=200, blank=False)
    departure_date = models.DateTimeField(blank=True, null=True)
    arrival_date = models.DateTimeField(blank=True, null=True)
    departure_time = models.TimeField(blank=False)
    arrival_time = models.TimeField(blank=False)
    adult = models.CharField(max_length=200, blank=True)
    childrens = models.CharField(max_length=200,blank=True)
    class_type = models.CharField(max_length=200, blank=True)
    # seats_economy = models.IntegerField(blank=True)
    # seats_business = models.IntegerField(blank=True)
    price_economy = models.IntegerField()
    price_business = models.IntegerField()
    def __str__(self):
        return self.from_city


class Payment_details(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    booking_ticket = models.CharField(max_length=200)
    payment_date = models.DateTimeField(default=datetime.now, blank=False)
    payment_amout = models.IntegerField(blank=False)
    payment_mode = models.CharField(max_length=200)
    booking_satutus = models.BooleanField(default=False)
    def __str__(self):
        return self.booking_ticket


class Passengers(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    booking_ticket = models.CharField(max_length=200, blank=False)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    meal_choice = models.CharField(max_length=200)
    # frequent_flier_no = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Ticket_details(models.Model):
    Payment_details_id = models.ForeignKey(Payment_details, on_delete=models.DO_NOTHING)
    date_of_reservation = models.DateTimeField(blank=False)
    flight_no = models.CharField(max_length=200)
    journey_date = models.DateTimeField(blank=False)
    booking_ticket = models.CharField(max_length=200, blank=False)
    booking_status = models.BooleanField(default=False)
    class_level = models.CharField(max_length=200)
    priority_checkin = models.CharField(max_length=200)
    # payment_id = models.ForeignKey(Payment_details, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def str__(self):
        return self.Payment_details_id






    

    



