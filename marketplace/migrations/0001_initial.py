from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('skills', models.JSONField(blank=True, default=list)),
                ('budget_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('budget_max', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('open', 'open'), ('in_progress', 'in_progress'), ('completed', 'completed')], default='open', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_letter', models.TextField()),
                ('bid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('eta_days', models.PositiveIntegerField(default=7)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to='marketplace.project')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('finished_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('closed', 'closed')], default='active', max_length=20)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='marketplace.project')),
                ('proposal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='marketplace.proposal')),
            ],
        ),
    ]
