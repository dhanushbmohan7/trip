from django.shortcuts import render
from . models import profiles
from django.db.models import Sum

# Create your views here.
def index(request):
    data=profiles.objects.all()
    total_recieved=profiles.objects.all().aggregate(Sum('amount_paid'))
    total_pending=profiles.objects.all().aggregate(Sum('amount_balance'))
    balance=total_recieved['amount_paid__sum']-500


    return render(request,'index.html',{'data':data,'total_recieved':total_recieved['amount_paid__sum'],'total_pending':total_pending['amount_balance__sum'],'balance':balance})
