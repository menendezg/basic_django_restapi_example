from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from series import views

urlpatterns = {
    url(r'^series/$', views.CreateView.as_view(), name="create"),
    url(r'^series/(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name="details"),
 
}
urlpatterns = format_suffix_patterns(urlpatterns)