# Generated by Django 3.2.6 on 2022-01-04 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=30)),
                ('title', models.CharField(default='', max_length=30)),
                ('company_website', models.CharField(default='', max_length=30)),
                ('technologies', models.CharField(default='', max_length=30)),
                ('responsibilities', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=30)),
                ('not_to_Display_Full_name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=30)),
                ('location', models.CharField(default='', max_length=30)),
                ('title', models.CharField(default='', max_length=30)),
                ('profile_photo', models.ImageField(default='media/isle.jpg', upload_to='profile_photos')),
                ('about_me', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('website_link', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
                ('github_link', models.URLField(blank=True)),
                ('q_edited_counter', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('reputation', models.IntegerField(default=1)),
                ('is_banned', models.BooleanField(default=False)),
                ('post_edit_inactive_for_six_month', models.IntegerField(default=0)),
                ('is_moderator', models.BooleanField(default=False)),
                ('is_high_moderator', models.BooleanField(default=False)),
                ('targeted_tag', models.CharField(default='Commenter', max_length=30)),
                ('review_close_votes', models.BooleanField(default=False)),
                ('favorite_question_S', models.BooleanField(default=False)),
                ('lifeJacket', models.BooleanField(default=False)),
                ('altruist', models.BooleanField(default=False)),
                ('commenter', models.BooleanField(default=False)),
                ('logout_on_all_devices', models.BooleanField(default=False)),
                ('send_email_notifications', models.BooleanField(default=False)),
                ('voting_flags', models.IntegerField(default=0)),
                ('helpful_close_votes', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=30)),
                ('prefered_technologies', models.CharField(default='', max_length=30)),
                ('min_expierence_level', models.CharField(choices=[('Student', 'Student'), ('Junior', 'Junior'), ('Mid_Level', 'Mid Level'), ('Senior', 'Senior'), ('Lead', 'Lead'), ('Manager', 'Manager')], default='', max_length=30)),
                ('max_expierence_level', models.CharField(choices=[('Student', 'Student'), ('Junior', 'Junior'), ('Mid_Level', 'Mid Level'), ('Senior', 'Senior'), ('Lead', 'Lead'), ('Manager', 'Manager')], default='', max_length=30)),
                ('job_type', models.CharField(choices=[('FULL_TIME', 'Full Time'), ('CONTRCT', 'Contract'), ('InternShip', 'InternShip')], max_length=30)),
                ('job_search_status', models.CharField(choices=[('looking_for_job', 'Actively looking right now'), ('open_but_not_looking', 'Open, but not actively looking'), ('not_interested_in_jobs', 'Not interested in jobs')], max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('create_posts', models.BooleanField(default=True)),
                ('create_wiki_posts', models.BooleanField(default=False)),
                ('remove_new_user_restrictions', models.BooleanField(default=False)),
                ('voteUpPriv', models.BooleanField(default=False)),
                ('flag_posts', models.BooleanField(default=False)),
                ('comment_everywhere_Priv', models.BooleanField(default=False)),
                ('set_bounties', models.BooleanField(default=False)),
                ('edit_community_wiki', models.BooleanField(default=False)),
                ('voteDownPriv', models.BooleanField(default=False)),
                ('view_close_votes_Priv', models.BooleanField(default=False)),
                ('access_review_queues', models.BooleanField(default=False)),
                ('established_user_Priv', models.BooleanField(default=False)),
                ('create_tags', models.BooleanField(default=False)),
                ('edit_questions_answers', models.BooleanField(default=False)),
                ('cast_close_AND_Reopen_votes', models.BooleanField(default=False)),
                ('accessTo_moderatorTools', models.BooleanField(default=False)),
                ('protect_questions', models.BooleanField(default=False)),
                ('trusted_user_Priv', models.BooleanField(default=False)),
                ('helpful_flags_counter', models.IntegerField(blank=True, default=0, null=True)),
                ('posts_edited_counter', models.IntegerField(blank=True, default=0, null=True)),
                ('suggested_Edit_counter', models.IntegerField(blank=True, default=0, null=True)),
                ('editPostTimeOfUser', models.DateTimeField(blank=True, null=True)),
                ('Refiner_Illuminator_TagPostCounter', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
