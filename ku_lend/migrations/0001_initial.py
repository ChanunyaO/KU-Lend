from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('pickup_place', models.CharField(max_length=300)),
                ('owner', models.CharField(max_length=50)),
                ('status', models.CharField(default='Avaliable', max_length=10)),
                ('note', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('amount_items', models.PositiveSmallIntegerField(default=1)),
                ('item_image', models.ImageField(upload_to='')),
                ('rate_fee', models.IntegerField()),
                ('max_item_each_user', models.IntegerField()),
                ('max_day_each_user', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('borrower', models.CharField(max_length=50)),
                ('borrower_email', models.EmailField(max_length=254)),
                ('borrower_fee', models.IntegerField(null=True)),
                ('borrower_paid_status', models.CharField(max_length=50)),
                ('borrower_note', models.CharField(max_length=10000)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ku_lend.item')),
            ],
        ),
    ]
