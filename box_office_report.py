# Matthew Cires 
#CMP 131
#Lab -01
#Week 4 
#9/11/26
#box_office_report.py
movie = input("enter the movie title")
aticket = int(input("enter number of adult"))
cticket=int(input("enter number of child"))
adultrevenue = aticket * 10
childrevenue = cticket * 6
Gbox= adultrevenue + childrevenue
Netbox=Gbox*0.2
Amount=Gbox-Netbox
print("Box office report")
print("------------------")
print("movie name :",movie)
print("adult revenue: $", format(adultrevenue, ".2f"))
print("child revenue: $", format(childrevenue,".2f"))
print("gross revenue : $", format(Gbox, ".2f"))
print("theater amount: $", format(Netbox, ".2f"))
print("distributor amount: $", format(Amount,".2f"))
