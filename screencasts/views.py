"""Views for the screencast Django app."""

from django.shortcuts import render_to_response, redirect, get_object_or_404
from screencasts.models import Screencast


def home(request):
    """Render the index page."""
    screencasts = Screencast.objects.order_by('-date')[:5]
    context = {'screencasts': screencasts}
    return render_to_response('index.html', context)


def about(request):
    """Render the about page."""
    return render_to_response('about.html')


def code(request):
    """Redirect to code repositories on Github."""
    return redirect('https://github.com/zachwill')


def donate(request):
    """Render donation page."""
    return render_to_response('donate.html')


def screencast(request, slug):
    """Return a specific screencast given a slug."""
    specific_screencast = get_object_or_404(Screencast, slug=slug)
    context = {'screencast': specific_screencast}
    return render_to_response('screencast.html', context)
