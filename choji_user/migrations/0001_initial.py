# Generated by Django 4.1.2 on 2022-12-13 00:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('trade_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.FloatField()),
                ('password', models.CharField(default='password', max_length=254)),
                ('d_o_b', models.DateField()),
                ('gender', models.BooleanField()),
                ('state_of_origin', models.CharField(max_length=50)),
                ('residential_address', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=100)),
                ('recovery_question', models.CharField(max_length=100)),
                ('recovery_answer', models.CharField(max_length=100)),
                ('national_identifier', models.IntegerField()),
                ('biography', models.TextField(default='Biography', null=True)),
                ('other_link', models.URLField(max_length=2083, null=True)),
                ('image_url', models.URLField(max_length=2083, null=True)),
                ('open_date', models.DateTimeField(auto_now=True)),
                ('choji_code', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('no_of_blogs', models.IntegerField(default=0)),
                ('no_of_products', models.IntegerField(default=0)),
                ('no_of_chapters', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Account_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('choji_code', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_username', models.CharField(max_length=100)),
                ('receiver_username', models.CharField(max_length=100)),
                ('message', models.TextField(default='Type Message')),
                ('sender_code', models.CharField(max_length=2083)),
                ('receiver_code', models.CharField(max_length=2083)),
                ('choji_code', models.CharField(default='fc61cae73e2948c68f796c60eca8057b', max_length=2083)),
                ('time_stamp', models.CharField(max_length=2083)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_id', models.CharField(max_length=2083)),
                ('followers', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_id', models.CharField(max_length=2083)),
                ('following', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_accounts', models.IntegerField(default=0)),
                ('group_name', models.CharField(max_length=255)),
                ('description', models.TextField(default='describe account')),
                ('group_admin_username', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=2083)),
                ('trade_name', models.CharField(max_length=255)),
                ('group_password', models.CharField(default='password', max_length=255)),
                ('no_of_post', models.IntegerField(default=0)),
                ('no_of_products', models.IntegerField(default=0)),
                ('followers', models.IntegerField(default=0)),
                ('total_likes', models.IntegerField(default=0)),
                ('open_date', models.CharField(max_length=2083)),
                ('choji_code', models.CharField(default='b347a49b9a154127a8b67c15b093f543', max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Group_chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=255)),
                ('no_of_members', models.IntegerField(default=0)),
                ('names_of_members', models.TextField(default='names of members')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='description')),
                ('status', models.CharField(max_length=255)),
                ('message', models.TextField(default='message')),
                ('sender_code', models.CharField(default=0, max_length=2083)),
                ('sender_name', models.CharField(max_length=100)),
                ('choji_code', models.CharField(default='63fb781c08944c1790b2b8646d2773dd', max_length=2083)),
                ('time_stamp', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_code', models.CharField(max_length=2083)),
                ('buyer_code', models.CharField(max_length=2083)),
                ('seller_trade_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('buyer_location', models.CharField(max_length=2083)),
                ('price', models.IntegerField(default=0)),
                ('trade_status', models.CharField(max_length=255)),
                ('trade_location', models.CharField(max_length=2083)),
                ('seller_location', models.CharField(max_length=2083)),
                ('buyer_trade_name', models.CharField(max_length=255)),
                ('choji_code', models.CharField(default='454550b45fe242acbd8226eea4c54885', max_length=2083)),
                ('start_date', models.CharField(max_length=2083)),
            ],
        ),
    ]
