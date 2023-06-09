from django.db import models
#Tambahan
import qrcode
from django.core.files import File
from PIL import Image, ImageDraw
from io import BytesIO
# Create your models here.
class Website(models.Model):
    name=models.CharField(max_length=200)
    qr_code =models.ImageField(upload_to='qr_codes',blank=True)
    
    def __str__(self):
        return str(self.name)
    
    # membuat method 
    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.name)
        canvas= Image.new('RGB',(290,290),'white')
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname=f'qr_code-{self.name}.png'
        #untuk menyimpan kedalam memory
        buffer=BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)
