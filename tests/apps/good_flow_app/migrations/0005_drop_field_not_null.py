# Generated by Django 3.1 on 2019-09-21 20:17

from django.db import migrations, models


def insert_objects_and_default_check(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    TestTable = apps.get_model('good_flow_app', 'TestTable')
    instance = TestTable.objects.using(db_alias).create(test_field_int=1)
    assert instance.field == 0
    instance.delete()
    instance = TestTable.objects.using(db_alias).create(test_field_int=1, field=None)
    assert instance.field is None
    instance.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('good_flow_app', '0004_set_field_not_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testtable',
            name='field',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.RunPython(insert_objects_and_default_check, migrations.RunPython.noop),
    ]
