# Generated by Django 3.2.7 on 2021-10-29 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name="person's first name")),
                ('last_name', models.CharField(max_length=150, verbose_name="person's last name")),
                ('age', models.IntegerField()),
                ('nick_name', models.CharField(blank=True, max_length=150)),
                ('father_name', models.CharField(blank=True, max_length=150)),
                ('mother_name', models.CharField(max_length=150)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('race', models.CharField(choices=[('W', 'White'), ('BL', 'Black'), ('BR', 'Brown'), ('Y', 'Yellow'), ('O', 'Other')], max_length=2)),
                ('another_race', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=2)),
                ('another_gender', models.CharField(blank=True, max_length=50)),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'Ab+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'Ab-'), ('O-', 'O-')], max_length=3)),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to='family.family')),
            ],
        ),
    ]