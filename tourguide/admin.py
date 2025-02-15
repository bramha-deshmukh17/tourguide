from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(restaurant,ImportExportModelAdmin)
admin.site.register(customer,ImportExportModelAdmin)
admin.site.register(hotel,ImportExportModelAdmin)
admin.site.register(place,ImportExportModelAdmin)
admin.site.register(TourGuide,ImportExportModelAdmin)
admin.site.register(Booking,ImportExportModelAdmin)
admin.site.register(admins,ImportExportModelAdmin)

