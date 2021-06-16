from django.conf.urls import url
from examples import views

urlpatterns = [
    url(r'^api/examples$', views.example_list),
    url(r'^api/examples/(?P<pk>[0-9]+)$', views.example_detail),
    url(r'^api/examples/published$', views.example_list_published)
    ]
