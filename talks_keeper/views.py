from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Country, Company, Talk


# -------------------------------------------------------------------
class CountryList(ListView):
    model = Country
    context_object_name = "countries"


class CountryCreate(CreateView):
    model = Country


class CountryDetail(DetailView):
    model = Country
    context_object_name = "country"

    def get_context_data(self, **kwargs):
        context = super(CountryDetail, self).get_context_data(**kwargs)
        country = Country.objects.filter(pk=self.kwargs['pk'])
        context["companies"] = Company.objects.filter(country=country)
        return context


class CountryUpdate(UpdateView):
    model = Country


class CountryDelete(DeleteView):
    model = Country
    succes_url = reverse_lazy("country_list")


# -------------------------------------------------------------------
class CompanyList(ListView):
    model = Company
    context_object_name = "companies"


class CompanyCreate(CreateView):
    model = Company


class CompanyDetail(DetailView):
    model = Company
    context_object_name = "company"

    def get_context_data(self, **kwargs):
        context = super(CompanyDetail, self).get_context_data(**kwargs)
        company = Company.objects.filter(pk=self.kwargs['pk'])
        context["talks"] = Talk.objects.filter(company=company)
        return context


class CompanyUpdate(UpdateView):
    model = Company


class CompanyDelete(DeleteView):
    model = Company
    succes_url = reverse_lazy("company_list")


# -------------------------------------------------------------------
class TalkCreate(CreateView):
    model = Talk


class TalkDetail(DetailView):
    model = Talk
    context_object_name = "talk"


class TalkUpdate(UpdateView):
    model = Talk


class TalkDelete(DeleteView):
    model = Talk
    succes_url = reverse_lazy("talk_detail")
