CREATE TABLE Tickets(
TicketID int identity(1,1) PRIMARY KEY,
ClientID int references Clients(ClientID),
AssignedUserID int references Users(UserID),
Title varchar(50),
Description varchar(500),
Status varchar(20),
Priority varchar(15),
CreatedDate DATE,
ClosedDate DATE)