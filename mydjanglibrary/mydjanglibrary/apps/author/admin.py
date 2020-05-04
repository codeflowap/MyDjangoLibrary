from django.contrib import admin
from mydjanglibrary.apps.author.models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_author_full_name',
        'user',
        'gender',
        'birth_date',
        'created_at',
        'updated_at',
    )

    def get_author_full_name(self, obj):
        first_name = obj.user.first_name
        last_name = obj.user.last_name

        return f'{first_name} {last_name}'

    get_author_full_name.short_description = 'Author'

