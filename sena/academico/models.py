from django.db import models

# Create your models here.

VACTIVO=(
    (1,"ACTIVO"),
    (2,"INACTIVO")
)

class COORDINACION(models.Model):
    nom=models.TextField(verbose_name="Nombre de la coordinación")
    
class COORDINACION(models.Model):
    nom=models.TextField(verbose_name="Nombre de la coordinación")
    def __str__(self):
        return self.nom
    
class AREA(models.Model):
    nom=models.CharField(max_length=4,verbose_name="Nombre del area")
    descripcion=models.TextField()
    idcoordina=models.ForeignKey(COORDINACION,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
class TITULACION(models.Model):
    cod=models.IntegerField(verbose_name="codigo de la titulacion")
    nom=models.TextField()
    idarea=models.ForeignKey(AREA,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
class FICHA(models.Model):
    nom=models.TextField()
    estado=models.IntegerField(default=1,choices=VACTIVO)
    idtitulacion=models.ForeignKey(TITULACION,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
class NCL(models.Model):
    cod=models.TextField()
    nom=models.TextField()
    des=models.TextField()
    idtitulacion=models.ForeignKey(TITULACION,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
class RAP(models.Model):
    cod=models.TextField()
    nom=models.TextField()
    idncl=models.ForeignKey(NCL,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
class ACTIVIDAD(models.Model):
    nom=models.TextField()
    estado=models.IntegerField(default=1,choices=VACTIVO)
    horas=models.IntegerField(default=0)
    def __str__(self):
        return self.nom
    
class RAP_ACTIVIDAD(models.Model):
    idrap=models.ForeignKey(RAP,null=True,blank=True,on_delete=models.CASCADE)
    idactividad=models.ForeignKey(ACTIVIDAD,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
class FICHAS_ACTIVIDAD(models.Model):
    idfichas=models.ForeignKey(FICHA,null=True,blank=True,on_delete=models.CASCADE)
    idactividad=models.ForeignKey(ACTIVIDAD,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom