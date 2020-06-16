# To change this license header, choose License Headers in Project Properties
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == “__main__”:

    import calendar
    year = int(input("Enter of this year: "))
    calendar.prcal(year)
    
    from time import time, ctime
    
    prev_time = ""
    while True:
        the_time = ctime(time())
        if prev_time != the_time:
            print ("Now of this time:", ctime(time())
            prev_time = the_time
