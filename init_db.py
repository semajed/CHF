#!/usr/bin/env python3

# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp1.settings'
import django
django.setup()

# import necessary stuff
import homepage.models as hmod
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess
import sys
from datetime import datetime, timedelta

###############################################################################################
    ############## drop database, recreate it, then migrate models ###################
###############################################################################################
cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable,"manage.py","migrate"])

########### create permissions and groups #############
# Permission.objects.all().delete()
Group.objects.all().delete()
group1 = Group()
group1.name = "Admin"
group1.save()

group2 = Group()
group2.name = "Manager"
group2.save()

group3 = Group()
group3.name = "User"
group3.save()

# permissionList = []
permissionsList = Permission.objects.all()

for p in permissionsList:
    permission = p
    permission.save()
    group1.permissions.add(permission)
    group1.save()

for p in permissionsList:
    if p.id > 15:
        permission = p
        permission.save()
        group2.permissions.add(permission)
        group2.save()

for p in permissionsList:
    if (p.id > 15 and p.id < 28) | (p.id > 30 and p.id < 34) | (p.id > 75 and p.id < 79):
        permission = p
        permission.save()
        group3.permissions.add(permission)
        group3.save()


######### create an address ###############
hmod.Address.objects.all().delete()
a2 = hmod.Address()
a2.street1 = "123 Easy Street"
a2.city = "Houston"
a2.state = "Texas"
a2.country = "United States"
a2.ZIP = "77379"
a2.save()

a1 = hmod.Address()
a1.street1 = "123 Difficult Street"
a1.city = "Orem"
a1.state = "Utah"
a1.country = "United States"
a1.ZIP = "87483"
a1.save()

a = hmod.Address()
a.street1 = "321 Backwards Circle"
a.city = "Munich"
a.state = "Idaho"
a.country = "United States"
a.ZIP = "99999"
a.save()

############## create photograph ###############

photo = hmod.Photograph()
photo.dateTaken = "1999-04-13"
photo.placeTaken = "Orem Utah"
photo.image = "/static/homepage/media/profilepictures/emptypic.jpg"
photo.save()

##### product photographs #####

photo1 = hmod.Photograph()
photo1.dateTaken = "1999-04-13"
photo1.placeTaken = "Orem Utah"
photo1.image = "/static/homepage/media/Products/CannonFinished.jpg"
photo1.save()

photo2 = hmod.Photograph()
photo2.dateTaken = "1999-04-13"
photo2.placeTaken = "Orem Utah"
photo2.image = "/static/homepage/media/Products/BreechesPic.jpg"
photo2.save()

photo3 = hmod.Photograph()
photo3.dateTaken = "1999-04-13"
photo3.placeTaken = "Orem Utah"
photo3.image = "/static/homepage/media/Products/covered_wagon.jpg"
photo3.save()

photo4 = hmod.Photograph()
photo4.dateTaken = "1999-04-13"
photo4.placeTaken = "Orem Utah"
photo4.image = "/static/homepage/media/Products/gun.jpg"
photo4.save()

##### item photographs #####

photo5 = hmod.Photograph()
photo5.dateTaken = "1999-04-13"
photo5.placeTaken = "Orem Utah"
photo5.image = "/static/homepage/media/Items/glasses.jpg"
photo5.save()

photo6 = hmod.Photograph()
photo6.dateTaken = "1999-04-13"
photo6.placeTaken = "Orem Utah"
photo6.image = "/static/homepage/media/Items/gatlin_gun.jpg"
photo6.save()

photo7 = hmod.Photograph()
photo7.dateTaken = "1999-04-13"
photo7.placeTaken = "Orem Utah"
photo7.image = "/static/homepage/media/Items/barrel.jpg"
photo7.save()

photo8 = hmod.Photograph()
photo8.dateTaken = "1999-04-13"
photo8.placeTaken = "Orem Utah"
photo8.image = "/static/homepage/media/Items/table.jpg"
photo8.save()

##### event photographs #####

photo9 = hmod.Photograph()
photo9.dateTaken = "1999-04-13"
photo9.placeTaken = "Orem Utah"
photo9.image = "/static/homepage/media/Events/civil_war.jpg"
photo9.save()

photo10 = hmod.Photograph()
photo10.dateTaken = "1999-04-13"
photo10.placeTaken = "Orem Utah"
photo10.image = "/static/homepage/media/Events/discussion.jpg"
photo10.save()

photo11 = hmod.Photograph()
photo11.dateTaken = "1999-04-13"
photo11.placeTaken = "Orem Utah"
photo11.image = "/static/homepage/media/Events/teaparty.jpg"
photo11.save()

############## create some users ###############
hmod.User.objects.all().delete()
u = hmod.User()
u.username = "admin"
u.first_name = "James"
u.last_name = "Dayhuff"
u.email = "dayhuffj@gmail.com"
u.phoneNumber = "111-222-3333"
u.address = a
u.set_password("admin")
u.is_superuser = True
u.is_staff = True
u.biographicalSketch = "Contrary to popular belief, Lorem Ipsum is not"
u.secQuestion = "What is your favorite color?"
u.secAnswer = "Green"
u.emergencyContactPhone = "888-999-7777"
u.emergencyContactRelation = "Best friend"
u.photo = photo
u.save()
group1.user_set.add(u)
group1.save()

u = hmod.User()
u.username = "manager"
u.first_name = "Luke"
u.last_name = "Skywalker"
u.email = "manager@skywalker.com"
u.phoneNumber = "111-222-3333"
u.address = a
u.set_password("manager")
u.is_staff = True
u.secQuestion = "What is your favorite color?"
u.secAnswer = "Green"
u.biographicalSketch = "Contrary to popular belief,"
u.save()
group2.user_set.add(u)
group2.save()

u = hmod.User()
u.username = "user1"
u.first_name = "Han"
u.last_name = "Solo"
u.email = "han@thesolo.com"
u.phoneNumber = "111-222-3333"
u.address = a
u.set_password("user")
u.is_agent = True
u.secQuestion = "What is your favorite color?"
u.secAnswer = "Green"
u.biographicalSketch = "Contrary to popular belief, Lorem Ipsum is"
u.save()
group3.user_set.add(u)
group3.save()

u1 = hmod.User()
u1.username = "user2"
u1.first_name = "Chewbaca"
u1.last_name = "Brownback"
u1.email = "normal@brown.com"
u1.phoneNumber = "111-222-3333"
u1.address = a
u1.set_password("user")
u1.is_agent = True
u.secQuestion = "What is your favorite color?"
u.secAnswer = "Green"
u1.is_participant = True
u.biographicalSketch = "Contrary to popular belief, Lorem"
u1.save()
group3.user_set.add(u1)
group3.save()

u = hmod.User()
u.username = "user3"
u.first_name = "Princess"
u.last_name = "Leah"
u.email = "dayhuffj@gmail.com"
u.phoneNumber = "111-222-3333"
u.address = a
u.secQuestion = "What is your favorite color?"
u.secAnswer = "Green"
u.set_password("user")
u.biographicalSketch = "Contrary to popular belief, Lorem Ipsum is"
u.save()
group3.user_set.add(u)
group3.save()

############## create some items ###############


it = hmod.Item()
it.name = "Ben Franklin Glasses"
it.description = "These glasses are the coolest"
it.isRentableItem = True
it.isSellableItem = False
it.value = 30.00
it.STP = 2.00
it.condition = "Slightly Used"
it.owner = u1
it.photo = photo5
it.save()

it1 = hmod.Item()
it1.name = "Barrel"
it1.description = "A barrel for fun"
it1.isRentableItem = True
it1.isSellableItem = False
it1.value = 99.00
it1.STP = 20.00
it1.condition = "Looks New"
it1.owner = u1
it1.photo = photo7
it1.save()


it2 = hmod.Item()
it2.name = "Gatlin Gun"
it2.description = "Just in case"
it2.isRentableItem = True
it2.isSellableItem = False
it2.value = 200.00
it2.STP = 30.00
it2.condition = "Heavily Used"
it2.owner = u1
it2.photo = photo6
it2.save()

it3 = hmod.Item()
it3.name = "Table"
it3.description = "Sturdy"
it3.isRentableItem = True
it3.isSellableItem = False
it3.value = 99.00
it3.STP = 20.00
it3.condition = "Moderately Used"
it3.owner = u1
it3.photo = photo8
it3.save()

############## create some rentals ###############
r = hmod.Rental()
r.memberName = u
r.rentalTime = '2015-02-02'
r.dueDate = datetime.now() - timedelta(days=35)
r.discountPercent = 13
r.handlingAgent = u1
r.creditCard = 333344448888
r.nameOnCard = r.memberName
r.save()

r = hmod.Rental()
r.memberName = u
r.rentalTime = '2014-12-02'
r.dueDate = '2014-12-09'
r.discountPercent = 13
r.handlingAgent = u1
r.creditCard = 333344448888
r.nameOnCard = r.memberName
r.save()

r = hmod.Rental()
r.memberName = u
r.rentalTime = '2015-02-02'
r.dueDate = '2015-01-04'
r.discountPercent = 13
r.handlingAgent = u1
r.creditCard = 333344448888
r.nameOnCard = r.memberName
r.save()

r = hmod.Rental()
r.memberName = u
r.rentalTime = '2015-02-02'
r.dueDate = '2015-02-09'
r.discountPercent = 13
r.handlingAgent = u1
r.creditCard = 333344448888
r.nameOnCard = r.memberName
r.save()

r = hmod.Rental()
r.memberName = u
r.rentalTime = '2015-02-02'
r.dueDate = '2015-02-09'
r.discountPercent = 13
r.handlingAgent = u1
r.creditCard = 333344448888
r.nameOnCard = r.memberName
r.save()

r = hmod.Rental()
r.memberName = u
r.rentalTime = '2015-02-02'
r.dueDate = '2015-02-09'
r.discountPercent = 13
r.handlingAgent = u1
r.creditCard = 333344448888
r.nameOnCard = r.memberName
r.save()

r1 = hmod.Rental()
r1.memberName = u
r1.rentalTime = datetime.now()
r1.dueDate = r1.rentalTime + timedelta(days=7)
r1.discountPercent = 10
r1.handlingAgent = u1
r1.creditCard = 333344448888
r1.nameOnCard = r.memberName
r1.save()

r2 = hmod.Rental()
r2.memberName = u
r2.rentalTime = datetime.now()
r2.dueDate = r2.rentalTime + timedelta(days=7)
r2.discountPercent = 0
r2.handlingAgent = u1
r2.creditCard = 333344448888
r2.nameOnCard = r.memberName
r2.save()

r3 = hmod.Rental()
r3.memberName = u
r3.rentalTime = '2015-03-04'
r3.dueDate = '2015-03-11'
r3.discountPercent = 10
r3.handlingAgent = u1
r3.creditCard = 333344448888
r3.nameOnCard = r.memberName
r3.save()

############# create some rented items ###############
ri = hmod.RentedItem()
ri.rental = r
ri.item = it
ri.save()

ri1 = hmod.RentedItem()
ri1.rental = r1
ri1.item = it1
ri1.save()

ri2 = hmod.RentedItem()
ri2.rental = r2
ri2.item = it3
ri2.save()

ri3 = hmod.RentedItem()
ri3.rental = r2
ri3.item = it2
ri3.save()

ri3 = hmod.RentedItem()
ri3.rental = r2
ri3.item = it
ri3.save()

ri3 = hmod.RentedItem()
ri3.rental = r2
ri3.item = it1
ri3.save()

ri4 = hmod.RentedItem()
ri4.rental = r3
ri4.item = it2
ri4.save()

ri5 = hmod.RentedItem()
ri5.rental = r3
ri5.item = it3
ri5.save()

ri6 = hmod.RentedItem()
ri6.rental = r3
ri6.item = it1
ri6.save()


############## create some products ###############
p = hmod.Product()
p.name = "Wagon"
p.description = "Brown Wagon that works fairly well"
p.isRentableItem = False
p.isSellableItem = True
p.category = "product"
p.currentPrice = 55.00
p.owner = u
p.quantityOnHand = 10
p.photo = photo3
p.dateMade = datetime.now()
p.save()

p = hmod.Product()
p.name = "Gun"
p.description = "Gun that shoots things"
p.isRentableItem = False
p.isSellableItem = True
p.category = "product"
p.currentPrice = 60.00
p.owner = u1
p.quantityOnHand = 99
p.dateMade = datetime.now()
p.photo = photo4
p.save()

p = hmod.Product()
p.name = "Breeches"
p.description = "They feel great when you wear them"
p.isRentableItem = False
p.isSellableItem = True
p.category = "product"
p.currentPrice = 1.00
p.owner = u
p.quantityOnHand = 50
p.photo = photo2
p.dateMade = datetime.now()
p.save()

p = hmod.Product()
p.name = "Cannon"
p.description = "Just in case you need it to defend your castle!"
p.isRentableItem = False
p.isSellableItem = True
p.category = "product"
p.currentPrice = 99.00
p.owner = u1
p.quantityOnHand = 20
p.photo = photo1
p.dateMade = datetime.now()
p.save()





############## create some sale items ###############
v = hmod.Venue()
v.name = "Orem Public Park"
v.location = a1
v.save()

v1 = hmod.Venue()
v1.name = "Scena Park"
v1.location = a2
v1.save()

v2 = hmod.Venue()
v2.name = "Fair Grounds"
v2.location = a1
v2.save()

v3 = hmod.Venue()
v3.name = "Top of Volcano"
v3.location = a2
v3.save()

############## create events ###############
ev = hmod.Event()
ev.name = "Tea Party"
ev.startDate = '2015-06-04'
ev.endDate = '2015-07-20'
ev.mapFileName = "file.doc"
ev.venue = v
ev.photo = photo11
ev.save()

ev1 = hmod.Event()
ev1.name = "American Heritage Discussions"
ev1.startDate = '2016-06-04'
ev1.endDate = '2016-07-20'
ev1.mapFileName = "file.doc"
ev1.venue = v1
ev1.photo = photo10
ev1.save()

ev2 = hmod.Event()
ev2.name = "Revolution Reenactment"
ev2.startDate = '2017-06-04'
ev2.endDate = '2017-07-20'
ev2.mapFileName = "file.doc"
ev2.venue = v2
ev2.photo = photo9
ev2.save()


############## create areas ###############
ar = hmod.Area()
ar.name = "Flexo Zone"
ar.description = "See how flex chords are made"
ar.placeNumber = 1
ar.event = ev
ar.save()

ar1 = hmod.Area()
ar1.name = "Woodworking"
ar1.description = "Build good things."
ar1.placeNumber = 2
ar1.event = ev
ar1.save()

ar2 = hmod.Area()
ar2.name = "Cooking"
ar2.description = "Old school cooking"
ar2.placeNumber = 1
ar2.event = ev1
ar2.save()

############## create some sale items ###############
si = hmod.SaleItem()
si.name = "Horse Shoe"
si.description = "Not good for much, just a little toy"
si.lowPrice = 2.00
si.highPrice = 4.00
si.event = ev
si.save()

si = hmod.SaleItem()
si.name = "Home-made Cinamon Butter"
si.description = "Absolutely Delicious"
si.lowPrice = 8.00
si.highPrice = 15.00
si.event = ev2
si.save()

si2 = hmod.SaleItem()
si2.name = "Musket Ball"
si2.description = "Cool ball of musket"
si2.lowPrice = 3.00
si2.highPrice = 8.00
si2.event = ev1
si2.save()

si = hmod.SaleItem()
si.name = "Huge Hat"
si.description = "Stuff and stuff and blah"
si.lowPrice = 38.00
si.highPrice = 59.00
si.event = ev1
si.save()

















