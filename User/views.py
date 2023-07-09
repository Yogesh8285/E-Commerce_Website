from django.shortcuts import render,redirect
from Admin.models import Category,Product,UserInfo,Recent,PaymentMaster
from .models import MyCart,OrderMaster,Account,Myorder
from django.contrib import messages
import base64
# Create your views here.

def homepage(request):
    try:
        uname = request.session["uname"]
    except:
        cats = Category.objects.all()
        prod = Product.objects.all()
        return render(request,'Homepage.html',{"cats":cats,"prod":prod})
    else:
        if(uname == "admin"):
            return render(request,"admin.html",{})
        else:
            cats = Category.objects.all()
            prod = Product.objects.all()
            return render(request,'Homepage.html',{"cats":cats,"prod":prod})

def myorders(request):
    cats = Category.objects.all()
    uname = request.session["uname"]
    user = UserInfo.objects.get(username = uname)
    cartitem = Myorder.objects.filter(user = user)
    total = 0
    for items in cartitem:
        total += items.qty * items.prod.price
    request.session["total"] = total
    return render(request,'myorders.html',{"items":cartitem,"cats":cats})



def Search(request):

    search = request.POST["search"]
    cats = Category.objects.all()
    # prod = Product.objects.filter(pname = search)
    prod = Product.objects.all()
    prds = []
    for p in prod:
        if(search.lower() in p.pname.lower()):
            # prds.append(p)
            prds += [p]
    if(len(prds) == 0):
        messages.success(request, "No product Found")
    return render(request,"Homepage.html",{"prod":prds,"cats":cats})

def login(request):
    cats = Category.objects.all()
    if(request.method == "GET"):
        return render(request,'login.html',{"cats":cats})

    else:
        uname = request.POST['uname']
        password = request.POST['pass']
        if('admin'== uname and 'admin'== password):
            try:
                user = UserInfo.objects.get(username=uname,password=password)
            except:
                a = "Invalid candidate plz check id or password..!"
                # messages.success(request, "Invalid candidate plz check id or password..!")
                return render(request,"login.html",{"a":a})
            else:
                request.session["uname"] = uname
                email = user.email
                request.session['email'] = email
                messages.success(request, "Admin Login Successfull")
                return render(request,"admin.html",{})
        else:
            try:
                encr_pass = base64.b85encode(password.encode('utf-8'))
                user = UserInfo.objects.get(username=uname,password=encr_pass)
            except:
                a = "Invalid candidate plz check id or password..!"
                # messages.success(request, "Invalid candidate plz check id or password..!")
                return render(request,"login.html",{"a":a})

            else:
                request.session["uname"] = uname
                email = user.email
                request.session['email'] = email
                messages.success(request, "Login Successfull")
                return redirect(homepage)

def signup(request):
    if(request.method =="GET"):
        cat = Category.objects.all()
        return render(request,'signup.html',{"cat":cat})
    else:
        uname = request.POST["uname"]
        password = request.POST["pass"]
        # For encript password
        encr_pass = base64.b85encode(password.encode('utf-8'))
        email = request.POST["email"]
        user = UserInfo(uname,encr_pass,email)
        user.save()
        return redirect(homepage)

def signout(request):
    request.session.clear()
    messages.success(request, "Signout Successfull")
    return redirect(homepage)

def viewDetails(request,id):
    cats = Category.objects.all()
    prod = Product.objects.get(id = id)
    return render(request,"viewDetails.html",{"prod":prod,"cats":cats})

def ShowCakes(request,id):
    id = Category.objects.get(id = id)
    prod = Product.objects.filter(cat = id)
    cats = Category.objects.all()
    return render(request,"Homepage.html",{"cats":cats,"prod":prod})

def addToCart(request):
    if(request.method == "POST"):
        if("uname" in request.session):
            # Add to Cart
            prodid = request.POST["prodid"]
            user = request.session["uname"]
            qty = request.POST["qty"]
            prod = Product.objects.get(id = prodid)
            user = UserInfo.objects.get(username = user)
            # check Duplicate entry
            try:
                cart = MyCart.objects.get(prod = prod,user=user)
            except:
                cart = MyCart()
                cart.user = user
                cart.prod = prod
                cart.qty = qty
                cart.save()
                messages.success(request, "Product added successfull")
            else:
                messages.success(request, "This  Product already in cart")
            return redirect(homepage)
        else:
            return redirect(login)

def ShowAllCartItems(request):
    if("uname" in request.session):
        cats = Category.objects.all()
        uname = request.session["uname"]
        user = UserInfo.objects.get(username = uname)
        if(request.method == "GET"):
            cartitem = MyCart.objects.filter(user = user)
            total = 0
            for items in cartitem:
                total += items.qty * items.prod.price
            request.session["total"] = total
            return render(request,'ShowAllCartItems.html',{"items":cartitem,"cats":cats})
        else:
            # Upadate product or Qty code
            prodid = request.POST['prodid']
            qty = request.POST['qty']
            prod = Product.objects.get(id = prodid)
            cart = MyCart.objects.get(prod = prod,user=user)
            cart.qty = qty
            cart.save()
            return redirect(ShowAllCartItems)
    else:
        return redirect(login)

def removeItem(request):
    # Remove product code
    uname = request.session["uname"]
    user = UserInfo.objects.get(username = uname)
    id = request.POST["prodid"]
    prod = Product.objects.get(id = id)
    item = MyCart.objects.get(user = user,prod = prod)
    item.delete()

    return redirect(ShowAllCartItems)

def profile(request):
    cats = Category.objects.all()
    if "uname" in request.session :
        user = request.session["uname"]
        id = UserInfo.objects.get(username=user)
        adds = Account.objects.filter(user = user)
        items = OrderMaster.objects.filter(user = id)
        orders = Myorder.objects.filter(user = user)
        return render(request,'profile.html',{"cats":cats,"adds":adds,"items":items,"orders":orders})
    else:
        return render(request,'profile.html',{"cats":cats})

def MakePayment(request):
    if(request.method == "GET"):
        return render(request,'MakePayment.html',{})
    else:
        cardno = request.POST["cardno"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        total = request.session["total"]
        try:
            buyer = PaymentMaster.objects.get(cardno = cardno,cvv=cvv,expiry=expiry)
        except:
            return redirect(MakePayment)
        else:
            ovner = PaymentMaster.objects.get(cardno='333',cvv='333',expiry='12/24')
            ovner.ballance += total
            buyer.ballance -= total
            ovner.save()
            buyer.save()

            # Maintain order statement
            uname = request.session["uname"]
            items = MyCart.objects.filter(user = uname)
            uid = UserInfo.objects.get(username = uname)
            prod_info =''
            qty = 0
            for item in items:
                qty += item.qty
                prod_info +=(item.prod.pname)+", "

                prodid = item.prod.id
                user = request.session["uname"]
                # qty = request.POST["qty"]
                prod = Product.objects.get(id = prodid)
                cart = Myorder()
                cart.user = user
                cart.prod = prod
                cart.qty = item.qty
                cart.amount = item.prod.price
                cart.save()
                item.delete()

            order = OrderMaster()
            order.user = uid
            order.details = prod_info
            order.qty = qty
            order.amount = total
            order.save()
            return render(request,"success.html",{})

def AddAddress(request):
    if "uname" in request.session :
        uname = request.session["uname"]
        name = request.POST["name"]
        mono = request.POST["mono"]
        house = request.POST["house"]
        pin = request.POST["pin"]
        city = request.POST["city"]
        state = request.POST["state"]
        id = UserInfo.objects.get(username=uname)
        add = Account()
        add.user = id
        add.name = name
        add.mono = mono
        add.house = house
        add.pin = pin
        add.city = city
        add.state = state
        add.save()
        return redirect(profile)
    else:
        return redirect(login)


def addremove(request):
    id = request.POST["addid"]
    add = Account.objects.get(id = id)
    add.delete()
    return redirect(profile)

def passwordchange(request):
    if("uname" in request.session):
        if(request.method == "GET"):
            return render(request,'password.html',{})
        else:
            uname = request.session["uname"]
            password = request.POST["pass"]
            p = UserInfo.objects.get(username = uname)
            p.password = password
            p.save()
            messages.success(request, "Password Change Successfully")
    return redirect(homepage)