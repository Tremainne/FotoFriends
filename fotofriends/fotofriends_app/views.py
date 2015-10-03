from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Image

def album(request, image_id)
    pic = get_object_or_404(Image, pk=image_id)
    try:
        selected_choice = pic.choice_set.get(pk=request.POST['Album']
    except (KeyError, Image.DoesNotExist):
        return render(request, 'home_page.html', {
            'error message': "No pictures available in this album.",
        })
    else:
        img = Image.open(
        img.show()
