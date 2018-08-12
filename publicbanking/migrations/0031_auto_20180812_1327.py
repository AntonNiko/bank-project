# Generated by Django 2.0.5 on 2018-08-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicbanking', '0030_auto_20180806_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='BufferAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=200)),
                ('account_number', models.IntegerField()),
                ('account_balance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('account_currency', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WireTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.IntegerField()),
                ('transaction_amount', models.FloatField()),
                ('transaction_time', models.DateTimeField(verbose_name='tansaction time')),
                ('transaction_name', models.CharField(max_length=200)),
                ('transaction_origin_balance', models.DecimalField(decimal_places=2, default=None, max_digits=20)),
                ('transaction_origin', models.ManyToManyField(related_name='wire_transaction_origin', to='publicbanking.Account')),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_origin',
            field=models.ManyToManyField(related_name='transaction_origin', to='publicbanking.Account'),
        ),
    ]