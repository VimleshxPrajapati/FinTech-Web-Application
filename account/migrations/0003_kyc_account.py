# Generated by Django 4.2.7 on 2023-11-28 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_red_code_kyc'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyc',
            name='account',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
    ]
