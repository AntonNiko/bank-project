# Generated by Django 2.0.7 on 2018-08-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicbanking', '0021_auto_20180730_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type_name', models.CharField(max_length=100)),
                ('account_free_transaction_len', models.IntegerField()),
                ('account_free_transaction_period', models.CharField(max_length=100)),
                ('account_website_transaction_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account_retail_transaction_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account_etransfer_transaction_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account_interest_rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_destination',
            field=models.ManyToManyField(related_name='_transaction_transaction_destination_+', to='publicbanking.Account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_origin',
            field=models.ManyToManyField(related_name='_transaction_transaction_origin_+', to='publicbanking.Account'),
        ),
    ]
