from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HealthProfile(models.Model):
  objects = models.Manager()
  age = models.IntegerField()
  sex = models.IntegerField() #1 = male, 0 = female
  cpt = models.IntegerField() # 1= typical angina, 2= atypical angina, 3= non-anginal pain, 4= asymptomatic
  restbps = models.IntegerField()
  chol = models.IntegerField()
  fbs = models.IntegerField() # (> 120 mg/dl, 1 = true; 0 = false)
  rest_ecg = models.IntegerField() #0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria
  max_heart_rate = models.IntegerField()
  ex_ang = models.IntegerField() #1 = yes; 0 = no
  oldpeak = models.DecimalField(max_digits = 5, decimal_places = 2)
  slope = models.IntegerField() #1: upsloping, Value 2: flat, Value 3: downsloping
  vessels = models.IntegerField() # (0-3) # vessels
  thal = models.IntegerField() # 3 = normal; 6 = fixed defect; 7 = reversable defect
  disease = models.IntegerField() # 1= has, 0 = doesn't have
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

  #Returns string representation
  def __str__(self):
    return "(age: " + self.age + ", sex: " + self.sex + ", cpt: " + self.cpt + \
      ", restbps: " + self.restbps + ", chol: " + self.chol + ", fbs: " + self.fbs + ", rest_ecg: " + self.rest_ecg + \
      ", max_heart_rate: " + self.max_heart_rate + ", ex_ang: " + self.ex_ang + ", oldpeak: " + self.oldpeak + \
      ", oldpeak: " + self.oldpeak + ", slope: " + self.slope + ", vessels: " + self.vessels + \
      ", thal: " + self.thal + ", disease: " + self.disease + ")"

  # defines whether two profile instances are equal
  def __eq__(self, other):
    return self.age == other.age and self.sex == other.sex and self.cpt == other.cpt and self.restbps == other.restbps and self.chol == other.chol \
      and self.fbs == other.fbs and self.rest_ecg == other.rest_ecg and self.max_heart_rate == other.max_heart_rate and self.ex_ang == other.ex_ang \
      and self.oldpeak == other.oldpeak and self.slope == other.slope and self.vessels == other.vessels and self.thal == other.thal and self.disease == other.disease
