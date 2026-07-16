# Creates a list of 5 ticket dictionaries, each with title, priority, and status
tickets = [
    {"title": "VPN not working", "priority": "medium", "status": "pending"},
    {"title": "Can't access sharepoint", "priority": "low", "status": "closed"},
    {"title": "slow pc", "priority": "unknown", "status": "new"},
    {"title": "cameras are offline", "priority": "high", "status": "pending"},
    {"title": "printer offline", "priority": "low", "status": "closed"}
]


# Loops through and prints only the tickets where status == "open"

for ticket in tickets:
    if "status" == "open":
        print (f"'title': {ticket['title']}, 'priority': {ticket['priority']}, 'status': {ticket['status']}")


















# Counts how many tickets are "high" priority
# Sorts the list alphabetically by title — hint: look up sorted() with a key parameter