from django.urls import path, re_path, include
from departments.views import index, view_with_name, view_with_int, view_with_slug, show_archive, redirect_to_softuni

urlpatterns = [
    path('', index, name='home'),
    path('softuni/', redirect_to_softuni),
    path('numbers/', include([
        path('<int:pk>/', view_with_int),
        path('<slug:slug>/', view_with_slug),
    ])),
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', show_archive),
    path('<variable>/', view_with_name),
    path('<path:variable>', view_with_name),
]