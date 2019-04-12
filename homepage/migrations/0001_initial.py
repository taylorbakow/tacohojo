# Generated by Django 2.1.5 on 2019-04-11 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drugs_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QtyPrescribed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Opioids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('DrugName', models.TextField()),
                ('IsOpioid', models.BooleanField()),
                ('AvgPerscribed', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Prescriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.TextField()),
                ('Lname', models.TextField()),
                ('Gender', models.TextField(choices=[('M', 'Male'), ('F', 'Female')], db_index=True, max_length=1)),
                ('Credentials', models.TextField()),
                ('Specialty', models.TextField()),
                ('OpioidPrescriber', models.BooleanField()),
                ('TotalPrescription', models.IntegerField()),
                ('AcetaminophinCodeine', models.IntegerField(default=0)),
                ('Fentanyl', models.IntegerField(default=0)),
                ('HydrocodoneAcetaminophen', models.IntegerField(default=0)),
                ('OxycodoneAcetaminophen', models.IntegerField(default=0)),
                ('Oxycontin', models.IntegerField(default=0)),
                ('IsOverPrescriber', models.BooleanField(default=0)),
                ('RiskRating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('StateAbbrev', models.CharField(db_column='StateAbbrev', max_length=2, primary_key=True, serialize=False)),
                ('StateName', models.TextField()),
                ('Population', models.IntegerField()),
                ('Deaths', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='prescriber',
            name='StateAbbrev',
            field=models.ForeignKey(db_column='StateAbbrev', on_delete=django.db.models.deletion.CASCADE, to='homepage.States'),
        ),
        migrations.AddField(
            model_name='drugs_details',
            name='DrugID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Opioids'),
        ),
        migrations.AddField(
            model_name='drugs_details',
            name='PrescriberID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Prescriber'),
        ),
    ]
