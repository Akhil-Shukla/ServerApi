from . import views
from .views import *
from rest_framework import routers
from django.conf.urls import url,include

router=routers.DefaultRouter()
router.register(r'products', ProductViewSet)


urlpatterns=[
    url('index/',views.index),
    url(r'^test/',views.test),
    url(r'^api/', include(router.urls)),
    url(r'^api/brands/',BrandViewSet),
]