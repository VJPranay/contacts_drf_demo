from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from datarepo.views import ContactViewSet

router = DefaultRouter()

router.register('contacts', ContactViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
