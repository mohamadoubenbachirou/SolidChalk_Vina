# Generated by Django 5.0 on 2024-01-20 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cumAtt', models.IntegerField(null=True)),
                ('cumVers', models.IntegerField(null=True)),
                ('ecart', models.IntegerField(null=True)),
                ('membre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='membre.membre')),
            ],
        ),
    ]