from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.filters import OrderingFilter



# Django Rest Framework

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = (DjangoFilterBackend, OrderingFilter,)


class SymbolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = (DjangoFilterBackend, OrderingFilter,)


class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, OrderingFilter,)

    def get_queryset(self):
        return Entry.objects.filter(created_by=self.request.user).order_by('-pk')


# https://www.django-rest-framework.org/tutorial/3-class-based-views/

class APIDeleteEntries(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(id=self.request.data)
        self.check_object_permissions(self.request, obj)
        return obj

    # https://stackoverflow.com/questions/60833108/django-rest-framework-how-to-use-multiple-pks-in-url-with-class-based-views-ser
    # https://stackoverflow.com/questions/27535076/keyerror-id-when-trying-to-access-request-data-in-viewset-create-definition
    # def get_queryset(self):
    #     id = self.kwargs['id']
    #     return APIDeleteEntries.objects.filter(entry__id=id)

    def delete(self, request, *args, **kwargs):
        # # fetch ID's in post https://stackoverflow.com/questions/43859053/django-rest-framework-assertionerror-fix-your-url-conf-or-set-the-lookup-fi
        # queryset = self.filter_queryset(self.get_queryset())
        # obj = queryset.get(id=self.kwargs['id'])
        # # entry_ids = self.kwargs['id']
        return self.destroy(request, *args, **kwargs)

class EntryListAPIView(LoginRequiredMixin, generics.ListAPIView):
    # queryset = Entry.objects.all().order_by('-pk')
    serializer_class = EntrySerializer

    # pagination_class = dt_pagination.DatatablesLimitOffsetPagination

    # def post(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # serializer_class = EntrySerializer
    # # pagination_class = dt_pagination.DatatablesLimitOffsetPagination
    #
    def get_queryset(self):
        return Entry.objects.filter(created_by=self.request.user).order_by('-pk')
    #
    # def pre_save(self, request, obj):
    #     obj.owner = request.user
    #
    # def post(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)


class EntryDelete(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('entry-list')