# Generated by Django 3.1 on 2019-09-21 20:15

from django.db import migrations, models


def insert_objects_and_null_check(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    TestTable = apps.get_model('good_flow_app', 'TestTable')
    instance = TestTable.objects.using(db_alias).create(test_field=1)
    assert instance.field is None
    instance.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('good_flow_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtable',
            name='field',
            field=models.IntegerField(null=True),
        ),
        migrations.RunPython(insert_objects_and_null_check, migrations.RunPython.noop),
    ]