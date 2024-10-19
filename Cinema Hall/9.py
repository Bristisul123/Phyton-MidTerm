class Star_Cinema:
    def __init__ (self):
       self._hall_list= []


    def entry_hall(self,hall):
        self._hall_list(hall)

class Hall(Star_Cinema):
    def __init__(self,row,col, hall_no):
        self._seats = {}
        self._show_list = []
        self._row = row
        self._col = col
        self._hall_no = hall_no       



    def entry_show(self,id,movie_name,time):
        show = (id,movie_name,time)
        self._show_list.append(show)

        seat_allocation = []

        for row in range(self._row):
            seat_row = []
            for col in range(self._col):
                seat_row.append(0)
            seat_allocation.append(seat_row) 

        self._seats[id] = seat_allocation 



    def book_seats(self,id,seat_list):
        if id not in self._seats:
             print(f"The id {id} is not found")    
             return 
        
        seat_allocation = self._seats[id]

        for seat in seat_list:
            row ,col = seat
            if row >= self._row or col >= self._col:
                print(f"Seat ({row},{col}) is not found")
                continue
            if seat_allocation[row][col] == 1:
                print(f"Seat ({row},{col}) is already booked")

            else:
                seat_allocation[row][col] = 1
                print(f"Seat ({row},{col}) is booked successfully")
                
       
             
    def view_show_list(self):
        if not self._show_list : 
            print(f"No show is running")

        else :
            print(f"The running shows in hall {self._hall_no} :")
            for show in self._show_list:
                show_id, movie_name,time = show
                print(f"Show Id : {show_id}, Movie :{movie_name}, time :{time}")



    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print(f"Show ID {show_id} not found.")
            return

        seat_layout = self._seats[show_id]

        print(f"Available seats for Show ID {show_id} are:")
        available_seats = []
        for row in seat_layout:
            print(" ".join(map(str,row)))


class Counter :
    def __init__(self,hall):
        self._hall = hall

    def view_all_shows(self):
        self._hall.view_show_list()

    def view_available_seats(self,show_id):
       self._hall.view_available_seats(show_id)


    def book_ticket(self,show_id, row,col):
         s = self._hall.book_seats(show_id,[(row,col)])
        


hall = Hall(5, 5, 101) 
hall.entry_show(111, "Jigra", "2PM")
hall.entry_show(112, "Avtar", "9PM")
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





