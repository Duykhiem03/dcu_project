# Generated by Django 5.0.1 on 2025-02-09 15:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cheese',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PizzaSauce',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PizzaSize',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('address', models.TextField(null=True)),
                ('crust_type', models.TextField()),
                ('cheese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaorder.cheese')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sauce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaorder.pizzasauce')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaorder.pizzasize')),
                ('toppings', models.ManyToManyField(to='pizzaorder.toppings')),
            ],
        ),
    ]
