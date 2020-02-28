from django.db import models


location_choices = (
	('Sydney','Sydney'),
	('Melborune','Melborune'),
	('Perth','Perth'),
	('Brisbane','Brisbane'),
	('Canberra','Canberra'),
	('Adelaide','Adelaide'),
	('International','International'),
)

scale_choices = (
	('1','1'),
	('2','2'),
	('5','5'),
	('10','10'),
	('20','20'),
	('50','50'),
	('100','100'),
	('200','200'),
	('500','500'),
	('1000','1000'),
	('2000','2000'),
)

paper_choices = (
	('A0','A0'),
 	('A1','A1'),   
	('A2','A2'),   
	('A3','A3'),   
	('A4','A4'),   
)

type_choices = (
	("2D Drawing","2D Drawing"),
	("2D Model","2D Model"),
	("3D Model","3D Model"),
	("Animation File","Animation File"),
	("Calculation","Calculation"),
	("Certificate","Certificate"),
	("Clash Report","Clash Report"),
	("Combined Model","Combined Model"),
	("Correspondence","Correspondence"),
	("Cost Plan","Cost Plan"),
	("Database","Database"),
	("Drawing","Drawing"),
	("File Note","File Note"),
	("Information Exchange File","Information Exchange File"),
	("Material Sample","Material Sample"),
	("Matrix","Matrix"),
	("Meeting Minutes","Meeting Minutes"),
	("Model Rendition File","Model Rendition File"),
	("Presentation","Presentation"),
	("Programme","Programme"),
	("Register","Register"),
	("Report","Report"),
	("Room Data Sheet","Room Data Sheet"),
	("Schedule","Schedule"),
	("Specification","Specification"),
	("Survey","Survey"),
	("Visualisation","Visualisation"),
)

level_LUT = {"00":"00 - Datum","B1":"B1 - Lower Basement","L0":"L0 - Basement","L1":"L1 - Concourse","L1M":"L1M - Concourse Mezzanine","L2":"L2 - Level 2","L3":"L3 - Level 3","L4":"L4 - Level 4","L5":"L5 - Level 5","RF":"RF - Roof","XX":"XX - Level NA","ZZ":"ZZ - Multiple Level","LT":"ZZ - Multiple Level","MT":"ZZ - Multiple Level","ST":"ZZ - Multiple Level","UT":"ZZ - Multiple Level"}
sequence_LUT = {"00":"00 - Whole Site","00.":"00 - Whole Site","01":"01 - Building Zone A","02":"02 - Building Zone B","03":"03 - Building Zone C","04":"04 - Building Zone D","05":"05 - Building Zone E","06":"06 - Building Zone F","07":"07 - Building Zone G","08":"08 - Building Zone H","09":"09 - Building Zone I","11":"11 - Building Sector 1","12":"12 - Building Sector 2","13":"13 - Building Sector 3","14":"14 - Building Sector 4","15":"15 - Building Sector 5","16":"16 - Building Sector 6","17":"17 - Building Sector 7","18":"18 - Building Sector 8","19":"19 - Building Sector 9","20":"20 - Building Sector 10","21":"21 - Building Sector 11","22":"22 - Building Sector 12","23":"23 - Building Sector 13","24":"24 - Building Sector 14","25":"25 - Building Sector 15","26":"26 - Building Sector 16","27":"27 - Building Sector 17","28":"28 - Building Sector 18","29":"29 - Building Sector 19","30":"30 - Building Sector 20","31":"31 - Building Sector 21","32":"32 - Building Sector 22","33":"33 - Building Sector 23","34":"34 - Building Sector 24"}


# Create your models here.
class Drawings(models.Model):
	dn_project = models.CharField(max_length=200)
	dn_originator = models.CharField(max_length=200)
	dn_volume_system = models.CharField(max_length=200)
	dn_type = models.CharField(max_length=200)
	dn_discipline = models.CharField(max_length=200)
	dn_series = models.CharField(max_length=200)
	dn_level = models.CharField(max_length=200)
	dn_zone_sequence = models.CharField(max_length=200)
	drawing_title1 = models.CharField(max_length=200)
	drawing_title2 = models.CharField(max_length=200)
	drawing_title3 = models.CharField(max_length=200)
	studio = models.CharField(max_length=200,choices=location_choices,default="Sydney")
	model_location = models.CharField(max_length=200)
	revision_offset = models.CharField(max_length=200)
	#ADD ACONEX REVISION current & to be issued
	scale = models.CharField(max_length=200,choices=scale_choices,default="100")
	paper = models.CharField(max_length=200,choices=paper_choices,default="A0")
	dwg_type = models.CharField(max_length=200,choices=type_choices,default="2D Drawing")
	discipline = models.CharField(max_length=200,default="Architectural")

	#Check ACONEX inputs for phase drop down
	phase = models.CharField(max_length=200,default="Design Development")
	originator = models.CharField(max_length=200,default="Cox Architects")





	def revitSheetNumber(self):
		rsn = self.dn_discipline + self.dn_series + self.dn_level + self.dn_zone_sequence
		rsn = str(rsn).replace("~","")
		return rsn

	def drawingNumber(self):
		dn = self.dn_project + "-" + self.dn_originator + "-" + self.dn_volume_system + "-" + self.dn_type + "-" + self.revitSheetNumber()
		dn = str(dn).replace("~","")
		return dn

	def drawingTitle(self):
		if self.drawing_title3 == "" or self.drawing_title3 == "-":
			dt = self.drawing_title2
		else:
			dt = self.drawing_title2 + "-" + self.drawing_title3
		return dt

	def level(self):
		try:
			lvl = level_LUT[self.dn_level]
		except:
			lvl = "Null"
		return lvl

	def sequence(self):
		try:
			if "~" in str(self.dn_zone_sequence):
				sq = "01-99 - Default Sequence"
			else:
				sq = sequence_LUT[self.dn_zone_sequence]
		except:
			sq = "Not a valid zone_sequence"
		return sq




