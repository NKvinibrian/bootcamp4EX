# Generated by Django 4.2.3 on 2023-07-12 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_alter_produtos_estoque_alter_produtos_nome_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('nome', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]
