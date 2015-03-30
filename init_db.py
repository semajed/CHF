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
photo.image = "/static/homepage/media/CannonFinished.jpg"
photo.save()

############## create some users ###############
hmod.User.objects.all().delete()
u = hmod.User()
u.username = "admin"
u.first_name = "Jabba"
u.last_name = "Hut"
u.email = "admin@admin.com"
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
u1.is_participant = True
u.biographicalSketch = "Contrary to popular belief, Lorem"
u1.save()
group3.user_set.add(u1)
group3.save()

u = hmod.User()
u.username = "user3"
u.first_name = "Princess"
u.last_name = "Leah"
u.email = "ima@princess.com"
u.phoneNumber = "111-222-3333"
u.address = a
u.set_password("user")
u.biographicalSketch = "Contrary to popular belief, Lorem Ipsum is"
u.save()
group3.user_set.add(u)
group3.save()

############## create some rentals ###############
r = hmod.Rental()
r.memberName = u
r.rentalTime = datetime.now()
r.dueDate = r.rentalTime + timedelta(days=7)
r.discountPercent = 10
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
r.rentalTime = datetime.now()
r.dueDate = r.rentalTime + timedelta(days=7)
r.discountPercent = 0
r.handlingAgent = u1
r.creditCard = 333344448888
r.nameOnCard = r.memberName
r.save()

r = hmod.Rental()
r.memberName = u
r.rentalTime = '2015-03-04'
r.dueDate = '2015-03-11'
r.discountPercent = 10
r.handlingAgent = u1
r.creditCard = 333344448888
r.nameOnCard = r.memberName
r.save()



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
p.photo = photo
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
p.photo = photo
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
p.photo = photo
p.dateMade = datetime.now()
p.save()

p = hmod.Product()
p.name = "Coat"
p.description = "Warm summer coat"
p.isRentableItem = False
p.isSellableItem = True
p.category = "product"
p.currentPrice = 99.00
p.owner = u1
p.quantityOnHand = 20
p.photo = photo
p.dateMade = datetime.now()
p.save()


############## create some items ###############
it = hmod.Item()
it.name = "Barrel"
it.description = "A barrel for fun"
it.isRentableItem = True
it.isSellableItem = False
it.value = 99.00
it.STP = 20.00
it.condition = "Looks New"
it.owner = u1
it.save()

it = hmod.Item()
it.name = "Shoes"
it.description = "Aren't very comfortable, beware"
it.isRentableItem = True
it.isSellableItem = False
it.value = 30.00
it.STP = 2.00
it.condition = "Slightly Used"
it.owner = u1
it.save()

it = hmod.Item()
it.name = "Gatlin Gun"
it.description = "Just in case"
it.isRentableItem = True
it.isSellableItem = False
it.value = 200.00
it.STP = 30.00
it.condition = "Heavily Used"
it.owner = u1
it.save()

it = hmod.Item()
it.name = "Table"
it.description = "Sturdy"
it.isRentableItem = True
it.isSellableItem = False
it.value = 99.00
it.STP = 20.00
it.condition = "Moderately Used"
it.owner = u1
it.save()


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
ev.name = "Colonial Party"
ev.startDate = '2015-06-04'
ev.endDate = '2015-07-20'
ev.mapFileName = "file.doc"
ev.venue = v
ev.save()

ev1 = hmod.Event()
ev1.name = "American Heritage Discussions"
ev1.startDate = '2016-06-04'
ev1.endDate = '2016-07-20'
ev1.mapFileName = "file.doc"
ev1.venue = v1
ev1.save()

ev2 = hmod.Event()
ev2.name = "Revolutino Reenactment"
ev2.startDate = '2017-06-04'
ev2.endDate = '2017-07-20'
ev2.mapFileName = "file.doc"
ev2.venue = v2
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
si.area = ar
si.save()

si = hmod.SaleItem()
si.name = "Home-made Cinamon Butter"
si.description = "Absolutely Delicious"
si.lowPrice = 8.00
si.highPrice = 15.00
si.area = ar2
si.save()

si = hmod.SaleItem()
si.name = "Musket Ball"
si.description = "Cool ball of musket"
si.lowPrice = 3.00
si.highPrice = 8.00
si.area = ar1
si.save()

si = hmod.SaleItem()
si.name = "Another Thing"
si.description = "Stuff and stuff and blah"
si.lowPrice = 38.00
si.highPrice = 59.00
si.area = ar1
si.save()

















