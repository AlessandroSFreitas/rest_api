from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

from apps.family.models import Family
from apps.family.api.serializers import FamilySerializer


class FamilyViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FamilySerializer

    def get_queryset(self):
        return Family.objects.all()

    def get_object(self):
        family_id = self.kwargs['pk']
        return Family.objects.get(id=family_id)

    def create(self, request, *args, **kwargs):
        """Creates a Family."""
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as ex:
            # TODO: rever essa exception
            return Response(ex.errors, status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        """Returns the list of Families."""
        queryset = self.get_queryset()

        serializer = FamilySerializer(queryset, many=True)
        return Response({'results': serializer.data}, status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """Returns the details of a Family."""
        try:
            family = self.get_object()
        except ObjectDoesNotExist as ex:
            return Response({"result": ex.args[0]}, status.HTTP_404_NOT_FOUND)

        serializer = FamilySerializer(family)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, pk=None, *args, **kwargs):
        """Fully updates a Family."""
        partial = kwargs.pop("partial", False)
        family = self.get_object()
        serializer = self.get_serializer(family, data=request.data, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as ex:
            # TODO: rever essa exception
            return Response(ex.errors, status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status.HTTP_200_OK)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """Partially updates a Family."""
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Deletes a Family."""
        family = self.get_object()

        family.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
