# Generated by Django 4.2.7 on 2023-11-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_kyc_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_status',
            field=models.CharField(choices=[('active', 'Active'), ('in-active', 'In-active'), ('pending', 'Pending')], default='in-active', max_length=100),
        ),
    ]
