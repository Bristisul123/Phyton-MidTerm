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
            row = seat
            col = seat
            if row >= self.row or col >= self.col:
                print(f"Seat ({row},{col}) is not found")
                continue
            if seat_allocation[row][col] == 1:
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



    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print(f"Show ID {show_id} not found.")
            return

        seat_layout = self.seats[show_id]

        print(f"Available seats for Show ID {show_id} are:")
        available_seats = []
        for row in seat_layout:
            print(" ".join(map(str,row)))


class Counter :
    def __init__(self,hall):
        self.hall = hall

    def view_all_shows(self):
        self.hall.view_show_list()

    def view_available_seats(self,show_id):
       self.hall.view_available_seats(show_id)


    def book_ticket(self,show_id, row,col):
         s = self.hall.book_seats(show_id,[(row,col)])
        


hall = Hall(5, 5, 101) 
hall.entry_show(1, "Jigra", "2PM")
hall.entry_show(2, "Avtar", "9PM")
counter = Counter(hall)

run = True
while run :
    print("\nOptions:\n")
    print("1 : Show all shows today")
    print("2 : View Available Seats")
    print("3 : Book Ticket")
    print("4 : Exit")

    ch = int(input("\nEnter Option : "))

    if ch == 1:
        counter.view_all_shows()
    elif ch == 2:
        show_id = int(input("Enter the show ID to view available seats: "))
        counter.view_available_seats(show_id)
    elif ch == 3:
        show_id = int(input("Enter the show ID to book seats: "))
        row = int(input("Enter row number: "))
        col = int(input("Enter column number: "))
        counter.book_ticket(show_id, row, col)
    elif ch == 4:
        run = False
    else:
        print("Try Again ")





