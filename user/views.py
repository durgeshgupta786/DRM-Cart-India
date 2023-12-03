from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime
from django.db import connection
#from django.http import HttpResponse
# Create your views here.
def index(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    x=category.objects.all().order_by('-id')[0:6]
    pdata=myproduct.objects.all().order_by('-id')[0:7]
    mdict={"data":x, "prodata":pdata,"cart":ct}
    return render(request, 'user/index.html',context=mdict)
######################################################
def about(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    return render(request, 'user/aboutus.html',{"cart":ct})
#######################################################
def product(request):
    return render(request, 'user/product.html')
#######################################################
def myorder(request):
    user=request.session.get('userid')
    oid=request.GET.get('oid')
    mydict={}
    if user:
        if oid is not None:
            morder.objects.all().filter(id=oid).delete()
            return HttpResponse("<script>alert('Your oder has been cancelled ');location.href='/user/myorder/'</script>")
        cursor=connection.cursor()
        cursor.execute("select p.*,o.* from user_myproduct p,user_morder o where p.id=o.pid and o.userid='"+str(user)+"' and o.remarks='Pending'  ")
        pdata=cursor.fetchall()
        cursor.execute("select p.*,o.* from user_myproduct p,user_morder o where p.id=o.pid and o.userid='"+str(user)+"' and o.remarks='Delivered'")
        ddata = cursor.fetchall()
        mydict={"pdata":pdata,"ddata":ddata}
    return render(request, 'user/myorder.html',mydict)
########################################################
def enquiry(request):
   mdict={}
   status=False
   if request.method=="post":
       a=request.POST.get("name")
       b=request.POST.get("mob")
       c=request.POST.get("email")
       d=request.POST.get("msg")
       contactus(Name=a,Mobile=b,Email=c,Message=d).save()
       mdict={"Name":a,"Mobile":b,"Email":c,"Message":d}
       status=True
   msg={"m":status}
   return render(request, 'user/enquiry.html',context=mdict,)

#######################################################
def myprofile(request):
    user=request.session.get('userid')
    x=""
    if user:
       if request.method=="POST":
           name=request.POST.get('name')
           mobile=request.POST.get('mob')
           email=request.POST.get('email')
           passwd=request.POST.get('passwd')
           upic=request.FILES.get('upic')
           message=request.POST.get('msg')
           uregister(email=user,mobile=mobile,name=name,passwd=passwd,userpic=upic,message=message).save()
           return HttpResponse("<script>alert('Your Profile Is Updated');location.href='/user/profile/'</script>")
       x=uregister.objects.all().filter(email=user)
    d={"mdata":x}
    return render(request,'user/myprofile.html',d)
#########################################################
def signin(request):
    if request.method=="POST":
        Email=request.POST.get('email')
        Passwd=request.POST.get('passwd')
        x=uregister.objects.all().filter(email=Email,passwd=Passwd).count()
        y=uregister.objects.all().filter(email=Email,passwd=Passwd)
        if x==1:
            request.session['userid']=Email
            request.session['userpic']=str(y[0].userpic)
            return HttpResponse("<script>alert('You are logged in ');location.href='/user/home/'</script>")

        else:
            return HttpResponse("<script>alert('Your userid or paasword is invalaid');location.href='/user/signin/'</script>")

    return render(request, 'user/signin.html')
#######################################################
def signup(request):
    status=False
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mob')
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        upic=request.FILES.get('upic')
        message=request.POST.get('msg')
        x=uregister.objects.all().filter(email=email).count()
        if x==0:
            uregister(name=name,mobile=mobile,email=email, passwd=passwd,userpic=upic,message=message).save()
            return HttpResponse("<script>alert('You are registered successfully');location.href='/user/signup/'</script>")
        else:
            return HttpResponse("<script>alert('Your email id is already register..');location.href='/user/signup/'</script>")
        status=True

    return render(request,'user/signup.html',context={"msg":status})
def mens(request):
    cid=request.GET.get('msg')
    cat=category.objects.all().order_by('-id')
    d=myproduct.objects.all()
    if cid is not None:
     d=myproduct.objects.all().filter(mcategory=1,pcategory=cid)
    mydict={"cats":cat,"data":d,"a":cid}
    return render(request, 'user/mens.html',mydict)
#######################################################
def womens(request):
    cid = request.GET.get('msg')
    cat = category.objects.all().order_by('-id')
    d = myproduct.objects.all().filter(mcategory=2)
    if cid is not None:
        d=myproduct.objects.all().filter(mcategory=2, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid}
    return render(request, 'user/womens.html',mydict)
############## #########################################
def kids(request):
    cid = request.GET.get('msg')
    cat = category.objects.all().order_by('-id')
    d = myproduct.objects.all().filter(mcategory=3)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=3, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid}
    return render(request, 'user/kids.html',mydict)
#######################################################
def viewproduct(request):
    a=request.GET.get('abc')
    x=myproduct.objects.all().filter(id=a)
    return render(request,'user/viewproduct.html',{"pdata":x})
################################################################

def signout(request):
    if request.session.get('userid'):
        del request.session['userid']
    return HttpResponse("<script>alert('You are Sign out !!');location.href='/user/index/'</script>")

def myordr(request):

    user=request.session.get('userid')
    pid=request.GET.get('msg')
    print(pid)
    print(user)

    if user:
        if pid is not None:
            morder(userid=user,pid=pid,remarks="Pending",odate=datetime.now().date(),status=True).save()
            return HttpResponse("<script> alert('Your oder is confirms');location.href='/user/index/'</script>")
    else:
        return HttpResponse("<script> alert('You have to login first..');location.href='/user/signin/'</script>)                                       </script>")
    return render(request,'user/myordr.html')

def mycart(request):
    p=request.GET.get('pid')
    user=request.session.get('userid')
    if user:
        if p is not None:
            mcart(userid=user,pid=p,cdate=datetime.now().date,status=True).save()
            return HttpResponse("<script>alert('Youe item is added to cart...');location.href='/user/index/'</script>")

    else:
        return HttpResponse("<script>alert('You have to login first');location.href='/user/signin/'</script>")

    return render(request,'user/mcart.html')

def showcart(request):
    userid = request.session.get('userid')
    md={}
    a=request.GET.get('msg')
    cid=request.GET.get('cid')
    pid=request.GET.get('pid')
    if userid:
        if a is not None:
           mcart.objects.all().filter(id=a).delete()
           return HttpResponse("<script>alert('Your item is deleted from the cart');location.href='/user/showcart/'</script>")
        elif pid is not None:
           mcart.objects.all().filter(id=cid).delete()
           morder(userid=userid,pid=pid,remarks="Pending",status=True,odate=datetime.now().date()).save()
           return HttpResponse("<script>alert('Yor oder has been placed successfully');location.href='/user/myorder/'</script>")
    cursor=connection.cursor()
    cursor.execute("select p.*,c.* from user_myproduct p, user_mcart c where p.id=c.pid and c.userid='"+str('user')+"'")
    cdata=cursor.fetchall()
    md={"cdata":cdata}
    return render(request,'user/showcart.html',md)

def cpdetail(request):
    c=request.GET.get('cid')
    if c is not None:
        p=myproduct.objects.all().filter(pcategory=c)
    return render(request, 'user/cpdetail.html',{"pdata":p})


