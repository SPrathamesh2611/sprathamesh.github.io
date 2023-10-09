# Generated by Django 4.2.1 on 2023-09-25 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='static/skills', verbose_name='Logo_Image')),
                ('name', models.CharField(max_length=15, verbose_name='name')),
                ('level', models.CharField(max_length=50, verbose_name='level')),
            ],
        ),
    ]
