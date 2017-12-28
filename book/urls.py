from django.conf.urls import url
from .views import (
    BookAddView,
    BookEditView,
    BookDeleteView
)

urlpatterns = [
    url(r'^add/$', BookAddView.as_view(), name='addbook'),
    url(r'^edit/(?P<fid>[\w.@+-]+)/$', BookEditView.as_view(), name='editbook'),
    url(r'^delete/(?P<fid>[\w.@+-]+)/$', BookDeleteView.as_view(), name='editbook'),
]