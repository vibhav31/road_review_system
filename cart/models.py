from django.db import models
from accounts.models import UserProfile
from road.models import Road
from django.db.models.signals import m2m_changed , pre_save
from decimal import Decimal
# Create your models here.
class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id" , None)
        qs = self.get_queryset().filter(id= cart_id)

        if qs.count() == 1 :
            new_obj = False
            cart_obj= qs.first()
            if request.session.get('username') is not None and cart_obj.user is None:
                try:
                    cart_obj.user=UserProfile.objects.get(email = request.session.get('username')).id
                except:
                    cart_obj.user = None
                cart_obj.save()
        else:
            try:
                user = UserProfile.objects.get(email = request.session.get('username'))
            except:
                user = None
            cart_obj = Cart.objects.new(request , user = user)
            new_obj=True

            request.session['cart_id'] = cart_obj.id
        return cart_obj , new_obj

    def new(self,request,user= None):
        user_obj = None
        if user is not None :
            if request.session.get('username'):
                user_obj = user
        return self.model.objects.create(user = user_obj)


class Cart(models.Model):
    user = models.ForeignKey(UserProfile , null = True , blank = True , on_delete = models.CASCADE)
    roads = models.ManyToManyField(Road,blank=True)
    subtotal = models.DecimalField(default=0.00,max_digits=100,decimal_places= 2 )
    total = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    updated_at = models.DateTimeField(auto_now= True)
    created_at = models.DateTimeField(auto_now_add= True)
    objects = CartManager()
    def __str__(self):
        return str(self.id)

def m2m_changed_cart_reciever(sender , instance , action , *args , **kwargs):
    if action=='post_add' or action=='post_remove' or action=='post_clear':
        roads= instance.roads.all()
        total = 0
        for road in roads:
            total = total + int(road.price)
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()
m2m_changed.connect(m2m_changed_cart_reciever,sender = Cart.roads.through)

def pre_save_cart_reciever(sender,instance,*args,**kwargs):
    if instance.subtotal > 0 :
        instance.total =  Decimal(instance.subtotal) * Decimal(1.10)
    else:
        instance.subtotal = 0.00
        instance.total = 0.00
pre_save.connect(pre_save_cart_reciever , sender = Cart)

