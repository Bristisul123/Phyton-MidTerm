class Star_Cinema:
    hall_list= []

    def entry_hall(self,hall):
        self.hall = hall

class Hall(Star_Cinema):
    def __init__(self,row,col, hall_no):
        self.seats = {}
        self.show_list = []
        self.row = row
        self.col = col
        self.hall_no = hall_no       

    def entry_show(self,id,movie_name,time):
        show = (id,movie_name,time)
        self.show_list.append(show)

        seat_allocation = []
        for row in range(self.row):
            seat_row = []
            for col in range(self.col):
                seat_row.append(0)
            seat_allocation.append(seat_row) 

        self.seats[id] = seat_allocation   

    def book_seats(self,id,seat_list):
        if id not in self.seats:
             print(f"The id {id} is not found")    
             return 
        
        seat_allocation = self.seats[id]

        for seat in seat_list:
            row , col = seat
            if row >= self.row or col >= self.col:
                print(f"Seat is not found")
                continue
            if seat_allocation[row][col] =='booked':
                print(f"Seat ({row},{col}) is already booked")

            else:
                seat_allocation[row][col] = 'booked'
                print(f"Seat ({row},{col}) is booked successfully")
                
hall1 = Hall(5, 5, 101) 
hall1.entry_show("1", "Jigra", "2PM")
hall1.entry_show("2", "Avtar", "9PM")

Seat_booking = [(1, 2), (0,0)]  
hall1.book_seats("2", Seat_booking)

for row in hall1.seats["1"]:
    print(row)