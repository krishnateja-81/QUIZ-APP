# Generated by Django 5.0.1 on 2024-01-03 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.IntegerField()),
                ('question', models.CharField(max_length=100)),
                ('o1', models.CharField(max_length=100)),
                ('o2', models.CharField(max_length=100)),
                ('o3', models.CharField(max_length=100)),
                ('o4', models.CharField(max_length=100)),
                ('co', models.IntegerField()),
            ],
        ),
    ]
