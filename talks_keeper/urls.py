from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [

    url(r'^$',
        login_required(views.CountryList.as_view()),
        name="country_list"),
    url(r'^country/detail/(?P<pk>\d+)/',
        login_required(views.CountryDetail.as_view()),
        name="country_detail"),
    url(r'^country/create/',
        login_required(views.CountryCreate.as_view()),
        name="country_create"),
    url(r'^country/update/(?P<pk>\d+)/',
        login_required(views.CountryUpdate.as_view()),
        name="country_update"),
    url(r'^country/delete/(?P<pk>\d+)/',
        login_required(views.CountryDelete.as_view()),
        name="country_delete"),

    url(r'^company/list',
        login_required(views.CompanyList.as_view()),
        name="company_list"),
    url(r'^company/detail/(?P<pk>\d+)/',
        login_required(views.CompanyDetail.as_view()),
        name="company_detail"),
    url(r'^company/create/(?P<country_pk>\d+)/',
        login_required(views.CompanyCreate.as_view()),
        name="company_create"),
    url(r'^company/update/(?P<pk>\d+)/',
        login_required(views.CompanyUpdate.as_view()),
        name="company_update"),
    url(r'^company/delete/(?P<pk>\d+)/',
        login_required(views.CompanyDelete.as_view()),
        name="company_delete"),

    url(r'^talk/detail/(?P<pk>\d+)/',
        login_required(views.TalkDetail.as_view()),
        name="talk_detail"),
    url(r'^talk/create/(?P<company_pk>\d+)/',
        login_required(views.TalkCreate.as_view()),
        name="talk_create"),
    url(r'^talk/update/(?P<pk>\d+)/',
        login_required(views.TalkUpdate.as_view()),
        name="talk_update"),
    url(r'^talk/delete/(?P<pk>\d+)/',
        login_required(views.TalkDelete.as_view()),
        name="talk_delete"),

]
