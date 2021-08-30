# Copyright The IETF Trust 2021 All Rights Reserved

# Generated by Django 2.2.24 on 2021-07-27 08:04

from django.db import migrations


def forward(apps, schema_editor):
    DocTypeName = apps.get_model('name', 'DocTypeName')
    DocTypeName.objects.create(
        prefix='proc-materials',
        slug='procmaterials',
        name="Proceedings Materials",
        desc="",
        used=True,
        order=0
    )


def reverse(apps, schema_editor):
    DocTypeName = apps.get_model('name', 'DocTypeName')
    DocTypeName.objects.filter(slug='procmaterials').delete()


class Migration(migrations.Migration):
    # Most of these dependencies are needed to permit the reverse migration
    # to work. Without them Django does not replay enough migrations and during
    # migration believes that there are foreign key references to the old
    # PK (name)  on the Document model.
    dependencies = [
        ('doc', '0043_bofreq_docevents'),
        ('group', '0044_populate_groupfeatures_parent_type_fields'),
        ('liaisons', '0006_document_primary_key_cleanup'),
        ('meeting', '0018_document_primary_key_cleanup'),
        ('name', '0029_populate_proceedingsmaterialtypename'),
        ('review', '0014_document_primary_key_cleanup'),
        ('submit', '0008_submissionextresource'),
    ]

    operations = [
        migrations.RunPython(forward, reverse)
    ]
