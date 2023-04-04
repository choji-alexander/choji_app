import uuid
from django.db import models


class Account(models.Model):
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    trade_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.FloatField()
    password = models.CharField(max_length=254, default='password')
    d_o_b = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.BooleanField()
    state_of_origin = models.CharField(max_length=50)
    residential_address = models.CharField(max_length=255)
    nationality = models.CharField(max_length=100)
    recovery_question = models.CharField(max_length=100)
    recovery_answer = models.CharField(max_length=100)
    national_identifier = models.IntegerField()
    biography = models.TextField(default='Biography', null=True)
    other_link = models.URLField(max_length=2083, null=True)
    image_url = models.URLField(max_length=2083, null=True)
    open_date = models.DateTimeField(auto_now=True)
    choji_code = models.UUIDField(editable=False, default=uuid.uuid4)
    no_of_blogs = models.IntegerField(default=0)
    no_of_products = models.IntegerField(default=0)
    no_of_chapters = models.IntegerField(default=0)


class Account_activity(models.Model):
    account_id = Account.choji_code
    timestamp = models.DateTimeField(auto_now=True)
    choji_code = models.UUIDField(editable=False, default=uuid.uuid4)


class Follower(models.Model):
    follower_id = models.CharField(max_length=2083)
    account_id = Account.choji_code
    followers = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=True)
    choji_code = models.UUIDField(editable=False, default=uuid.uuid4)


class Following(models.Model):
    followed_id = models.CharField(max_length=2083)
    account_id = Account.choji_code
    following = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=True)
    choji_code = models.UUIDField(editable=False, default=uuid.uuid4)


class Chat(models.Model):
    sender_username = models.CharField(max_length=100)
    receiver_username = models.CharField(max_length=100)
    message = models.TextField(default='Type Message')
    sender_code = models.CharField(max_length=2083)
    receiver_code = models.CharField(max_length=2083)
    choji_code = models.CharField(max_length=2083, default=uuid.uuid4().hex)
    time_stamp = models.CharField(max_length=2083)
    is_read = models.BooleanField(default=False)


class Group_account(models.Model):
    no_of_accounts = models.IntegerField(default=0)
    group_name = models.CharField(max_length=255)
    description = models.TextField(default='describe account')
    group_admin_username = models.CharField(max_length=100)
    image_url = models.CharField(max_length=2083)
    trade_name = models.CharField(max_length=255)
    group_password = models.CharField(max_length=255, default='password')
    no_of_post = models.IntegerField(default=0)
    no_of_products = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    open_date = models.CharField(max_length=2083)
    choji_code = models.CharField(max_length=2083, default=uuid.uuid4().hex)


class Group_chat(models.Model):
    admin_name = models.CharField(max_length=255)
    no_of_members = models.IntegerField(default=0)
    names_of_members = models.TextField(default='names of members')
    title = models.CharField(max_length=255)
    description = models.TextField(default='description')
    status = models.CharField(max_length=255)
    message = models.TextField(default='message')
    sender_code = models.CharField(max_length=2083, default=0)
    sender_name = models.CharField(max_length=100)
    choji_code = models.CharField(max_length=2083, default=uuid.uuid4().hex)
    time_stamp = models.CharField(max_length=2083)


class Trade(models.Model):
    seller_code = models.CharField(max_length=2083)
    buyer_code = models.CharField(max_length=2083)
    seller_trade_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    buyer_location = models.CharField(max_length=2083)
    price = models.IntegerField(default=0)
    trade_status = models.CharField(max_length=255)
    trade_location = models.CharField(max_length=2083)
    seller_location = models.CharField(max_length=2083)
    buyer_trade_name = models.CharField(max_length=255)
    choji_code = models.CharField(max_length=2083, default=uuid.uuid4().hex)
    start_date = models.CharField(max_length=2083)


