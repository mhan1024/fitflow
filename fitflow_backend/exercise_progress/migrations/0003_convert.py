from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('exercise_progress', '0002_rename_user_email_exerciseprogress_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exerciseprogress',
            name='date',
        ),
        migrations.RunSQL(
            """
            ALTER TABLE exercise_progress_exerciseprogress
            ALTER COLUMN weight_str TYPE jsonb USING to_jsonb(weight_str);

            ALTER TABLE exercise_progress_exerciseprogress
            ALTER COLUMN time_car TYPE jsonb USING to_jsonb(time_car);

            ALTER TABLE exercise_progress_exerciseprogress
            ALTER COLUMN distance_car TYPE jsonb USING to_jsonb(distance_car);

            ALTER TABLE exercise_progress_exerciseprogress
            ALTER COLUMN incline_car TYPE jsonb USING to_jsonb(incline_car);

            ALTER TABLE exercise_progress_exerciseprogress
            ALTER COLUMN speed_car TYPE jsonb USING to_jsonb(speed_car);

            ALTER TABLE exercise_progress_exerciseprogress
            ALTER COLUMN duration_mob TYPE jsonb USING to_jsonb(duration_mob);
            """
        ),
        migrations.AlterField(
            model_name='exerciseprogress',
            name='weight_str',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='exerciseprogress',
            name='time_car',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='exerciseprogress',
            name='distance_car',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='exerciseprogress',
            name='incline_car',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='exerciseprogress',
            name='speed_car',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='exerciseprogress',
            name='duration_mob',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
