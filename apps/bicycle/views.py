from django.shortcuts import render, get_object_or_404

from .models import Bicycle

# Create your views here.
def bicycle_detail_all(request):
    all_bikes = Bicycle.objects.all()

    context = {
        'bikes': all_bikes,
    }

    return render(request, 'detail_all/detail_all.html', context)

def bicycle_detail_single(request, id):
    bike = Bicycle.objects.get(id=id)

    return render(request, 'detail_single/detail_single.html', {'bike': bike})