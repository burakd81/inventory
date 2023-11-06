from django.db import models
from user.models import users
from type.models import types
from brand.models import brands

# Create your models here.
class inventory(models.Model):
    def __str__(self):
        return self.adSoyad
    
    id_users = models.ForeignKey(users, on_delete=models.CASCADE,verbose_name="Kullanıcı",null=True)
    id_types = models.ForeignKey(types, on_delete=models.CASCADE,verbose_name="Cinsi",null=True)
    id_brands = models.ForeignKey(brands, on_delete=models.CASCADE,verbose_name="Marka Model",null=True)
    computerName = models.CharField(max_length=50,verbose_name="Bilgisayar Adı",null=True)
    userName = models.CharField(max_length=50,verbose_name="Kullanıcı Adı",null=True)
    serialNumber = models.CharField(max_length=50,verbose_name="Seri No",null=True)
    lanMac = models.CharField(max_length=50,verbose_name="LAN MAC",null=True)
    wifiMac = models.CharField(max_length=50,verbose_name="Wİ-Fİ MAC",null=True)
    windows = models.CharField(max_length=50,verbose_name="WİNDOWS",null=True)
    office = models.CharField(max_length=50,verbose_name="Ofis",null=True)
    licenceCodeOfOffice = models.CharField(max_length=50,verbose_name="Lisans Kodu Ofis",null=True)
    connectOfficeToMail = models.CharField(max_length=50,verbose_name="Ofis Bağlı E-Posta Adresi",null=True)
    debitNumber = models.CharField(max_length=50,verbose_name="Zimmet No",null=True)
    remoteDesktopConnection = models.CharField(max_length=50,verbose_name="Uzaktan Masaüstü Bağlantısı",null=True)
    debitDate = models.DateField(verbose_name="Zimmet Tarihi",null=True)
