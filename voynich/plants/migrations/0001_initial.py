# Generated by Django 3.1.3 on 2020-12-17 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('misc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=10)),
                ('page_image', models.ImageField(upload_to='')),
                ('svg', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Label', models.CharField(max_length=255)),
                ('plant_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.plant')),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('descr', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('real_image', models.ImageField(upload_to='')),
                ('medievial_image', models.ImageField(upload_to='')),
                ('person_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.person')),
                ('plant_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.plant')),
            ],
        ),
    ]