from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse

from .models import Country, Company, Talk


# -------------------------------------------------------------------
class CountryList(ListView):
    model = Country
    context_object_name = "countries"


class CountryCreate(CreateView):
    model = Country
    fields = ['name']


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
    fields = ['short_name', 'full_name']

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        country_pk = self.kwargs['country_pk']
        form.instance.country = Country.objects.filter(pk=country_pk).first()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_initial(self):
        country_pk = self.kwargs['country_pk']
        return {'country': Country.objects.filter(pk=country_pk).first()}


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
    fields = ['date', 'source_info', 'talk_details', 'is_our_talk']

    def post(self, request, *args, **kwargs):
        company_pk = self.kwargs['company_pk']
        self.success_url = reverse('company_detail',
                                   kwargs={'pk': int(company_pk)})

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.instance.company = Company.objects.filter(pk=company_pk).first()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_initial(self):
        company_pk = self.kwargs['company_pk']
        return {'company': Company.objects.filter(pk=company_pk).first()}


class TalkDetail(DetailView):
    model = Talk
    context_object_name = "talk"


class TalkUpdate(UpdateView):
    model = Talk


class TalkDelete(DeleteView):
    model = Talk
    succes_url = reverse_lazy("talk_detail")
