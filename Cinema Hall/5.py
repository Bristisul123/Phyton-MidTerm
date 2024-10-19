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
            if seat_allocation[row][col] ==1:
                print(f"Seat ({row},{col}) is already booked")

            else:
                seat_allocation[row][col] = 1
                print(f"Seat ({row},{col}) is booked successfully")

    def view_show_list(self):
        if not self.show_list : 
            print(f"No show is running")

        else :
            print(f"The running shows in hall {self.hall_no} :")
            for show in self.show_list:
                show_id, movie_name,time = show
                print(f"Show Id : {show_id}, Movie :{movie_name}, time :{time}")


hall1 = Hall(5, 5, 101) 
hall1.entry_show(1, "Jigra", "2PM")
hall1.entry_show(2, "Avtar", "9PM")

hall1.view_show_list()