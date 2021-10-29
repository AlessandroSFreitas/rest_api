from apps.person.models import Person
from apps.person.api.serializers import PersonSerializer

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist


class PersonViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()

    def get_object(self):
        person_id = self.kwargs['person_id']
        return Person.objects.get(id=person_id)

    def create(self, request, *args, **kwargs):
        """Creates a Person."""
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as ex:
            return Response(ex.detail, status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        """Returns the list of Persons."""
        queryset = self.get_queryset()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """Returns the details of a Person."""
        try:
            person = self.get_object()
        except ObjectDoesNotExist as ex:
            return Response({"result": ex.args[0]}, status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(person)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """Fully updates a Person."""
        partial = kwargs.pop("partial", False)
        person = self.get_object()
        serializer = self.get_serializer(person, data=request.data, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as ex:
            return Response(ex.errors, status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status.HTTP_200_OK)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """Partially updates a Person."""
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Deletes a Person."""
        person = self.get_object()

        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
