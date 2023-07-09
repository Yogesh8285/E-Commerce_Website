from django.shortcuts import render,redirect
from Admin.models import Category,Product,UserInfo,Recent,PaymentMaster
from User.models import MyCart,OrderMaster,Account,Myorder
from .function import handle_uploaded_file

# Create your views here.

def dashboard(request):
    total = OrderMaster.objects.all()
    count = 0
    for i in total:
        count+=1

    user = UserInfo.objects.all()
    user_c = 0
    for i in user:
        user_c += 1

    cat = Category.objects.all()
    cat_c = 0
    for i in cat:
        cat_c += 1
    
    prod = Product.objects.all()
    prod_c = 0
    for i in prod:
        prod_c += 1

    return render(request,"dashbord.html",{"count":count,'user_c':user_c,'cat_c':cat_c,'prod_c':prod_c})
        
def category(request):
    cats = Category.objects.all()
    return render(request,"category.html",{"cats":cats})

def Addcategory(request):
    c = request.POST["cat_name"]
    cats = Category()
    cats.Category_name = c
    cats.save()
    return redirect(category)

def Removecat(request):
    catid = request.POST["catid"]
    cat = Category.objects.get(id = catid)
    cat.delete()
    return redirect(category)

def product(request):
    prod = Product.objects.all()
    return render(request,"product.html",{"prod":prod})

def editproduct(request):
    cats = Category.objects.all()
    try:
        id = request.POST["prodid"]
    except:
        return render(request, "editproduct.html",{"cats":cats})
    else:
        prod = Product.objects.get(id = id)
        # print(prod)      
        return render(request,"editproduct.html",{"cats":cats,"prod":prod})

def modifyproduct(request):
    pname =request.POST["pname"]
    price = request.POST["price"]
    description =request.POST["description"]
    size = request.POST["size"]
    qty = request.POST["qty"]
    cat = request.POST["cat"]
    handle_uploaded_file(request.FILES['image'])
    image = request.FILES["image"]
    print(image)
    try:
        id = request.POST["prodid"]
        prod = Product.objects.get(id = id)
    except:
        prod =Product()
    finally:
        prod.pname = pname
        prod.price = price
        prod.description = description
        prod.size = size
        prod.quantity = qty
        prod.image = image
        # foreign key can not assign directly it should fetch first
        cats = Category.objects.get(Category_name = cat)
        prod.cat= cats
        prod.save()
        return redirect(product)

def Removepro(request):
    id = request.POST["prodid"]
    prod = Product.objects.get(id = id)
    prod.delete()
    return redirect(product)

def user(request):
    user = UserInfo.objects.all()
    return render(request,"user.html",{"user":user})

def Removeuser(request):
    uname = request.POST["uname"]
    u = UserInfo.objects.get(username = uname)
    u.delete()
    return redirect(user)

def orders(request):
    orders = OrderMaster.objects.all()
    collection = 0
    for i in orders:
        collection += i.amount
    return render(request,"orders.html",{'orders':orders,"collection":collection})


