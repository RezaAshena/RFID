from django.urls import path

from . import views
urlpatterns =[
    path('xml_rpc/',views.index)  #our domain.com/rpc
]