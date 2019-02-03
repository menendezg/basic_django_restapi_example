from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from series import views

urlpatterns = {
    url(r'^series/$', views.CreateView.as_view(), name="create"),
}
urlpatterns = format_suffix_patterns(urlpatterns)