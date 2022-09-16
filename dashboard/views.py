from django.shortcuts import render
from django.contrib.auth import get_user_model
from furn.models import Product, Blog, Arrival , Contact
from django.utils import timezone

today = timezone.now().today()

User = get_user_model()

def dashboard_home(request):
    if 'q' in request.GET:
        search = request.GET['q']
        full_search = Q(Q(title__icontains=search))
        products = Product.objects.filter(full_search)
    else:
        products = Product.objects.all()
        
    users = User.objects.count()
    blogs = Blog.objects.count()
    new_products = Arrival.objects.count()
    products = Product.objects.count() + new_products
    contact = Contact.objects.count()
    contact_taklif = Contact.objects.filter(choices="Taklif").count()
    contact_shikoyat = Contact.objects.filter(choices="Shikoyat").count()
    
    #contact last get
    contact_last = Contact.objects.filter(date__date=timezone.now()).count()
    
    context = {
        "blogs": blogs,
        "users": users,
        "products": products,
        "new_products": new_products,
        "contact": contact,
        "contact_taklif": contact_taklif,
        "contact_shikoyat": contact_shikoyat,
        "contact_last": contact_last
    }
    return render(request, 'dashboard/pages/home.html', context)

def buttons(request):
    return render(request, 'dashboard/includes/buttons.html')

def cards(request):
    return render(request, 'dashboard/includes/cards.html')

def animation(request):
    return render(request, 'dashboard/includes/animation.html')

def colors(request):
    return render(request, 'dashboard/includes/colors.html')

def border(request):
    return render(request, 'dashboard/includes/border.html')

def other(request):
    return render(request, 'dashboard/includes/other.html')

def dashboard_login(request):
    return render(request, 'dashboard/registertration/login.html')

def forgot_password(request):
    return render(request, 'dashboard/includes/forgot-password.html')

def register(request):
    return render(request, 'dashboard/registertration/register.html')

def charts(request):
    return render(request, 'dashboard/includes/charts.html')

def tables(request):
    return render(request, 'dashboard/includes/tables.html')

def page_404(request):
    return render(request, 'dashboard/includes/404.html')

def blank(request):
    return render(request, 'dashboard/includes/blank.html')
