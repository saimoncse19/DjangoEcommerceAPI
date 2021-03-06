# Generated by Django 3.1.4 on 2020-12-08 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20201208_1522'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('In Review', 'In Review'), ('Being Delivered', 'Being Delivered'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_refunded', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('products', models.ManyToManyField(to='product.Product')),
            ],
        ),
    ]
