from django.shortcuts import render

from road.models import Road,Review,SubCategory
from django.http import HttpResponse
from road.forms import ReviewForm
from django.core.paginator import Paginator
from cart.models import Cart

# Create your views here.


def roadpage(request):
    roads = Road.objects.all().order_by('subcategory_name')
    subcategory = SubCategory.objects.all()
    context = {'roads':roads , 'subcategory': subcategory}
    return render(request,'front/roadpage.html',context)

def home(request):
    return render(request,'front/home.html')
#converted road
def roaddetails(request,id):
    if 'username' not in request.session:
        form=ReviewForm(request.POST or None)
    else:
        form = ReviewForm(request.POST or None, initial = { 'reviewedby':request.session['username'], 'roadid':id})
    if request.method=="POST":
        if form.is_valid():
            reviewedby= form.cleaned_data.get('reviewedby')
            description=form.cleaned_data.get('description')

            review = Review(reviewedby=reviewedby,description=description,roadid= id)
            try:
                review.save()
            except:
                return redirect('/unsuccessful')
    try:
        road= Road.objects.get(id = id)
        reviews_list = Review.objects.filter(roadid = id)
        paginator = Paginator(reviews_list,11)
        page = request.GET.get('page')
        reviews = paginator.get_page(page)
     #cart part is left
        cart_obj, new_obj = Cart.objects.new_or_get(request)

        context={'title':'roaddetails',
                 'road':road,
                 'form':form,
                 'reviews': reviews,
                 'cart':cart_obj ,
                 }
        return render(request,'front/roaddetails.html',context)

    except:
        return HttpResponse("<h1>Road Not Found</h1>")


def roadcategory(request,id):
    roads = Road.objects.filter(subcategory_name = id)
    subcategory = SubCategory.objects.all()
    context = {'roads':roads , 'subcategory': subcategory}
    return render(request,'front/roadpage.html',context)
