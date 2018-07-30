# Generated by Django 2.0.7 on 2018-07-30 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicbanking', '0019_auto_20180730_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.AlterField(
            model_name='account',
            name='account_holder',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='publicbanking.Client'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.CharField(default=None, max_length=50, primary_key=True, serialize=False),
        ),
    ]
