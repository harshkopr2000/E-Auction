from django.urls import path

from . import views

urlpatterns = [
    path("", views.userhome),
    path("funds/", views.funds),
    path("payment/", views.payment),
    path("success/", views.success),
    path("cancel/", views.cancel),
    path("cpuser/",views.cpuser),
    path("epuser/",views.epuser),
    path("searchcat/",views.searchcat),
    path("searchsubcat/",views.searchsubcat), 
    path("searchproduct/",views.searchproduct),
    path("bidstatus/",views.bidstatus)
]
