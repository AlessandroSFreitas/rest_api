"""new_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.person.api.views import PersonViewSet
from apps.family.api.views import FamilyViewSet

urlpatterns = [
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