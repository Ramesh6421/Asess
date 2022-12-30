from django.shortcuts import render,redirect
from .models import RequesterModel,RiderModel 
from .forms import RiderForm,RequesterForm,UserRegistrationForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'myApp/base.html')

def rider(request):

    return render(request,'myApp/rider.html')

def rider_form(request):
    form = RiderForm()
    if request.method == 'POST':
        form = RiderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rider')

    context = {
        'form':form
    }
    return render(request,'myApp/riderform.html',context)


def requester(request):
    form = RequesterForm()
    if request.method == 'POST':
        form = RequesterForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {
        'form':form
    }
    return render(request,'myApp/requester.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created for {username}!!")
            return redirect("login")
    else:        
        form = UserRegistrationForm()
    context = {
        'form':form
        }
    return render(request,'myApp/register.html',context)

def matching(request):
    all_requests = RequesterModel.objects.filter(user_id = request.user)
    List=[]
    request_Ids = [i.user for i in all_requests]
    for each in all_requests:
        From = each.From
        To = each.To
        obj = RiderModel.objects.filter(From = From, To = To)
        List.append(obj)
    context = {
        'List':List,
        'request_Ids':request_Ids
    }
    return render(request,'myApp/match.html',context)    

def requests(request):
    all_requests = RequesterModel.objects.filter(user_id = request.user.id)
    context = {
        'all_requests':all_requests
    }
    return render(request,'myApp/requests.html',context)