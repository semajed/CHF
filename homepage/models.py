from django.db import models
from polymorphic import PolymorphicModel
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate
from django.contrib import auth
from PIL import Image
import os.path
from django.conf import settings

class Address(models.Model):
	street1 = models.TextField()
	street2 = models.TextField(null=True)
	city = models.TextField()
	state = models.TextField()
	country = models.TextField()
	ZIP = models.TextField()
	def validateAddress():
		return
	def updateAddress():
		return

# class ShippingAddress(models.Model):
# 	street1 = models.TextField()
# 	street2 = models.TextField(null=True)
# 	city = models.TextField()
# 	state = models.TextField()
# 	country = models.TextField()
# 	ZIP = models.TextField()
# 	def validateAddress():
# 		return
# 	def updateAddress():
# 		return

class Photograph(models.Model):
	dateTaken = models.DateTimeField()
	placeTaken = models.TextField()
	image = models.ImageField(max_length="300",upload_to=os.path.join(settings.BASE_DIR, 'homepage/media/profilepictures/'))
	def updatePhoto():
		return
	def assignPhoto():
		return
	def assignNumber():
		return
	def updateType():
		return

class User(AbstractUser):
	secQuestion = models.TextField()
	secAnswer = models.TextField()
	phoneNumber = models.TextField()
	address = models.ForeignKey(Address)
	emergencyContactPhone = models.TextField()
	emergencyContactRelation = models.TextField()
	is_agent = models.BooleanField(default=False)
	is_participant= models.BooleanField(default=False)
	biographicalSketch = models.TextField(max_length=1000)
	is_organization = models.BooleanField(default=False)
	organizationName = models.TextField()
	photo = models.ForeignKey(Photograph, null=True)
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
	def __str__ (self):
		return self.first_name

class ShoppingCart(models.Model):
	totalItemsInCart = models.IntegerField()
	def clearShoppingCart():
		return

class Order(models.Model):

	orderDate = models.DateTimeField()
	# datePacked = models.DateTimeField()
	# dateShipped = models.DateTimeField()
	trackingNumber = models.IntegerField()
	shipping = models.TextField(Address)
	# totalOrders = models.IntegerField()
	creditCard = models.TextField()
	nameOnCard = models.TextField()
	def showShoppingCart():
		return
	def showCheckOutPage():
		return
	def emailReceiptToUser():
		return

class CatalogItem(PolymorphicModel):
	name = models.TextField()
	description = models.TextField()
	isRentableItem = models.BooleanField(default=False)
	isSellableItem = models.BooleanField(default=False)
	orders = models.ManyToManyField(Order, through='OrderProduct')

class CartLineItem(models.Model):
	totalItemsInCart = models.IntegerField()
	shoppingCart = models.ForeignKey(ShoppingCart)
	catalogItem = models.ForeignKey(CatalogItem)
	def clearShoppingCart():
		return

class OrderProduct(models.Model):
	order = models.ForeignKey(Order)
	catalogItem = models.ForeignKey(CatalogItem)


class Rental(models.Model):
	memberName = models.ForeignKey(User,related_name="+")
	rentalTime = models.DateTimeField()
	dueDate = models.DateTimeField()
	discountPercent = models.DecimalField(max_digits=5,decimal_places=2)
	handlingAgent = models.ForeignKey(User,related_name="+")
	totalRentals = models.IntegerField()
	catalogItems = models.ManyToManyField(CatalogItem, through='RentedItem')
	def createNewRental():
		return
	def emailReceiptToUser():
		return
	def addItem():
		return
	def calcDiscPercent():
		return
	def addToTotalRentals():
		return

class Return(models.Model):
	returnTime = models.DateTimeField()
	feesPaid = models.DecimalField(max_digits=10,decimal_places=2)
	user = models.ForeignKey(User)
	def completedReturnEmail():
		return

class RentedItem(models.Model):
	catalogItem = models.ForeignKey(CatalogItem)
	rental = models.ForeignKey(Rental)
	condition = models.TextField()
	newdamage = models.TextField()
	feeWaived = models.BooleanField(default=True)
	damageFee = models.DecimalField(max_digits=10,decimal_places=2)
	lateFee = models.DecimalField(max_digits=10,decimal_places=2)
	Return = models.ForeignKey(Return)

class Item(CatalogItem):
	value = models.DecimalField(max_digits=10,decimal_places=2)
	STP = models.DecimalField(max_digits=10,decimal_places=2)
	owner = models.ForeignKey(User,null=True)
	dueDate = models.DateTimeField()

class WardrobeItem(Item):
	size = models.IntegerField()
	sizeModifier = models.TextField()
	gender = models.TextField()
	color = models.TextField()
	pattern = models.TextField()
	startYear = models.IntegerField()
	endYear = models.IntegerField()
	note = models.TextField()

class Product(CatalogItem):
	category = models.TextField()
	currentPrice = models.DecimalField(max_digits=10,decimal_places=2)
	#maybe this can allow us to prevent further inheritance, making the creation of objects cleaner
	massProduced = models.BooleanField(default=False)
	quantityOnHand = models.IntegerField(null=True)
	uniqueProduct = models.BooleanField(default=False)
	dateMade = models.DateTimeField(null=True)
	madeToOrder = models.BooleanField(default=False)
	#should order form name be a reference to the orders?
	#or do we even need this field since we are keeping track of "OrderProduct"
	orderFormName = models.TextField(null=True)
	owner = models.ForeignKey(User,null=True)
	photo = models.ForeignKey(Photograph)
	def addToCart():
		return
	def showDetails():
		return

#i wonder if we can model this better to prevent this depth of inheritance, which can cause messy creation of objects
#look at the boolean fields in Product as a possible solution
# class MassProducedProduct(Product):
# 	quantityOnHand = models.IntegerField()

# class OneOffProduct(Product):
# 	dateMade = models.DateTimeField()

# class MadeToOrderProduct(Product):
# 	orderFormName = models.TextField()
# 	def createCustomForm():
# 		return

class HistoricalFigure(models.Model):
	name = models.TextField()
	birthPlace = models.TextField()
	birthDate = models.DateTimeField()
	deathPlace = models.TextField()
	deathDate = models.DateTimeField()
	bio = models.TextField()
	isFictional = models.BooleanField(default=False)

class Venue(models.Model):
	name = models.TextField()
	location = models.ForeignKey(Address)

class Event(models.Model):
	name = models.TextField()
	startDate = models.DateTimeField()
	endDate = models.DateTimeField()
	mapFileName = models.TextField()
	venue = models.ForeignKey(Venue, null=True)
	def mapEvent():
		return
	def __str__ (self):
		return self.name

class Area(models.Model):
	name = models.TextField()
	description = models.TextField()
	placeNumber = models.IntegerField()
	event = models.ForeignKey(Event)
	users = models.ManyToManyField(User, through='ParticipantRole')
	def __str__ (self):
		return self.name

class SaleItem(models.Model):
	name = models.TextField()
	description = models.TextField()
	lowPrice = models.DecimalField(max_digits=10,decimal_places=2)
	highPrice = models.DecimalField(max_digits=10,decimal_places=2)
	area = models.ForeignKey(Area,related_name="+")

class ParticipantRole(models.Model):
	name = models.TextField()
	participantType = models.TextField()
	area = models.ForeignKey(Area)
	user = models.ForeignKey(User)
	historicalFigure = models.ForeignKey(HistoricalFigure)

class PublicEvent(models.Model):
	name = models.TextField()
	description = models.TextField()
	event = models.ForeignKey(Event)





# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import authenticate
# from django.contrib import auth

# # event class models
# class Event(models.Model):
# 	name = models.TextField()
# 	startDate = models.DateField("Date")
# 	endDate = models.DateField("Date")
# 	def __str__ (self):
# 		return self.name

# class PublicEvent(models.Model):
# 	name = models.TextField()
# 	description = models.TextField()
# 	event = models.ForeignKey(Event, null=True)


# class Venue(models.Model):
# 	name = models.TextField()
# 	address = models.TextField()
# 	city = models.TextField()
# 	state = models.TextField()
# 	ZIP = models.TextField()
# 	event = models.ForeignKey(Event, null=True)
# 	def sendAddress():
# 		return
# 	def validateAddress():
# 		return


# class Area(models.Model):
# 	name = models.TextField()
# 	description = models.TextField()
# 	placeNumber = models.IntegerField()
# 	event = models.ForeignKey(Event)
# 	def updateAreaDetails():
# 		return
# 	def __str__ (self):
# 		return self.name


# class SaleItem(models.Model):
# 	name = models.TextField()
# 	description = models.TextField()
# 	lowPrice = models.DecimalField(max_digits=10,decimal_places=2)
# 	highPrice = models.DecimalField(max_digits=10,decimal_places=2)
# 	area = models.ForeignKey(Area,related_name="+")

# class Address(models.Model):
# 	# List of constants for the states:
# 	ALASKA = 'AK'
# 	ALABAMA = 'AL'
# 	ARKANSAS = 'AR'
# 	ARIZON = 'AZ'
# 	CALIFORNIA = 'CA'
# 	COLORADO = 'CO'
# 	CONNECTICUT = 'CT'
# 	DELAWARE = 'DE'
# 	FLORIDA = 'FL'
# 	GEORGIA = 'GA'
# 	HAWAII = 'HI'
# 	IOWA = 'IA'
# 	IDAHO = 'ID'
# 	ILLINOIS = 'IL'
# 	INDIANA = 'IN'
# 	KANSAS = 'KS'
# 	LOUISIANA = 'LA'
# 	MASSACHUSETTS = 'MA'
# 	MARYLAND = 'MD'
# 	MAINE = 'ME'
# 	MICHIGAN = 'MI'
# 	MINNESOTA = 'MN'
# 	MISSOURI = 'MO'
# 	MISSISSIPPI = 'MS'
# 	MONTANA = 'MT'
# 	NORTH_CAROLINA = 'NC'
# 	NORTH_DAKOTA = 'ND'
# 	NEBRASKA = 'NE'
# 	NEW_HAMPSHIRE = 'NH'
# 	NEW_JERSEY = 'NJ'
# 	NEW_MEXICO = 'NM'
# 	NEVADA = 'NV'
# 	NEW_YORK = 'NY'
# 	OHIO = 'OH'
# 	OKLAHOMA = 'OK'
# 	OREGON = 'OR'
# 	PENNSYLVANIA = 'PA'
# 	RHODE_ISLAND = 'RI'
# 	SOUTH_CAROLINA = 'SC'
# 	SOUTH_DAKOTA = 'SD'
# 	TENNESSEE = 'TN'
# 	TEXAS = 'TX'
# 	UTAH = 'UT'
# 	VIRGINIA = 'VA'
# 	VERMONT = 'VT'
# 	WASHINGTON = 'WA'
# 	WISCONSIN = 'WI'
# 	WEST_VIRGINIA = 'WV'
# 	WYOMING = 'WY'
# 	STATE_CHOICES = (
# 		(ALASKA, 'Alaska'),
# 		(ALABAMA, 'Alabama'),
# 		(ARKANSAS, 'Arkansas'),
# 		(ARIZON, 'Arizon'),
# 		(CALIFORNIA, 'California'),
# 		(COLORADO, 'Colorado'),
# 		(CONNECTICUT, 'Connecticut'),
# 		(DELAWARE, 'Delaware'),
# 		(FLORIDA, 'Florida'),
# 		(GEORGIA, 'Georgia'),
# 		(HAWAII, 'Hawaii'),
# 		(IOWA, 'Iowa'),
# 		(IDAHO, 'Idaho'),
# 		(ILLINOIS, 'Illinois'),
# 		(INDIANA, 'Indiana'),
# 		(KANSAS, 'Kansas'),
# 		(LOUISIANA, 'Louisiana'),
# 		(MASSACHUSETTS, 'Massachusetts'),
# 		(MARYLAND, 'Maryland'),
# 		(MAINE, 'Maine'),
# 		(MICHIGAN, 'Michigan'),
# 		(MINNESOTA, 'Minnesota'),
# 		(MISSOURI, 'Missouri'),
# 		(MISSISSIPPI, 'Mississippi'),
# 		(MONTANA, 'Montana'),
# 		(NORTH_CAROLINA, 'North Carolina'),
# 		(NORTH_DAKOTA, 'North Dakota'),
# 		(NEBRASKA, 'Nebraska'),
# 		(NEW_HAMPSHIRE, 'New Hampshire'),
# 		(NEW_JERSEY, 'New Jersey'),
# 		(NEW_MEXICO, 'New Mexico'),
# 		(NEVADA, 'Nevada'),
# 		(NEW_YORK, 'New York'),
# 		(OHIO, 'Ohio'),
# 		(OKLAHOMA, 'Oklahoma'),
# 		(OREGON, 'Oregon'),
# 		(PENNSYLVANIA, 'Pennsylvania'),
# 		(RHODE_ISLAND, 'Rhode Island'),
# 		(SOUTH_CAROLINA, 'South Carolina'),
# 		(SOUTH_DAKOTA, 'South Dakota'),
# 		(TENNESSEE, 'Tennessee'),
# 		(TEXAS, 'Texas'),
# 		(UTAH, 'Utah'),
# 		(VIRGINIA, 'Virginia'),
# 		(VERMONT, 'Vermont'),
# 		(WASHINGTON, 'Washington'),
# 		(WISCONSIN, 'Wisconsin'),
# 		(WEST_VIRGINIA, 'West Virginia'),
# 		(WYOMING, 'Wyoming'),
# 	)
# 	street = models.TextField()
# 	city = models.TextField()
# 	state = models.CharField(max_length=2,
# 		choices=STATE_CHOICES,
# 		default=UTAH)
# 	ZIP = models.TextField()

# #user
# class User(AbstractUser):
# 	securityQuestion = models.TextField()
# 	securityAns = models.TextField()
# 	address = models.ForeignKey(Address,related_name="User Address",null=True)
# 	def login():
# 		return
# 	def signUp():
# 		return
# 	def loginErrorWarning():
# 		return
# 	def editUserSettings():
# 		return
# 	def forgotPassword():
# 		return

# class Phone(models.Model):
# 	number = models.IntegerField(primary_key=True)
# 	extension = models.IntegerField()
# 	phoneType = models.TextField()
# 	user = models.ForeignKey(User,related_name="+")
# 	def assignNumber():
# 		return


# class Agent(models.Model):
# 	appointmentDate = models.DateTimeField()
# 	def handleRequest():
# 		return


# class Participant(models.Model):
# 	biographicalSketch = models.TextField()
# 	contactRelationship = models.TextField()
# 	IDPhoto = models.ImageField()
# 	user = models.OneToOneField(User,related_name="particpant is a user")

# # class UserAccessRoles(models.Model):
# # 	personID = models.IntegerField()
# # 	accessRoleID = models.IntegerField()
# # 	userAccount = models.ForeignKey(User)
# # 	accessRoles = models.ForeignKey(AccessRoles)

# # class AccessRoles(models.Model):
# # 	name = models.TextField()
# # 	description = models.TextField()
# # 	user = models.ManyToManyField(UserAccessRoles,through="User")

# # class Permissions(models.Model):
# # 	name = models.TextField()
# # 	description = models.TextField()
# # 	accessRoles = models.ManyToManyField(AccessRoles,through="RolesPermissions")

# # class RolesPermissions(models.Model):
# # 	accessRoleID = models.IntegerField()
# # 	permissionsID = models.IntegerField()
# # 	accessRoles = models.ForeignKey(AccessRoles)
# # 	permissions = models.ForeignKey(Permissions)


# class Role(models.Model):
# 	name = models.TextField()
# 	roleType = models.TextField()
# 	def __str__ (self):
# 		return self.name


# # item class models 
# class Item(models.Model):
# 	name = models.TextField()
# 	description = models.TextField()
# 	value = models.DecimalField(max_digits=10,decimal_places=2)
# 	STP = models.DecimalField("Standard Rental Price",max_digits=10,decimal_places=2)
# 	owner = models.ForeignKey(User)


# class RentableItem(Item):
# 	item = models.ForeignKey(Item,related_name="+")


# class WardrobeItem(Item):
# 	size = models.IntegerField()
# 	sizeModifier = models.TextField()
# 	gender = models.TextField()
# 	color = models.TextField()
# 	pattern = models.TextField()
# 	startYear = models.IntegerField()
# 	endYear = models.IntegerField()
# 	note = models.TextField()


# class Rental(models.Model):
# 	rentalTime = models.DateTimeField()
# 	dueDate = models.DateTimeField()
# 	discountPercent = models.DecimalField(max_digits=5,decimal_places=2)
# 	totalRentals = models.IntegerField()
# 	user = models.ForeignKey(User)
# 	agent = models.ForeignKey(Agent)
# 	def emailReceiptToUser():
# 		return
# 	def calcDiscPercent():
# 		return
# 	def addToRentals():
# 		return


# class Return(models.Model):
# 	returnTime = models.DateTimeField()
# 	feesPaid = models.DecimalField(max_digits=10,decimal_places=2)
# 	agentID = models.ForeignKey(Agent)
# 	def completedReturnEmail():
# 		return

# # product class models
# class Order(models.Model):
# 	orderDate = models.DateTimeField()
# 	phone = models.TextField()
# 	datePacked = models.DateTimeField()
# 	dateShipped = models.DateTimeField()
# 	trackingNumber = models.IntegerField()
# 	totalOrders = models.IntegerField()
# 	packingAgent = models.ForeignKey(Agent,related_name="+")
# 	payProcessAgent = models.ForeignKey(Agent,related_name="+")
# 	shippingAgent = models.ForeignKey(Agent,related_name="+")
# 	def showShoppingCart():
# 		return
# 	def showCheckOutPage():
# 		return
# 	def thankYouPage():
# 		return


# class Product(models.Model):
# 	name = models.TextField()
# 	description = models.TextField()
# 	category = models.TextField()
# 	currentPrice = models.DecimalField(max_digits=10,decimal_places=2)
# 	user = models.ForeignKey(User)


# class BulkProduct(Product):
# 	quantityOnHand = models.IntegerField()
# 	order = models.ManyToManyField(Product,related_name="+")


# class IndividualProduct(Product):
# 	dateMade = models.DateField()
# 	order = models.ForeignKey(Order)


# class MadeToOrderProduct(Product):
# 	orderFormName = models.TextField()
# 	order = models.ManyToManyField(Product,related_name="+")


# class ProductPicture(Product):
# 	#picture should be an image field but we don't currently have the right dependency
# 	#pip3 install Pillow to enable the use of imageField()
# 	picture = models.TextField()
# 	caption = models.TextField()


# # Pictures
# class Photograph(models.Model):
# 	DateTaken = models.DateTimeField()
# 	PlaceTaken = models.TextField()
# 	#picture should be an image field but we don't currently have the right dependency
# 	#pip3 install Pillow to enable the use of imageField()
# 	Image = models.TextField()
# 	def assignPhoto():
# 		return
# 	def assignNumber():
# 		return

# class PhotographableThing(models.Model):
# 	photograph = models.ManyToManyField(Photograph)

