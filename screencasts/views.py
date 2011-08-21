"""Views for the screencast Django app."""

from django.shortcuts import render_to_response, redirect


def home(request):
    """Render the index page."""
    return render_to_response('index.html')


def about(request):
    """Render the about page."""
    return render_to_response('about.html')


def code(request):
    """Redirect to code repositories on Github."""
    return redirect('https://github.com/zachwill')


def donate(request):
    """Render donation page."""
    return render_to_response('donate.html')
