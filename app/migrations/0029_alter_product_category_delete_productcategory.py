# Generated by Django 5.0 on 2024-01-04 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CZ', 'Cheese'), ('IC', 'Ice-Cream'), ('CR', 'Curd'), ('LS', 'Lassi'), ('MS', 'Milk Shake'), ('GH', 'Ghee'), ('ML', 'Milk'), ('PN', 'Paneer')], max_length=2),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]
