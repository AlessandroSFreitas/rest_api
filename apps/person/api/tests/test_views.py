import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.person.models import Person
from django.contrib.auth.models import User


class TestCreatePerson(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test")
        cls.url = reverse("person-add")
        cls.payload = {
            "first_name": "Leandro",
            "last_name": "Santos",
            "age": 19,
            "mother_name": "Maria Santos",
            "weight": 79,
            "height": 175,
            "race": "W",
            "gender": "M",
            "blood_type": "A-",
            "family_id": None
        }

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_create_person(self):
        response = self.client.post(self.url, data=self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().first_name, 'Leandro')


class TestUpdatePerson(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test")
        Person.objects.create(
            first_name="Leandro",
            last_name="Santos",
            age=19,
            mother_name="Maria Santos",
            weight=79,
            height=175,
            race="W",
            gender="M",
            blood_type="A-"
        )

        person = Person.objects.first()

        cls.url = reverse("person-detail", kwargs={"person_id": person.id})
        cls.payload = {
            "id": person.id,
            "first_name": "Leandro",
            "last_name": "Santos",
            "age": 19,
            "mother_name": "Maria Santos Silva",
            "weight": 79,
            "height": 175,
            "race": "W",
            "gender": "M",
            "blood_type": "A-"
        }

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_update_person(self):
        response = self.client.put(self.url, data=self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPartialUpdatePerson(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test")
        Person.objects.create(
            first_name="Leandro",
            last_name="Santos",
            age=19,
            mother_name="Maria Santos",
            weight=79,
            height=175,
            race="W",
            gender="M",
            blood_type="A-"
        )

        person = Person.objects.first()

        cls.url = reverse("person-detail", kwargs={"person_id": person.id})
        cls.payload = {"mother_name": "Maria Santos Silva"}

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_partial_update_person(self):
        response = self.client.patch(
            self.url, data=self.payload, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Person.objects.get().mother_name, 'Maria Santos Silva'
        )


class TestDeletePerson(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test")
        Person.objects.create(
            first_name="Leandro",
            last_name="Santos",
            age=19,
            mother_name="Maria Santos",
            weight=79,
            height=175,
            race="W",
            gender="M",
            blood_type="A-"
        )

        person = Person.objects.first()

        cls.url = reverse("person-detail", kwargs={"person_id": person.id})

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_delete_person(self):
        response = self.client.delete(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)


class TestRetrievePerson(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test")
        Person.objects.create(
            first_name="Leandro",
            last_name="Santos",
            age=19,
            mother_name="Maria Santos",
            weight=79,
            height=175,
            race="W",
            gender="M",
            blood_type="A-"
        )

        person = Person.objects.first()

        cls.url = reverse("person-detail", kwargs={"person_id": person.id})

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_retrieve_person(self):
        response = self.client.get(self.url, format='json')

        person = Person.objects.get()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(person.first_name, 'Leandro')
        self.assertEqual(person.last_name, 'Santos')


class TestListPerson(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test")
        Person.objects.create(
            first_name="João",
            last_name="Oliveira",
            age=65,
            mother_name="Silvia Oliveira",
            weight=85,
            height=171,
            race="B",
            gender="M",
            blood_type="O-"
        )
        Person.objects.create(
            first_name="Leandro",
            last_name="Santos",
            age=19,
            mother_name="Maria Santos",
            weight=79,
            height=175,
            race="W",
            gender="M",
            blood_type="A-"
        )
        cls.url = reverse("person-add")

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_list_person(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.count(), 2)
