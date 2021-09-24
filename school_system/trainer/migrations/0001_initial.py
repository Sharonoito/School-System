# Generated by Django 3.2.4 on 2021-09-24 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=12)),
                ('last_name', models.CharField(default=None, max_length=20)),
                ('course', models.CharField(default=None, max_length=20)),
                ('email', models.EmailField(default=0, max_length=254)),
                ('national_id', models.CharField(default=None, max_length=15)),
                ('contract', models.FileField(default=None, upload_to='files/')),
                ('resume', models.FileField(default=None, upload_to='files/')),
                ('salary', models.PositiveBigIntegerField(default=None)),
                ('trainer_image', models.ImageField(default=None, upload_to='images/')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default=None, max_length=10)),
                ('phonenumber', models.CharField(default=None, max_length=15)),
                ('syllabus_relationship', models.CharField(default=None, max_length=20)),
                ('course_name', models.CharField(default=None, max_length=20)),
                ('course_code', models.CharField(default=None, max_length=5)),
                ('company', models.CharField(default=None, max_length=20)),
                ('joining_date', models.DateField(default=None)),
            ],
        ),
    ]
