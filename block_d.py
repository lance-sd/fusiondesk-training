import json


# Creates a list of 5 ticket dictionaries, each with title, priority, and status
tickets = [
    {"title": "VPN not working", "priority": "medium", "status": "pending"}
    {"title": "Can't access sharepoint", "priority": "low", "status": "closed"}
    {"title": "slow pc", "priority": "unknown", "status": "new"}
    {"title": "cameras are offline", "priority": "high", "status": "pending"}
    {"title": "printer offline", "priority": "low", "status": "closed"}
]


# Loops through and prints only the tickets where status == "open"

for ticket in tickets:
    if "status" == "open":
        print (f"'title': {ticket['title']}, 'priority': {ticket['priority']}, 'status': {ticket['status']}")




# Counts how many tickets are "high" priority

high_priority_count = 0
for  ticket in tickets:
    if ticket["priority"] == "high":
        high_priority_count = high_priority_count + 1    # or high_priority_count += 1

print(f"Number of hight priority tickets = {high_priority_count}")



# Sorts the list alphabetically by title — hint: look up sorted() with a key parameter

sorted_tickets = sorted(tickets, key=lambda ticket: ticket['title'] )    #lambda =  #def get_title(ticket) return ticket["title"]
for ticket in sorted_tickets:
    print(ticket['title'])


def load_contacts():
    # Try to open contacts.json and return the contents
    # If FileNotFoundError return an empty list

def save_contacts(contacts):
    # Write the contacts list to contacts.json