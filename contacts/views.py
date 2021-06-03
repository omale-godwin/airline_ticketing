from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from .models import Contact
from django.contrib.auth.models import User


def contacted(request):
    if request.method == 'POST':
   
        first_name = request.POST['name']
        last_name = request.POST['surname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        # user_id = request.user.id
        if first_name == '':
             messages.error(request, 'first name should not be empty')
             return redirect('contact')
        elif last_name == '':
            messages.error(request, 'Last name should not be empty')
            return redirect('contact')
        elif email == '':
            messages.error(request, 'email field should not be empty')
            return redirect('contact')
        elif phone == '':
            messages.error(request, 'please provide a valid phone number')
            return redirect('contact')
        elif message == '':
            messages.error(request, 'please provide a valid description of your message')
            return redirect('contact')
        else:
             contact = Contact(first_name=first_name, last_name=last_name,email=email, phone=phone, message=message )

             contact.save()
        
             messages.success(request, 'Your request has been submitted, Our Custome Representative will get back to you soon')
             return redirect('contact')
  
      

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )
    return render(request, 'contact/contact.html')


def validatepay(request):
    if request.user.is_authenticated:
    
        user_detail = User.objects.get(username__icontains=request.user)

       
        
        context = {
        'adult': request.session['adult'],
        'class': request.session['class_type'],
        'date_choosen': request.session['departure'],
        'user_detail': user_detail,
        'price':request.session['price'], 
        'ticket': request.session['ticket']
        }
        
       
    else:
        messages.error(request, 'PLEASE LOGIN TO BOOK YOUR AIRLINE TICKET')
        return redirect('login')

    return render(request, 'pages/confirm.html')