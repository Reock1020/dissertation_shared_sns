# Generated by Django 3.2 on 2021-05-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0006_auto_20210503_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='befollowed_text',
            field=models.CharField(blank=True, default='initial', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='follow_text',
            field=models.CharField(blank=True, default='initial', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='header_image',
            field=models.ImageField(blank=True, default=0, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='one_thing',
            field=models.TextField(blank=True, default='initial', null=True),
        ),
    ]