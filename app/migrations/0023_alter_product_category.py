# Generated by Django 5.0 on 2024-01-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('LS', 'Lassi'), ('GH', 'Ghee'), ('ML', 'Milk'), ('CZ', 'Cheese'), ('CR', 'Curd'), ('IC', 'Ice-Cream'), ('PN', 'Paneer'), ('MS', 'Milk Shake')], max_length=2),
        ),
    ]
