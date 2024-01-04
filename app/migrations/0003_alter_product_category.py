# Generated by Django 5.0 on 2023-12-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ML', 'Milk'), ('PN', 'Paneer'), ('MS', 'Milk Shake'), ('CZ', 'Cheese'), ('CR', 'Curd'), ('GH', 'Ghee'), ('LS', 'Lassi'), ('IC', 'Ice-Cream')], max_length=2),
        ),
    ]
