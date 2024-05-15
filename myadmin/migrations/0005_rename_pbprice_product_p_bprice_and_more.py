# Generated by Django 4.2.2 on 2024-04-23 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0004_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pbprice',
            new_name='p_bprice',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pdescription',
            new_name='p_description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='piconname',
            new_name='p_iconname',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pid',
            new_name='p_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='ptitle',
            new_name='p_title',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='product_image/'),
        ),
    ]
