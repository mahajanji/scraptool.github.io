from django.db import models
# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True)
    address = models.CharField(max_length=220,blank=True, null=True)
    contact = models.CharField(max_length=120,blank=True, null=True)
    mob_no = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(max_length=120,blank=True, null=True)
    ename = models.CharField(max_length=120,blank=True, null=True)
    econtact = models.CharField(max_length=120,blank=True, null=True)
    emob_no = models.CharField(max_length=120, blank=True, null=True)
    eemail = models.EmailField(max_length=120,blank=True, null=True)
    

    def __str__(self):
        return self.name


class Yard(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,blank=True, null=True,related_name="Supplier")
    name = models.CharField(max_length=120,blank=True, null=True)
    address = models.CharField(max_length=120,blank=True, null=True)

    def __str__(self):
        return self.name        


class cost(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True)
    shortform = models.CharField(max_length=120,blank=True, null=True)
    rate = models.FloatField(blank=True, null=True, default=0)
    misc = models.CharField(max_length=120,blank=True, null=True)

    def __str__(self):
        return self.name  


class metal(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True)
    shortform = models.CharField(max_length=120,blank=True, null=True)
    misc = models.CharField(max_length=120,blank=True, null=True)

    def __str__(self):
        return self.name  

class Typeo(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True)
    def __str__(self):
        return self.name
        
class GradeNewValue(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True)
    

        
class Grade(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True)
    details = models.CharField(max_length=120,blank=True, null=True)
    gradegrp = models.CharField(max_length=120,blank=True, null=True)
    misc = models.CharField(max_length=120,blank=True, null=True)
    recovery = models.CharField(max_length=120, null=True,blank=True)
    typeo = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.name  
        
class GradeMetal(models.Model):
    cost = models.CharField(max_length=120,blank=True, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE,blank=True, null=True,related_name="Grade_grademetal")
    metal = models.ForeignKey(metal, on_delete=models.CASCADE,blank=True, null=True,related_name="metal_grademetal")
    
    def __str__(self):
        return self.cost 
        
class GradeOverhead(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE,blank=True, null=True,related_name="Grade_gradeoverhead")
    cost = models.ForeignKey(cost, on_delete=models.CASCADE,blank=True, null=True,related_name="cost_gradeoverhead")
    cost_value = models.CharField(max_length=120,blank=True, null=True)
    

class Quality(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,blank=True, null=True,related_name="Supplier_quality")
    yard = models.ForeignKey(Yard, on_delete=models.CASCADE,blank=True, null=True,related_name="Yard_quality")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE,blank=True, null=True,related_name="Grade_quality")
    duty = models.FloatField(null=True, blank=True, default=0)
    recovery = models.CharField(max_length=120, null=True,blank=True)
    typeo = models.CharField(max_length=120, null=True, blank=True)
    alc = models.CharField(max_length=120, null=True,blank=True)
    weightage_al = models.CharField(max_length=120, null=True, blank=True)
    mc = models.CharField(max_length=120, null=True,blank=True)
    ohc = models.CharField(max_length=120, null=True, blank=True)
    
    
class QualityMetal(models.Model):
    weightage = models.CharField(max_length=120,blank=True, null=True)
    cost = models.CharField(max_length=120,blank=True, null=True)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE,blank=True, null=True,related_name="Quality_Qualitymetal")
    metal = models.ForeignKey(metal, on_delete=models.CASCADE,blank=True, null=True,related_name="metal_Qualitymetal")
    
    def __str__(self):
        return self.cost 
        
class QualityOverhead(models.Model):
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE,blank=True, null=True,related_name="Quality_Qualityoverhead")
    cost = models.ForeignKey(cost, on_delete=models.CASCADE,blank=True, null=True,related_name="cost_Qualityoverhead")
    cost_value = models.CharField(max_length=120,blank=True, null=True)
    
    
class Actual(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,blank=True, null=True,related_name="Supplier_actual")
    yard = models.ForeignKey(Yard, on_delete=models.CASCADE,blank=True, null=True,related_name="Yard_actual")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE,blank=True, null=True,related_name="Grade_actual")
    duty = models.FloatField(null=True, blank=True, default=0)
    po_number = models.CharField(max_length=120,blank=True, null=True)
    recovery = models.CharField(max_length=120, null=True,blank=True)
    typeo = models.CharField(max_length=120, null=True, blank=True)
    alc = models.CharField(max_length=120, null=True,blank=True)
    weightage_al = models.CharField(max_length=120, null=True, blank=True)
    mc = models.CharField(max_length=120, null=True,blank=True)
    ohc = models.CharField(max_length=120, null=True, blank=True)
    
class ActualMetal(models.Model):
    actual_value = models.CharField(max_length=120,blank=True, null=True)
    weightage = models.CharField(max_length=120,blank=True, null=True)
    cost = models.CharField(max_length=120,blank=True, null=True)
    actual = models.ForeignKey(Actual, on_delete=models.CASCADE,blank=True, null=True,related_name="Actual_Actualmetal")
    metal = models.ForeignKey(metal, on_delete=models.CASCADE,blank=True, null=True,related_name="metal_Actualmetal")
    
    def __str__(self):
        return self.cost 
        
class ActualOverhead(models.Model):
    actual = models.ForeignKey(Actual, on_delete=models.CASCADE,blank=True, null=True,related_name="Actual_Actualoverhead")
    cost = models.ForeignKey(cost, on_delete=models.CASCADE,blank=True, null=True,related_name="cost_Actualoverhead")
    cost_value = models.CharField(max_length=120,blank=True, null=True)
