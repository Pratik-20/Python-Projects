#Take a phonenumber from user and show its operator ,region these details.

#pip install phonenumbers
import phonenumbers
#Load geocoder file 
from phonenumbers import geocoder,carrier,timezone
#take phonenumber as a  input as "+917066884590"
n1= input("Please Enter Your Number along with Contry Code")
#Run respextive command to pass no 
phoneNumber = phonenumbers.parse(n1)
# To obtain timezone use this command along eith its operator
timeZone= timezone.time_zones_for_number(phoneNumber)
Carrier= carrier.name_for_number(phoneNumber,'en')

Region= geocoder.description_for_number(phoneNumber,'en')
#print all details
print(phoneNumber)
print(timeZone)
print(Carrier)
print(Region)
