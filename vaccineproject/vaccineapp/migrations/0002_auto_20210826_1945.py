# Generated by Django 3.2.4 on 2021-08-26 14:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vaccineapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='people',
            name='cpassword',
        ),
        migrations.RemoveField(
            model_name='people',
            name='email',
        ),
        migrations.RemoveField(
            model_name='people',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='people',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='people',
            name='password',
        ),
        migrations.RemoveField(
            model_name='people',
            name='username',
        ),
        migrations.AddField(
            model_name='people',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='people',
            name='vaccine',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Taluk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccineapp.district')),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vaccineapp.district'),
        ),
        migrations.AddField(
            model_name='people',
            name='taluk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vaccineapp.taluk'),
        ),
    ]
