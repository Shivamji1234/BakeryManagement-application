# Generated by Django 4.0.2 on 2022-12-24 14:16

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Admin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField()),
                ('number', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('IP', 'In Processing'), ('OH', 'On Hold'), ('Can', 'Cancelled'), ('OFD', 'Out For Delivery'), ('Re', 'Returned'), ('De', 'Delivered')], default='IP', max_length=20)),
                ('quantity', models.IntegerField(default=1)),
                ('total_amount', models.IntegerField()),
                ('is_cancelled', models.BooleanField(default=False)),
                ('payment_type', models.CharField(choices=[('COD', 'COD'), ('Card', 'Card'), ('UPI', 'UPI'), ('Wallet', 'Wallet')], max_length=20)),
                ('shipping_address', models.CharField(blank=True, max_length=100)),
                ('transaction_id', models.CharField(max_length=256, unique=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Admin.items')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
