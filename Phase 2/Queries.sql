USE FusionDesk;

-- Query 1: All open tickets (anything not Closed), newest first
SELECT * FROM Tickets
WHERE Status != 'Closed'
ORDER BY CreatedDate DESC;

-- Query 2: Ticket count per client
SELECT ClientID, COUNT(ClientID) AS Tickets_Per_Client
FROM Tickets
GROUP BY ClientID;

-- Query 3: High-priority tickets assigned to a specific user (UserID 2)
SELECT AssignedUserID, Title, Status, Priority
FROM Tickets
WHERE AssignedUserID = 2 AND Priority = 'High';

-- Query 4: Average days-to-close for closed tickets
-- (* 1.0 forces decimal arithmetic, otherwise SQL Server truncates the average to a whole number)
SELECT AVG(DATEDIFF(day, CreatedDate, ClosedDate) * 1.0) AS AvgDaysToClose
FROM Tickets
WHERE Status = 'Closed';