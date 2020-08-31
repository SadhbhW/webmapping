from django.contrib.postgres import operations
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('blog', '0001_initial')]
    operations = [
        operations.CreateExtension('postgis')
    ]
