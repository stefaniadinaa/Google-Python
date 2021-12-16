from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView

from location.forms import LocationForm
from location.models import Location


class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    # fields = '__all__'
    # fields = ['city', 'country']
    form_class = LocationForm
    template_name = 'location/location_form.html'

    def get_success_url(self):
        return reverse('location:listare')

    def get_form_kwargs(self):
        data = super(CreateLocationView, self).get_form_kwargs()
        data.update({'pk': None})
        return data


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    # fields = '__all__'
    # fields = ['city', 'country']
    form_class = LocationForm
    template_name = 'location/location_form.html'

    def get_form_kwargs(self):
        data = super(UpdateLocationView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('location:listare')


class ListLocationView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'location/location_index.html'

    def get_queryset(self):
        return Location.objects.filter(active=1)

#verifica daca sunt autentificata
@login_required
def delete_location(request, pk):
    if request.user.is_authenticated:
        Location.objects.filter(id=pk).update(active=0)
    return redirect('location:listare')