from django.contrib import admin

from tutor_app.models import Tutor,Review,Transaction_T

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('tutor', 'rating', 'user_name', 'comment')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
    
# Register your models here.
admin.site.register(Tutor)
admin.site.register(Review)
admin.site.register(Transaction_T)