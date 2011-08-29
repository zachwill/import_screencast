"""Views for the screencast Django app."""

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from screencasts.models import Screencast


def home(request, page_num=1):
    """Render the index page."""
    screencast_list = Screencast.objects.order_by('-date').all()
    pagination = Paginator(screencast_list, 3)
    try:
        screencasts = pagination.page(page_num)
    except PageNotAnInteger:
        screencasts = pagination.page(1)
    except EmptyPage:
        screencasts = pagination.page(pagination.num_pages)
    context = {'screencasts': screencasts}
    return render_to_response('index.html', context)


def about(request):
    """Render the about page."""
    return render_to_response('about.html')


def code(request):
    """Redirect to code repositories on Github."""
    return redirect('https://github.com/zachwill')


def screencast(request, slug):
    """Return a specific screencast given a slug."""
    specific_screencast = get_object_or_404(Screencast, slug=slug)
    context = {'screencast': specific_screencast}
    return render_to_response('screencast.html', context)
