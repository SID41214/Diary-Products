# Generated by Django 5.0 on 2023-12-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_product_category_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('GH', 'Ghee'), ('CR', 'Curd'), ('PN', 'Paneer'), ('MS', 'Milk Shake'), ('LS', 'Lassi'), ('IC', 'Ice-Cream'), ('CZ', 'Cheese'), ('ML', 'Milk')], max_length=2),
        ),
    ]
