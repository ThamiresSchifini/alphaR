from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from alphaR.planet.forms.planet_forms import PlanetForm
from alphaR.planet.models.planet import Planet


@csrf_exempt
def list_planets(request):
    """
    This view retrieves all planets from the database and paginates the results.
    :param request: The view expects a GET request and supports pagination using the 'page' query parameter.
    :return: A rendered response with the paginated planets.
    """
    planets_list = Planet.objects.all()
    paginator = Paginator(planets_list, 10)

    page_number = request.GET.get('page')
    planets = paginator.get_page(page_number)

    return render(request, 'alphaR/list_planets.html', {'planets': planets})


@csrf_exempt
def create_planet(request):
    """
    This view allows users to create a new planet by submitting a form. Upon successful form submission,
    the planet is saved to the database, and the user is redirected to the 'list_planets' view. If the
    form is invalid, an HTTP 400 Bad Request response is returned with an error message.
    :param request: The HTTP request object containing the form data.
    :return: The HTTP response containing the rendered 'alphaR/create_planet.html' template with the form.
    """
    form = PlanetForm(request.POST or None)
    if request.method == 'POST':
        form = PlanetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_planets')
        return HttpResponseBadRequest("Formulário inválido. Verifique os campos.")

    return render(request, 'alphaR/create_planet.html', {'form': form})


@csrf_exempt
def edit_planet(request, pk):
    """
    This view retrieves a specific planet from the database based on the provided `pk` (primary key) and
    allows users to edit the planet. If the request method is POST and the form is valid, the planet is
    updated in the database and the user is redirected to the 'list_planets' view. If the form is invalid,
    an HTTP 400 Bad Request response is returned with an error message.
    :param request: The HTTP request object.
    :param pk: The primary key of the planet to be edited.
    :return: The HTTP response containing the rendered 'alphaR/edit_planet.html' template with the form and planet data.
    """
    planet = get_object_or_404(Planet, pk=pk)
    form = PlanetForm(instance=planet)

    if request.method == 'POST':
        form = PlanetForm(request.POST, instance=planet)
        if form.is_valid():
            form.save()
            return redirect('list_planets')
        return HttpResponseBadRequest("Formulário inválido. Verifique os campos.")

    return render(request, 'alphaR/edit_planet.html', {'form': form, 'planet': planet})


@csrf_exempt
def delete_planet(request, pk):
    """
    This view retrieves a specific planet from the database based on the provided 'pk' (primary key) and
    allows users to delete the planet. If the request method is POST, the planet is deleted from the database
    and the user is redirected to the 'list_planets' view.
    :param request: The HTTP request object.
    :param pk: The primary key of the planet to be deleted.
    :return: The HTTP response containing the rendered 'alphaR/delete_planet.html' template with the planet details.
    """
    planet = get_object_or_404(Planet, pk=pk)
    if request.method == 'POST':
        planet.delete()
        return redirect('list_planets')

    return render(request, 'alphaR/delete_planet.html', {'planet': planet})

