from rest_framework import viewsets
from rest_framework import mixins
from .serializers import ContactSerializer
from .models import Contact


class ContactViewSet(mixins.CreateModelMixin,  # create  - post
                     mixins.ListModelMixin,  # list - get
                     mixins.UpdateModelMixin,  # update - put
                     mixins.RetrieveModelMixin,  # retrive - get
                     mixins.DestroyModelMixin,  # delete - delete
                     viewsets.GenericViewSet  # get the base layout
                     ):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
