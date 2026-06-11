import datetime
import calendar
now = datetime.datetime.now()
city = input("Input city name: ")
print("City: ", city)
print("Time now:", now)
print(calendar.calendar(now.year))
#Distance fare
distance = int(input("Input your distance: "))
if distance <= 50:
    fare = 50
elif distance <= 100:
    fare = 100
elif distance <= 200:
    fare = 180
elif distance <= 300:
    fare = 290
else:
    fare = 400

ticket_type = input("Enter your ticket type [student/regular/vip]: ").lower()
if ticket_type == "student":
    discount = 20
elif ticket_type == "regular":
    discount = 0
elif ticket_type == "vip":
    discount = 0
    fare=+200
else:
    print("Input a valid ticket type")

if fare>0:
    final_fare = fare-(fare*discount/100)
    print("Ticket Summary")
    print("Distance: ", distance)
    print("Discount: ", discount)
    print("Final Fare", final_fare)
