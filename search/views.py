from django.shortcuts import render
from road.models import SubCategory,Road
from django.db.models import Q

# Create your views here.4
def search(request):
    method_dict = request.GET
    query = method_dict.get('search')
    subcategory = SubCategory.objects.all()

    if query is not None:
        lookups = (Q (description__icontains = query) |
                   Q (brand_name__brand_name__icontains = query) |
                   Q (title__icontains = query))
        road = Road.objects.filter(lookups , active=True).distinct
        context = { 'roads':road, 'subcategory':subcategory}
    else:
        road = Road.objects.all()
        context = {'roads': road, 'subcategory': subcategory}
    return render(request, 'front/roadpage.html', context)