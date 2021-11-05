from django.contrib import admin
from django.urls import path, include
from apps.person.api.views import PersonViewSet
from apps.family.api.views import FamilyViewSet


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('person/', PersonViewSet.as_view({"get": "list", "post": "create"}), name="person-add"),
    path('person/<int:person_id>/', PersonViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="person-detail"
    ),
    path('family/', FamilyViewSet.as_view({"get": "list", "post": "create"}), name="family-add"),
    path('family/<int:family_id>/', FamilyViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="family-detail"
    ),
]
