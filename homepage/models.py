from django.db import models
from django.contrib.auth.models import AbstractUser


# event class models
class Event(models.Model):
	name = models.TextField()
	startDate = models.DateField("Date")
	endDate = models.DateField("Date")

class PublicEvent(models.Model):
	name = models.TextField()
	description = models.TextField()
	event = models.ForeignKey(Event, null=True)


class Venue(models.Model):
	name = models.TextField()
	address = models.TextField()
	city = models.TextField()
	state = models.TextField()
	ZIP = models.TextField()
	event = models.ForeignKey(Event, null=True)
	def sendAddress():
		return
	def validateAddress():
		return


class Area(models.Model):
	name = models.TextField()
	description = models.TextField()
	placeNumber = models.IntegerField()
	event = models.ForeignKey(Event)
	def updateAreaDetails():
		return


class SaleItem(models.Model):
	name = models.TextField()
	description = models.TextField()
	lowPrice = models.DecimalField(max_digits=10,decimal_places=2)
	highPrice = models.DecimalField(max_digits=10,decimal_places=2)
	area = models.ForeignKey(Area,related_name="+")


class Person(models.Model):
	name = models.TextField()
	def notifyItemIsDue():
		return
	def notifyItemIsLate():
		return

#user
class User(AbstractUser):
	securityQuestion = models.TextField()
	securityAns = models.TextField()
	owner = models.OneToOneField(Person,related_name="account_of")
	def login():
		return
	def signUp():
		return
	def loginErrorWarning():
		return
	def editUserSettings():
		return
	def forgotPassword():
		return

class Address(models.Model):
	street = models.TextField()
	city = models.TextField()
	state = models.TextField()
	ZIP = models.TextField()
	person = models.ForeignKey(Person)

class Phone(models.Model):
	number = models.IntegerField(primary_key=True)
	extension = models.IntegerField()
	phoneType = models.TextField()
	person = models.ForeignKey(Person,related_name="+")
	def assignNumber():
		return


class Agent(models.Model):
	appointmentDate = models.DateTimeField()
	def handleRequest():
		return


class Participant(models.Model):
	biographicalSketch = models.TextField()
	contactRelationship = models.TextField()
	IDPhoto = models.ImageField()
	person = models.OneToOneField(Person,related_name="particpant is a person")

# class UserAccessRoles(models.Model):
# 	personID = models.IntegerField()
# 	accessRoleID = models.IntegerField()
# 	userAccount = models.ForeignKey(User)
# 	accessRoles = models.ForeignKey(AccessRoles)

# class AccessRoles(models.Model):
# 	name = models.TextField()
# 	description = models.TextField()
# 	user = models.ManyToManyField(UserAccessRoles,through="User")

# class Permissions(models.Model):
# 	name = models.TextField()
# 	description = models.TextField()
# 	accessRoles = models.ManyToManyField(AccessRoles,through="RolesPermissions")

# class RolesPermissions(models.Model):
# 	accessRoleID = models.IntegerField()
# 	permissionsID = models.IntegerField()
# 	accessRoles = models.ForeignKey(AccessRoles)
# 	permissions = models.ForeignKey(Permissions)


class Role(models.Model):
	name = models.TextField()
	roleType = models.TextField()
	def __str__ (self):
		return self.name


# item class models 
class Item(models.Model):
	name = models.TextField()
	description = models.TextField()
	value = models.DecimalField(max_digits=10,decimal_places=2)
	STP = models.DecimalField("Standard Rental Price",max_digits=10,decimal_places=2)
	owner = models.ForeignKey(Person)


class RentableItem(Item):
	item = models.ForeignKey(Item,related_name="+")


class WardrobeItem(Item):
	size = models.IntegerField()
	sizeModifier = models.TextField()
	gender = models.TextField()
	color = models.TextField()
	pattern = models.TextField()
	startYear = models.IntegerField()
	endYear = models.IntegerField()
	note = models.TextField()


class Rental(models.Model):
	rentalTime = models.DateTimeField()
	dueDate = models.DateTimeField()
	discountPercent = models.DecimalField(max_digits=5,decimal_places=2)
	totalRentals = models.IntegerField()
	personID = models.ForeignKey(Person)
	agentID = models.ForeignKey(Agent)
	def emailReceiptToUser():
		return
	def calcDiscPercent():
		return
	def addToRentals():
		return


class Return(models.Model):
	returnTime = models.DateTimeField()
	feesPaid = models.DecimalField(max_digits=10,decimal_places=2)
	agentID = models.ForeignKey(Agent)
	def completedReturnEmail():
		return

# product class models
class Order(models.Model):
	orderDate = models.DateTimeField()
	phone = models.TextField()
	datePacked = models.DateTimeField()
	dateShipped = models.DateTimeField()
	trackingNumber = models.IntegerField()
	totalOrders = models.IntegerField()
	packingAgent = models.ForeignKey(Agent,related_name="+")
	payProcessAgent = models.ForeignKey(Agent,related_name="+")
	shippingAgent = models.ForeignKey(Agent,related_name="+")
	def showShoppingCart():
		return
	def showCheckOutPage():
		return
	def thankYouPage():
		return


class Product(models.Model):
	name = models.TextField()
	description = models.TextField()
	category = models.TextField()
	currentPrice = models.DecimalField(max_digits=10,decimal_places=2)
	person = models.ForeignKey(Person)


class BulkProduct(Product):
	quantityOnHand = models.IntegerField()
	order = models.ManyToManyField(Product,related_name="+")


class IndividualProduct(Product):
	dateMade = models.DateField()
	order = models.ForeignKey(Order)


class MadeToOrderProduct(Product):
	orderFormName = models.TextField()
	order = models.ManyToManyField(Product,related_name="+")


class ProductPicture(Product):
	#picture should be an image field but we don't currently have the right dependency
	#pip3 install Pillow to enable the use of imageField()
	picture = models.TextField()
	caption = models.TextField()


# Pictures
class Photograph(models.Model):
	DateTaken = models.DateTimeField()
	PlaceTaken = models.TextField()
	#picture should be an image field but we don't currently have the right dependency
	#pip3 install Pillow to enable the use of imageField()
	Image = models.TextField()
	def assignPhoto():
		return
	def assignNumber():
		return

class PhotographableThing(models.Model):
	photograph = models.ManyToManyField(Photograph)