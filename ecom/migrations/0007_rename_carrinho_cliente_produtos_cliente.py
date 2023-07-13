# Generated by Django 4.2.3 on 2023-07-12 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_carrinho'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carrinho',
            new_name='Cliente',
        ),
        migrations.AddField(
            model_name='produtos',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.cliente'),
        ),
    ]