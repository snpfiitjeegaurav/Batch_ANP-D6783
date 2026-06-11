# Problem 1: Smart Railway Reservation System
# Problem Statement
# A railway reservation system stores the booking status of seats in a train coach.
# Sample Data
# seats = {
#  1: "Booked",
#  2: "Available",
#  3: "Booked",
#  4: "Available",
#  5: "Booked",
#  6: "Booked",
#  7: "Available",
#  8: "Booked",
#  9: "Available",
#  10: "Booked"
# }
# Tasks
# 1. Display all available seat numbers.
# 2. Count booked and available seats.
# 3. Reserve the first available seat.
# 4. Cancel booking for a given seat number.
# 5. Store the updated reservation status in reservations.txt.
# 6. Display occupancy percentage.
# Sample Output
# Available Seats:
# 2 4 7 9
# Booked Seats: 6
# Available Seats: 4
# Seat 2 Reserved Successfully.
# Occupancy Percentage: 70.0%
# Reservation Details Saved Successfully.

#creating dictionary of booking status
booking_status = {1:"booked",2:"available",3:"booked",4:"available",5:"booked",6:"booked",7:"available",8:"booked",9:"available",10:"booked"}
#1. Display all available seat numbers. 
for items in booking_status:
    if booking_status[seat_num] == "available":
        print(seat_num, end=" ")
    else:
        pass
print("\n" + "-"*30)
#2. Count booked and available seats. 
booked_seats = 0
available_seats = 0
for items in booking_status:
    if booking_status[seat_num] == "":
        "available"
        available_seats += 1
    elif booking_status[seat_num] == booked:
        booked_seats += 1
    else:
        print("invalid status")
print("booked seats: ", available_seats)
print("available seats: ", available_seats)
print("-"*30)
#3. Reserve the first available seat. 
for items in booking_status:
    if booking_status.[seat_num] == "available":
        booking_status[seat_num] = "booked"
        print(f"seat {seat_num} resrved successfully")
        available_seats -= 1
        booked_seats += 1
        break
print("-"*30)
#4. Cancel booking for a given seat number. 
seat_to_cancel = int(input("seat to be cancelled: "))
if seat_to_cancel in booking_status:
    if booking_status[seat_to_cancel] == "booked":
        booking_status[seat_to_cancel] = "available"
        print(f"booking for seat {seat_to_cancel} cancelled successfully")
        available_seats += 1
        booked_seats -= 1
    else:
        print(f"{seat_to_cancel} is already available.")
else:
    print{"invalid seat no."}
print("-"*30)
# -------------------------------------------------------------
# 5. Store the updated reservation status in reservations.txt.
# -------------------------------------------------------------

# for keys in booking_status:
#     if booking_status.values == booked
#         booking_status.values == available
#         break
#     elif booking_status.values == available
#         booking_status.values == booking_status.values
#     else:
#         pass
#     break
#store the updated reservation status in reservations.txt. 

#Display occupancy percentage. 
occupancy_percentage = booked_seats/(booked_seats + available seats)*100
print("occupancy percentage is: ", occupancy_percentage)