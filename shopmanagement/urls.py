from django.conf.urls import url

from shopmanagement import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^create',views.ItemCreate.as_view(),name="item-create"),
    url(r'^login/$',login,name = "shop-login"),
    url(r'^logout/$', logout,name = "shop-logout"),
    url(r'^list/$',views.ItemView.as_view(),name = "item-list"),
    url(r'^min_count/$',views.MinimumProductsView.as_view(),name = "item-minimum-list"),
    url(r'^update/(?P<pk>[0-9]+)',views.ItemUpdate.as_view(),name="item-update"),
    url(r'^details/(?P<pk>[0-9]+)', views.ItemDetailView.as_view(), name="item-details"),
    url(r'^delete/(?P<pk>[0-9]+)',views.ItemDeleteView.as_view(),name="item-delete"),
    url(r'^signup/$',views.adduser,name="signup-page"),
    url(r'^$',views.Home,name = "homepage")
]
