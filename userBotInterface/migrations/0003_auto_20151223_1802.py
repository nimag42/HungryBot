# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userBotInterface', '0002_choice_str_nb_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice_str',
            old_name='nb_Choice',
            new_name='nb_choice',
        ),
    ]
