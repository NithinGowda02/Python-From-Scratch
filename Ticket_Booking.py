"""
**Ticket Booking Simulation**:
   - Write a program that simulates a bus ticket booking system. The bus has 8 seats. Each time a seat is booked, the available seats decrease. When there are no seats left, the loop stops and displays a message saying "All seats are booked.
"""
Availaible_seats = 8
while Availaible_seats > 0:
    book_seat = input(f"Book bus ticket.Type (yes) to book (Availaible seat >{Availaible_seats})  >>")
    if book_seat == "yes":
        print(f"Seat Booked Successfully. Availaible Seats >> {Availaible_seats}")
        Availaible_seats = Availaible_seats - 1
print("All seats are booked")        