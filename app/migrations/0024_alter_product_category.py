# Generated by Django 5.0 on 2024-01-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CR', 'Curd'), ('MS', 'Milk Shake'), ('GH', 'Ghee'), ('LS', 'Lassi'), ('PN', 'Paneer'), ('ML', 'Milk'), ('IC', 'Ice-Cream'), ('CZ', 'Cheese')], max_length=2),
        ),
    ]
