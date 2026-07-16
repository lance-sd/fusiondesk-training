#Excercise 1
def celcius_to_fahrenheit(celcius):
    return(celcius * 1.8 + 32)

celcius_to_fahrenheit(15)

def is_valid_email(email):
    return("@" in email and "." in email)
is_valid_email("lancefusiongroup.co.za")

def ticket_status_label(status):
    if status = "Open":
        return "🟡 Open"
    elif status = "In Progress":
        return "🔵 In Progress"
    elif status = "Closed":
        return "🟢 Closed"
    else:
        return "⚪ Unknown"
    
#Exercise 2
def safe_divide(a, b):
    try:
        a / b
    except ZeroDivisionError:
        print("You cannot divide by 0")

