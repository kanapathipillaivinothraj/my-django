# Generated by Django 4.1.4 on 2023-02-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detail_dataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No', models.IntegerField()),
                ('Name', models.CharField(max_length=255)),
                ('Address', models.TextField(max_length=255)),
                ('Image', models.ImageField(upload_to='')),
                ('Links', models.URLField(blank=True, null=True)),
                ('Salary', models.FloatField()),
            ],
        ),
    ]