from django.shortcuts import render, redirect
from django.contrib import messages
from Shoes.models import registeration_data, category_data, product_data, contact_data
from django.shortcuts import render
from ShoesWebpage.models import customerdetails, cartdb

# Create your views here.
def mainpage(request):
    details = category_data.objects.all()
    return render(request,"home_Page.html",{'details':details})
def contactpage(request):
    return render(request,"Contact_page.html")
def contact_save(request):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('mail')
        sb = request.POST.get('sub')
        ms = request.POST.get('message')

        obj = contact_data(name=na, email=em, subject=sb, message=ms)
        obj.save()
        return redirect(contactpage)
def contactview(request):
    details = contact_data.objects.all()
    return render(request,"contact_Details.html",{'details':details})
def Allproduct(request):
    details = product_data.objects.all()
    return render(request, "Products.html", {'details': details})
def singleproduct(request, itemcatg):
    data = category_data.objects.all()
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    details = product_data.objects.filter(category=itemcatg)
    context = {
        'details': details,
        'catg': catg,
        'data': data
    }
    return render(request, "display_Category_Product.html", context)
def prodetails(request, dataid):
    details = product_data.objects.get(id=dataid)
    return render(request,"Display_Single_Product.html", {"details":details})
def login(request):
    return render(request,"Customer_login.html")
def loginsave(request):
    if request.method=="POST":
        u = request.POST.get('name')
        e = request.POST.get('mail')
        p = request.POST.get('pass')
        c = request.POST.get('cpass')
        if p == c:
            obj = customerdetails(username=u,email=e,password=p,confirmpassword=c)
            obj.save()
            messages.success(request,"User Register Successfully")
            return redirect(login)
        else:
            messages.warning(request,"Sorry.... Invalid Username Or Password")
            return render(request,'Customer_login.html',{'msg':"Sorry......password not matched "})
def customerlogin(request):
    if request.method == "POST":
        u = request.POST.get('name')
        p = request.POST.get('pass')
        if customerdetails.objects.filter(username=u, password=p).exists():
            data = customerdetails.objects.filter(username=u, password=p).values('id').first()
            # obj = LoginRegister(username=u, password=p).values('email','id').first()
            request.session['name']=u
            request.session['pass']=p
            request.session['userid']=data['id']
            messages.success(request,"User Login successfully")
            # request.session['email']=data['email']
            # request.session['userid']=data['id']
            return redirect(mainpage)
        else:

            messages.warning(request,"Sorry.... Invalid Username Or Password")
            return render(request, 'Customer_login.html', {'msg': "Sorry... password not correct."})
def logoutfn(request):
    del request.session['name']
    del request.session['pass']
    return redirect(mainpage)
def cart(request):
    da = category_data.objects.all()
    data = cartdb.objects.all()
    return render(request, 'Cart_Product.html', {'data': data, 'da': da})
def cartview(request):
    if request.method=="POST":
        na=request.POST.get('name')
        rs=request.POST.get('price')
        qt=request.POST.get('quantity')
        sz=request.POST.get('size')
        to=request.POST.get('totalprice')

        obj=cartdb(name=na, price=rs, quantity=qt, size=sz, total=to)
        obj.save()
    return redirect(cart)
def deleteitem(request,dataid):

    data=cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cart)


