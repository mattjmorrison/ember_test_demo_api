from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from developers.views import Developers

router = DefaultRouter(trailing_slash=False)
router.register('developers', Developers, base_name='developer')

urlpatterns = router.urls
urlpatterns += [
    path('admin/', admin.site.urls),
]
