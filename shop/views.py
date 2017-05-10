from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import User,Type_menu,Menu,Order_user,Order

def index(request):
    return render(request,'shop/index.html','')
def login(request):
    return render(request,'shop/login.html','')
def register(request):
    return render(request,'shop/register.html','')
def about(request):
    return render(request,'shop/about.html','')

def save_user(request):
    name_text = request.POST['name']
    phone_text = request.POST['phone']
    username_text = request.POST['username']
    password_text = request.POST['password']
    
    q=User(name=name_text,phone=phone_text,username=username_text,password=password_text)
    q.save()
    context = { 'name_text' : name_text,
                'phone_text' : phone_text,
                'username_text' : username_text,
                'password_text' : password_text,
              }
    return render(request,'shop/respone.html',context)

def check_user_login(request):
    u_text = request.POST['username']
    p_text = request.POST['password']
    check = False
    user = User.objects.filter(username=u_text,password=p_text)
    menu_list =  Type_menu.objects.all()
    order_list =  Order_user.objects.all()
    if(u_text == 'admin' and p_text == 'root'):
        context = { 'order_list' :order_list}
        return render(request,'shop/admin.html',context)      
    for u in user:
        if u != False:
             check = u
    if check !=False:
        context = { 'u_text' :u_text,'menu_list':menu_list}
         
        return render(request,'shop/home.html',context)
    else:
        context ={'error_message': "username หรือ password ของคุณไม่ถูกต้อง."}
        return render(request,'shop/login.html',context)
          


def select_item(request,u_text):
    location = request.POST['location']
    time = request.POST['time']
    type_all = Type_menu.objects.count()
    item = request.POST.getlist('checks[]')
    o=Order_user(Order_user_text=u_text,Delivery_location=location,time=time)
    o.save()
    for i in item :
        o.order_set.create(order_text=i)
    context = {'item':item,'u_text':u_text,'location':location,'time':time}
    return render(request,'shop/select_item.html',context)

def clear_order(request):
    Order_user.objects.all().delete()
    order_list =  Order_user.objects.all()
    context = { 'order_list' :order_list}
    return render(request,'shop/admin.html',context)
    
    

