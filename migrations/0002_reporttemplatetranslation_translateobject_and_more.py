# Generated by Django 4.2 on 2024-02-22 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporttemplatetranslation',
            name='translateObject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translates', to='report.reporttemplate'),
        ),
        migrations.AlterField(
            model_name='reporttemplatetranslation',
            name='language',
            field=models.CharField(choices=[('fr', 'fr')], default='fr', max_length=255, verbose_name='language'),
        ),
    ]