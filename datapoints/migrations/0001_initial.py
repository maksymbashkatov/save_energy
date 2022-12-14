# Generated by Django 4.1.3 on 2022-11-02 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datapoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('counter_data', models.IntegerField(blank=True, null=True)),
                ('organization_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.organizationobject')),
            ],
            options={
                'verbose_name': 'Datapoint',
                'verbose_name_plural': 'Datapoints',
                'db_table': 'Datapoints',
            },
        ),
    ]
