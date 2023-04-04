from django.contrib import admin
from .models import Account, Chat, Group_account, Group_chat, Trade, Account_activity


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'trade_name', 'email', 'phone_number', 'gender', 'state_of_origin', 'choji_code')


class ChatAdmin(admin.ModelAdmin):
    list_display = ('sender_code', 'receiver_code', 'choji_code', 'time_stamp')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('choji_code', 'timestamp')


class Group_accountAdmin(admin.ModelAdmin):
    list_display = ('no_of_accounts', 'group_name', 'trade_name', 'group_admin_username', 'choji_code')


class Group_chatAdmin(admin.ModelAdmin):
    list_display = ('admin_name', 'no_of_members', 'title', 'sender_code', 'choji_code', 'time_stamp')


class TradeAdmin(admin.ModelAdmin):
    list_display = ('seller_code', 'buyer_code', 'product_name', 'price', 'trade_status', 'trade_location', 'choji_code'
                    )


admin.site.register(Account, AccountAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Group_chat, Group_chatAdmin)
admin.site.register(Group_account, Group_accountAdmin)
admin.site.register(Trade, TradeAdmin)
admin.site.register(Account_activity, ActivityAdmin)
