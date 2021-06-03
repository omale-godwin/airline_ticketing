from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from .models import Flight_details
import random

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def about(request):
    print(request.session['return_date'])
    return render(request, 'pages/about.html')


def blog(request):
    return render(request, 'pages/blog.html')

def confirm(request, ticket_id):
    if request.user.is_authenticated:
    
        user_detail = User.objects.get(username__icontains=request.user)
        confirm_my_ticket = get_object_or_404(Flight_details, pk=ticket_id)
    
        # print(confirm_my_ticket)
        request.session['ticket'] = 'confirm_my_ticket' 
        context = {
        'adult': request.session['adult'],
        'class': request.session['class_type'],
        'date_choosen': request.session['departure'],
        'user_detail': user_detail,
        'price':request.session['price'], 
        'ticket': confirm_my_ticket
        }
       
    else:
        messages.error(request, 'PLEASE LOGIN TO BOOK YOUR AIRLINE TICKET')
        return redirect('login')
    return render(request, 'pages/confirm.html', context)


def ticket(request):
    
    queryset_list = Flight_details.objects.all()
    
    # from_city
    if 'from_city' in request.GET:
        from_city = request.GET['from_city']
        if from_city:
            queryset_list = queryset_list.filter(from_city__icontains=from_city)
    else:
        messages.error(request, 'please Select Your Current City Of Departure')
        return redirect('index')

    # to_city
    if 'to_city' in request.GET:
        to_city = request.GET['to_city']
        if to_city:
            queryset_list = queryset_list.filter(to_city__icontains=to_city)

    if from_city == to_city:
        messages.error(request, 'MAKE APPROPRIATE SELECT OF DESTINATION')
        return redirect('index')
       
    # class_type
    if 'class_type' in request.GET:
        request.session['class_type'] = request.GET['class_type']
        if 'class_type' in request.session:
            print('sweeettttttt')
    # departure
    if 'departure' in request.GET:
        request.session['departure'] = request.GET['departure']
        if 'departure' in request.session:
            print('sweeettttttt2222222222222')
            print(request.session['departure'])
    if request.session['departure'] == '':
        messages.error(request, 'PLEASE SELECT DATE TO DEPART')
        return redirect('index')

      # # return_date
    if 'return_date' in request.GET:
        request.session['return_date'] = request.GET['return_date']
        if 'return_date' in request.session:
            print('sweeettttttt333333333333')
            print(request.session['return_date'])
    # # adult
    if 'adult' in request.GET:
        request.session['adult'] = request.GET['adult']
        if 'adult' in request.session:
            print('sweeettadultgggggttttt333333333333')
            print(request.session['adult'])
   
    
    # # childrens
    if 'childrens' in request.GET:
        request.session['childrens'] = request.GET['childrens']
        if 'childrens' in request.session:
            print('sweeettttttt33333333childrens3333')
            print(request.session['childrens'])
    mydata = queryset_list.first()
    if request.session['class_type'] == 'Economy':
        price = 45000
    elif request.session['class_type'] == 'Premium Economy':
        price = 60000
    elif request.session['class_type'] == 'Business':
        price = 75000
    else:
        price = 90000
    
    request.session['price'] = price

    
    context = {
        'price':request.session['price'],
        'class': request.session['class_type'],
        'mydata': mydata,
        'date_choosen': request.session['departure'],
        'queryset_list': queryset_list
    }
    
   

    return render(request, 'pages/ticket.html', context)