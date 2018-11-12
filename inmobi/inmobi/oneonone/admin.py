from django.contrib import admin
from .models import App, Content, Result


@admin.register(App)
class devicesAdmin(admin.ModelAdmin):
    list_display = ('app_title',
                    'app_title_eng',
                    'creator',
                    )


@admin.register(Content)
class devicesAdmin(admin.ModelAdmin):
    list_display = ('owner',
                    'os',
                    'adid',
                    'impression_id',
                    'modified_url')


@admin.register(Result)
class devicesAdmin(admin.ModelAdmin):
    list_display = (
        'os',
        'owner',
        'impression_id',
        'result_msg'
        )
