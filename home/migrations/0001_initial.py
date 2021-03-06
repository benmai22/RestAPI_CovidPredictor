# Generated by Django 3.1.6 on 2021-03-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=15)),
                ('ethnicity', models.CharField(choices=[('Graduate', 'Graduated'), ('Not_Graduate', 'Not_Graduate'), ('White', ' White'), ('American Indian', 'American Indian'), ('Non-Hispanic', ' Non-Hispanic'), ('Alaska Native', ' Alaska Native'), ('Native Hawaiian', 'Native Hawaiian'), ('Other Pacific Islander', 'Other Pacific Islander'), ('Hispanic', 'Hispanic'), ('Latino', 'Latino'), ('Black,', 'Black,'), ('Other', 'Other')], max_length=40)),
                ('underlying', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15)),
            ],
        ),
    ]
