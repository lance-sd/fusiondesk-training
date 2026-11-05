SELECT Clients.ClientID, Company_Name, COUNT(TicketID) AS Tickets_Per_Client
FROM Clients
LEFT JOIN Tickets ON Clients.ClientID = Tickets.ClientID
GROUP BY Clients.ClientID, Company_Name;