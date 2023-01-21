from django.contrib.auth import  authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from Shoes.models import registeration_data, category_data,product_data
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def indexpage(request):
    return render(request,"index.html")
def Adminpage(request):
    return render(request,"Add_admin.html")
def Admin_save(request):
    if request.method=="POST":
        na = request.POST.get('name')
        mb = request.POST.get('mobile')
        un = request.POST.get('name2')
        em = request.POST.get('mail')
        pa = request.POST.get('pass')
        cp = request.POST.get('cpass')
        im = request.FILES['img[]']
        obj = registeration_data(name=na, mobile=mb, email=em,image=im, username=un, password=pa, confirmpassword=cp)
        obj.save()
        return redirect(Adminpage)
def Admindata(request):
    details = registeration_data.objects.all()
    return render(request, "Admindetail.html", {'details': details})
def editAdmindata(request,dataid):
    details= registeration_data.objects.get(id=dataid)
    print(details)
    return render(request,"Edit_admin.html",{'details':details})
def updateAdmin(request, dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        mb = request.POST.get('mobile')
        un = request.POST.get('name2')
        em = request.POST.get('mail')
        pa = request.POST.get('pass')
        cp = request.POST.get('cpass')
        try:
            img = request.FILES['img[]']
            fs = FileSystemStorage()
            im = fs.save(img.name, img)
        except MultiValueDictKeyError:
            im=registeration_data.objects.get(id=dataid).image
        registeration_data.objects.filter(id=dataid).update(name=na, mobile=mb, username=un, email=em, password=pa, confirmpassword=cp, image=im)
        return redirect(Admindata)
def deleteAdminData(request, dataid):
    data = registeration_data.objects.filter(id=dataid)
    data.delete()
    return redirect(Admindata)
def category(request):
    return render(request,"Addcategory.html")
def categoryitem(request):
    if request.method=="POST":
        na = request.POST.get('name')
        ds = request.POST.get('content')
        im = request.FILES['img[]']
        obj = category_data(name=na, content=ds, image=im)
        obj.save()
        return redirect(category)
def items(request):
    details = category_data.objects.all()
    return render(request, "Category_Data.html", {'details': details})
def edititems(request,dataid):
    details= category_data.objects.get(id=dataid)
    print(details)
    return render(request,"Edit_Category.html",{'details':details})
def updatecategory(request, dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        ds = request.POST.get('content')
        try:
            img = request.FILES['img[]']
            fs = FileSystemStorage()
            im = fs.save(img.name, img)
        except MultiValueDictKeyError:
            im=category_data.objects.get(id=dataid).image
        category_data.objects.filter(id=dataid).update(name=na, content=ds, image=im,)
        return redirect(items)
def deledata(request, dataid):
    data = category_data.objects.filter(id=dataid)
    data.delete()
    return redirect(items)
def adproduct(request):
    details=category_data.objects.all()
    return render(request, "AddProduct.html",{'details':details})
def products(request):
    if request.method=="POST":
        cat = request.POST.get('cat')
        na = request.POST.get('name')
        rs = request.POST.get('price')
        sz = request.POST.get('size')
        qn = request.POST.get('quantity')
        ds = request.POST.get('content')
        im = request.FILES['img[]']
        obj = product_data(category=cat,name=na, price=rs, size=sz, quantity=qn, descrption=ds, image=im)
        obj.save()
        return redirect(adproduct)
def productview(request):
    details = product_data.objects.all()
    return render(request,"Display_Product.html",{'details':details})
def editproduct(request,dataid):
    details= product_data.objects.get(id=dataid)
    da = category_data.objects.all()
    return render(request,"Edit_Product.html",{'details':details, 'da':da})
def updateproduct(request, dataid):
    if request.method=="POST":
        cat = request.POST.get('cat')
        na = request.POST.get('name')
        rs = request.POST.get('price')
        sz = request.POST.get('size')
        qn = request.POST.get('quantity')
        ds = request.POST.get('content')
        try:
            img = request.FILES['img[]']
            fs = FileSystemStorage()
            im = fs.save(img.name, img)
        except MultiValueDictKeyError:
            im=product_data.objects.get(id=dataid).image
        product_data.objects.filter(category=cat,name=na, price=rs, size=sz, quantity=qn, descrption=ds, image=im)
        return redirect(productview)
def deleproduct(request, dataid):
    data = product_data.objects.get(id=dataid)
    data.delete()
    return redirect(productview)
def loginadmin(request):
    return render(request,"Admin_Login.html")
def loginpage(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(loginadmin)
        else:
            return redirect(loginadmin)
def customerlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginadmin)
