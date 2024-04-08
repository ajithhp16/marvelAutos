from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(verbose_name="Person's first name", max_length=30, null=False)
    last_name = models.CharField(verbose_name="Person's last name", max_length=30, default=".")
    users_slug = models.SlugField()
    dob = models.DateField(verbose_name="Person's Date Of Birth")
    contact_number = models.CharField(verbose_name="Person's Contact Number", max_length=15, null=False, unique=True)
    mail_address = models.EmailField(verbose_name="Peron's Mail Address", max_length=50, null=False, unique=True)
    address = models.CharField(verbose_name="Person's Address", max_length=500)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class VehicleType(models.Model):
    vehicle_type = models.CharField(verbose_name="2/3/4/.. wheeler", max_length=30, unique=True, null=False)
    
    
class Insurance(models.Model):
    insurance_id = models.AutoField(primary_key=True)
    insurance_number = models.CharField(verbose_name="Insurance Number", max_length=30, null=False, unique=True)
    start_date = models.DateField(verbose_name="Insurance start  date", null=False)
    end_date = models.DateField(verbose_name="Insurance end  date", null=False)
    
    def __str__(self):
        return self.insurance_number
    
    
class Vehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_number = models.CharField(verbose_name="Vehicle Number", max_length=15, null=False, unique=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    insurance_id = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    brand_name = models.CharField(verbose_name="Brand name of the vehicle", max_length=30)
    model_name = models.CharField(verbose_name="Model name of the Vehicle", max_length=30)
    manufacture_year = models.PositiveIntegerField()
    
    def __str__(self):
        return self.vehicle_number
    
    
class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(verbose_name="Service Name", max_length=30)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    service_charges = models.DecimalField(max_digits=7, decimal_places=2)
    

class Bills(models.Model):
    bill_id = models.AutoField(primary_key=True)
    vehicle_id = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    admit_date = models.DateTimeField(verbose_name="Date when vehicle is taken for servicing")
    deliver_date = models.DateTimeField(verbose_name="Date when vehicle is delivered after servicing")
    total_charges = models.DecimalField(max_digits=7, decimal_places=2)
    discount_applied = models.PositiveIntegerField()
    paid_charges = models.DecimalField(max_field=7, decimal_places=2)

    
class VehicleServicings(models.Model):
    vehicle_servicing_id = models.AutoField(primary_key=True)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE)