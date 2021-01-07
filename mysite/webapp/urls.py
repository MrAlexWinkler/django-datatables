from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    #Entry
    # path('entry/', EntryListView.as_view(), name="import-entry"),
    path('entry/', APIDeleteEntries.as_view(), name="import-entry"),

    # DRF API Custom Endpoints
    path('api/delete-entries/', APIDeleteEntries.as_view(), name="delete-entries"),

]

urlpatterns += format_suffix_patterns(urlpatterns)