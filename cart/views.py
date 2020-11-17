from django.shortcuts import render,redirect
from .models import Cart, CartManager
from road.models import Road
from accounts.forms import LoginForm,GuestForm
from billing.models import BillingProfile
# Create your views here.
def cart(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    print( request.session.get('cart_id'))
    context = {'cart': cart_obj}

    return render(request,'cart/cart.html',context)
def cartupdate(request):
    road_id = request.POST.get('road_id')
    print(road_id)
    if road_id is not None:
        try:
            road_obj = Road.objects.get(id = road_id)
        except Road.DoesNotExist :
            print("This Road Does Not Exist")
            return redirect('/cart')
        cart_obj , new_obj = Cart.objects.new_or_get(request)
        if road_obj in cart_obj.roads.all():
            cart_obj.roads.remove(road_obj)
        else:
            cart_obj.roads.add(road_obj)
        request.session['cart_items']= cart_obj.roads.count()

    return redirect('/cart')
def checkout(request,):
    cart_obj , cart_created = Cart.objects.new_or_get(request)
    next_url= request.build_absolute_uri
    print(next_url)
    order_obj = None
    if cart_created or cart_obj.roads.count() == 0 :
        return redirect('/cart')

    loginform = LoginForm()
    guestform = GuestForm()
    billing_profile,billing_profile_created = BillingProfile.objects.new_or_get(request)
    context = { 'loginform': loginform,
                'guestform':guestform,
                'billing_profile':billing_profile,
                'next_url':next_url,}
    return render(request,'cart/checkout.html',context)