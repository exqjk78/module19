# Generated by Django 5.1.5 on 2025-01-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_alter_buyer_balance_alter_game_cost_alter_game_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='game',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='game',
            name='size',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(default='Unnamed', max_length=100),
        ),
    ]
