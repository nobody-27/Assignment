from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from .models import *
from .models import User,Vehicle,Vehicle_Types
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import (
    authenticate, 
    login, 
    logout
)
# Create your views here.

class Home(View):
    def get(self,request):
        vehicle_obj = Vehicle.objects.all().order_by('-id')
        context = {
            'vehicle_obj':vehicle_obj,
        }
        return render(request,'vehicle/home.html',context)
    

class Login(View):
    def get(self,request):
        return render(request,'vehicle/login.html')
    
    def post(self,request):
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        user = authenticate(username = user_name, password = pass_word)
        if user is not None:
            login(request, user)
            return redirect('home')
        messages.error(request, 'username & password not match!',extra_tags='danger')
        return render(request,'vehicle/login.html')

class Register(View):
    def get(self,request):
        return render(request,'vehicle/register.html')
    
    def post(self,request):
        user_name = request.POST.get('username')
        role = request.POST.get('role')
        password_1 = request.POST.get('pass1')
        password_2 = request.POST.get('pass2')

        if User.objects.filter(username=user_name).exists():
            messages.error(request, 'Username Exits .',extra_tags='danger')
            return render(request,'vehicle/register.html')

        if password_1 != password_2:
            messages.success(request, 'paasword not match',extra_tags='danger')
            return render(request,'vehicle/register.html')
        
        user_obj = User(username = user_name,user_type = int(role))
        user_obj.set_password(password_1)
        user_obj.is_active = True
        user_obj.is_staff = True
        user_obj.save()
        return redirect('login')




class Add_Vehicle(View):
    def post(self,request):
        number = request.POST.get('number')
        types = request.POST.get('vehicle_type')
        try:
            types = Vehicle_Types.objects.get(id = types)
        except:
            types = None
        model = request.POST.get('vehicle_model')
        description = request.POST.get('description')
        
        vehicle_obj = Vehicle(
            number = number,
            type = types,
            model = model,
            decription = description
        )
        vehicle_obj.save()
        return JsonResponse({'message':"done"})

class get_vehicle_details(View):
    def get(self,request,id):
        vehicle_obj = Vehicle.objects.get(id=id)
        data = {'id':int(vehicle_obj.id),"number":vehicle_obj.number,"type":vehicle_obj.type.id,"model":vehicle_obj.model,"description":vehicle_obj.decription}
        return JsonResponse({'vehicle_obj':data})

class Edit_vehicle(View):
    def post(self,request):
        vehicle_id = request.POST.get('id')
        number = request.POST.get('number')
        vehicle_type = request.POST.get('vehicle_type')
        vehicle_model = request.POST.get('vehicle_model')
        description = request.POST.get('description')


        try:
            vehicletype = Vehicle_Types.objects.get(id=int(vehicle_type))
        except:
            vehicletype = None


        try:
            vehicle_obj = Vehicle.objects.get(id=int(vehicle_id))
            vehicle_obj.number = number
            vehicle_obj.type = vehicletype
            vehicle_obj.model = vehicle_model
            vehicle_obj.decription= description
            vehicle_obj.save()
            return JsonResponse({"status":"sucessfully updated"})
        except Exception as e:
            print(e)
            return JsonResponse({"status":"Something went wrong"})

class Delete_Vehicle(View):
    def post(self,request,id):
        vehicle_obj = Vehicle.objects.get(id=id)
        vehicle_obj.delete()
        return JsonResponse({"vehicle":"delete sucessFully!"})



class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')
