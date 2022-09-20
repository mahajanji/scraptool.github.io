from django.contrib import admin
from .models import GradeMetal,GradeOverhead,Quality,QualityMetal,QualityOverhead,GradeNewValue,Actual
# Register your models here.
admin.site.register(GradeMetal)
admin.site.register(GradeOverhead)
admin.site.register(Quality)
admin.site.register(QualityMetal)
admin.site.register(QualityOverhead)
admin.site.register(GradeNewValue)
admin.site.register(Actual)