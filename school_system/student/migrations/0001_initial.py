# Generated by Django 3.2.4 on 2021-09-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=20)),
                ('last_name', models.CharField(default=None, max_length=20)),
                ('age', models.PositiveSmallIntegerField(default=None)),
                ('date_of_birth', models.DateField(null=True)),
                ('student_id', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default=None, max_length=10, null=True)),
                ('nationality', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('course', models.CharField(blank=True, max_length=30, null=True)),
                ('admission_date', models.DateField(auto_now=True, null=True)),
                ('student_image', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('medical_report', models.FileField(blank=True, default=None, null=True, upload_to='files/')),
                ('student_phonenumber', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('class_name', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('academical_year', models.CharField(blank=True, default='2021', max_length=5, null=True)),
                ('gurdian_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('gurdian_phonenumber', models.CharField(blank=True, default=None, max_length=15, null=True)),
            ],
        ),
    ]
