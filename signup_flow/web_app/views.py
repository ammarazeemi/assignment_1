from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Users, Records, Category
from django.core.mail import send_mail
from django.conf import settings
import random
from datetime import datetime

# Create your views here.

def index(request):
    if request.method == 'POST':
        try:
            Users(
                    name=request.POST.get('name'),
                    email=request.POST.get('email'),
                    password=request.POST.get('password'),
                    created_at=datetime.now(),
                    updated_at=datetime.now()
            ).save()

            return redirect('records')
        except IntegrityError:
            return render(request, 'index.html', {'msg': 'Email already exists'})
    else:
        return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        try:
            user = Users.objects.get(
                email=request.POST.get('email'),
                password=request.POST.get('password')
            )
            request.session['id'] = user.id
            request.session['email'] = user.email
            return redirect('records')
        except Users.DoesNotExist:
            return render(request, 'signin.html', {'msg': 'Invalid email or password'})
    return render(request, 'signin.html')

def email_authenticate(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if not email:
            return redirect('signin')

        if Users.objects.get(email=email).email == email:

            request.session['email'] = email
            # Generate OTP
            otp = random.randint(1000, 9999)
            request.session['otp'] = otp

            # Send OTP via email
            subject = "Verify Your Email"
            message = f"Your OTP is {otp}. Please enter this code to verify your email."
            from_email = settings.EMAIL_HOST_USER

            send_mail(subject, message, from_email, [email])

        return redirect('authorization')
    return render(request, 'email_authenticate.html')

def authorization(request):
    if request.method == "POST":
        otp_input = request.POST.get('num1')
        otp_input += request.POST.get('num2')
        otp_input += request.POST.get('num3')
        otp_input += request.POST.get('num4')
        otp_session = request.session.get('otp')

        if otp_input == str(otp_session):
            return redirect('change_pass')
        else:
            return render(request, 'authorization.html', {'msg': 'Invalid OTP'})
    return render(request, 'authorization.html')

def records(request):
    if request.method == 'POST':
        if request.POST.get('add_product') == 'add_product':
            try:
                category = request.POST.get('category')
                category = Category.objects.get(id=category)
                Records(
                    title=request.POST.get('title'),
                    brand=request.POST.get('brand'),
                    category = category,
                    description=request.POST.get('description'),
                    price=request.POST.get('price'),
                    qty=request.POST.get('qty'),
                    user = Users.objects.get(id=request.session['id']),
                    created_at=datetime.now(),
                    updated_at=datetime.now()
                ).save()
            except Exception as e:
                return render(request, 'records.html', {'msg': f'Product not added \n{e}'})
            
        elif request.POST.get('update_product') == 'update_product':
            try:
                Records.objects.filter(id=request.POST.get('id')).update(
                    title=request.POST.get('title'),
                    brand=request.POST.get('brand'),
                    category=request.POST.get('category'),
                    description=request.POST.get('description'),
                    price=request.POST.get('price'),
                    qty=request.POST.get('qty'),
                    updated_at=datetime.now()
                )
                context = {'record': Records.objects.get(id=request.POST.get('id'))}
            except:
                return render(request, 'records.html', {'msg': 'Product not found'})
            
        elif request.POST.get('delete_product') == 'delete_product':
            try:
                Records.objects.filter(id=request.POST.get('id')).delete().save()
            except:
                return render(request, 'records.html', {'msg': 'Product not found'})
    
    records = Records.objects.all()
    category = Category.objects.all()
    return render(request, 'records.html', {'records1': records, 'category1': category})

def change_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password == confirm_password:
            Users.objects.filter(email=request.session['email']).update(password=new_password)
            return redirect('signin')
        else:
            return render(request, 'change_pass.html', {'msg': 'Passwords do not match'})
    return render(request, 'change_pass.html')
