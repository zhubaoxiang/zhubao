# Generated by Django 2.2 on 2019-05-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('content', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
                ('port', models.IntegerField()),
            ],
        ),
    ]
