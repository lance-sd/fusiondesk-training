def tech_number_tickets():
    name = input("What is your name?:" ).strip().title()  
    department = input("what department do you work in?:" )
    number_of_tickkets = int(input("How many tickets do you have open?:" ))
    return(f"{name} from {department} has {number_of_tickkets} open tickets")