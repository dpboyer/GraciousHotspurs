# Generated by Django 3.1.3 on 2020-12-08 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('CS351_Project', '0006_delete_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CS351_Project.course'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='office_hour',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='instructor',
            name='office_location',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='instructor',
            name='office_number',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.CreateModel(
            name='TA',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('phone_number', models.CharField(default='', max_length=20, null=True)),
                ('office_hour', models.CharField(default='', max_length=20, null=True)),
                ('office_number', models.CharField(default='', max_length=20, null=True)),
                ('office_location', models.CharField(default='', max_length=20, null=True)),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CS351_Project.section')),
            ],
        ),
    ]
