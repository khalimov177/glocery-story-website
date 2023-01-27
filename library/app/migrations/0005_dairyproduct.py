# Generated by Django 4.1.4 on 2023-01-13 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_feature_alter_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dairyproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('thumb', models.ImageField(default='default_product.png', null=True, upload_to='')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'db_table': 'app_dairyproducts',
            },
        ),
    ]
