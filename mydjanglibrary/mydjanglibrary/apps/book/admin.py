from django.contrib import admin
from mydjanglibrary.apps.book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'get_author_full_name',
        'isbn',
        'published',
        'published_at',
    )

def get_author_full_name(self,obj):
    author_obj = obj.author
    first_name = author_obj.user.first_name
    last_name = author_obj.user.last_name

    return f'{first_name} {last_name}'

get_author_full_name.short_description = 'Author'