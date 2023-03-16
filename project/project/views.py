from django.shortcuts import render
from flask import redirect

from contact .models import Contact

from  bizcontact .models import BizContact
from biz .models import BizCont
from . import views




def index(request):
    return render(request, 'front/index.html')



      
def contact(request):
    #url= 'https://realpython.com/django-redirects/'
    if request.method == 'POST':
        name = request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        if name =='' or email =='' or phone=='':
            msg = 'please fill all the field'
            
        b = Contact(name=name, email=email,phone=phone)
        b.save()
    else:
        msg = 'pls fill right inforation'
        return render(request, 'front/error.html')

        

    #return redirect(url)
    return render(request, 'front/check.html')


def mtcontact(request):
    mtdata = Contact.objects.all()
    if request.method =='POST':
        srch = request.POST.get('top-search')
        if srch!=None:
            mtdata = Contact.objects.filter(phone__icontains=srch)
        

   
    return render(request,'back/mtcontact.html',{'mtdata':mtdata})



def adminpanel(request):
    return render(request,'back/admin.html')









def adminpanel(request):
    return render(request,'back/admin.html')











def index2(request):
    return render(request, 'front/index2.html')
    


def contact2(request):
    #url= 'https://realpython.com/django-redirects/'
    if request.method == 'POST':
        bizname = request.POST.get('bizname')
        bizemail =request.POST.get('bizemail')
        bizphone =request.POST.get('bizphone')
        if bizname =='' or bizemail =='' or bizphone=='':
            bizlist = 'please fill all the field'
            
        data = BizContact(bizname=bizname, bizemail=bizemail,bizphone=bizphone)
        data.save()
    else:
        bizlist = 'pls fill right inforation'
        return render(request, 'front/error.html')
    
    return render(request, 'front/check.html')
def bizcontact(request):
    bizdata = BizContact.objects.all()
    if request.method =='POST':
        srch2 = request.POST.get('top-search')
        if srch2!=None:
            bizdata = BizContact.objects.filter(bizphone__icontains=srch2)
            
        

   
    return render(request,'back/bizcontactlist.html',{'bizdata':bizdata})





