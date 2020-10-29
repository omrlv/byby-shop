from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .forms import FormReview
from .models import Review


# Create your views here.

def reviews(request):
    if request.method == 'POST':
        form = FormReview(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('reviews:reviews'))

    reviews = Review.objects.all()

    context = {
        'revs': reviews,
    }
    return render(request, 'reviews.html', context)


def leave_review(request):
    return render(request, 'leave_review.html')
