from django.contrib import admin

from .models import Jet_detail, Flight_details, Payment_details, Passengers, Ticket_details

class JetAdmin(admin.ModelAdmin):
  list_display = ('id', 'jet_name', 'jet_type', 'active', 'jet_capacity', 'jet_photo')
  list_display_links = ('id', 'jet_name')
  list_filter = ('id',)
  list_editable = ('active',)
  search_fields = ('name', 'jet_capacity', 'active')
  list_per_page = 25

class FlightAdmin(admin.ModelAdmin):
  list_display = ('id', 'flight_no', 'from_city', 'to_city', 'departure_time', 'price_economy', 'price_business')
  list_display_links = ('id', 'flight_no')
  list_filter = ('id',)
  search_fields = ('flight_no', 'from_city', 'to_city')
  list_per_page = 25


class PassengerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'booking_ticket', 'phone', 'email')
    list_display_links = ('id', 'user_id')
    list_filter = ('booking_ticket', 'user_id')
    search_fields = ('user_id', 'booking_ticket')
    list_per_page = 25



class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'booking_ticket', 'payment_amout', 'payment_date', 'booking_satutus')
    list_display_links = ('user_id', 'booking_ticket')
    list_filter = ('id', 'booking_ticket')
    search_fields = ('name', 'booking_ticket', 'payment_amout')
    list_per_page = 25


class TicketAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'date_of_reservation', 'flight_no', 'journey_date', 'booking_ticket', 'class_level')
    list_display_links = ('user_id', 'booking_ticket')
    list_filter = ('id', 'booking_ticket')
    search_fields = ('user_id', 'booking_ticket', 'journey_date')
    list_per_page = 25


admin.site.register(Jet_detail, JetAdmin)
admin.site.register(Ticket_details, TicketAdmin)
admin.site.register(Passengers, PassengerAdmin)
admin.site.register(Flight_details, FlightAdmin)
admin.site.register(Payment_details, PaymentAdmin)