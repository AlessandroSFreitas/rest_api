from django.db import models


class Person(models.Model):
    RACES = (
        ('W', 'White'),
        ('BL', 'Black'),
        ('BR', 'Brown'),
        ('Y', 'Yellow'),
        ('O', 'Other'),
    )
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    first_name = models.CharField("person's first name", max_length=150)
    last_name = models.CharField("person's last name", max_length=150)
    age = models.IntegerField()
    nick_name = models.CharField(max_length=150, blank=True)
    father_name = models.CharField(max_length=150, blank=True)
    mother_name = models.CharField(max_length=150)
    weight = models.IntegerField() # peso
    height = models.IntegerField() # altura
    race = models.CharField(max_length=2, choices=RACES)
    another_race = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=2, choices=GENDERS)
    another_gender = models.CharField(max_length=50, blank=True)
    BloodType = models.TextChoices('BloodType', 'A+ B+ AB+ O+ A- B- AB- O-')
    blood_type = models.CharField(max_length=3, choices=BloodType.choices)
    family = models.ForeignKey(
        "family.Family", related_name='people', on_delete=models.CASCADE, blank=True, null=True
    )
