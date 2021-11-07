from django.contrib import admin
from .models import Unibber, University

# Register your models here.
@admin.register(Unibber)
class UnibberAdmin(admin.ModelAdmin):
    pass

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    pass
