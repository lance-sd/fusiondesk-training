INSERT INTO Tickets (ClientID, AssignedUserID,  Title, Description, Status, Priority, CreatedDate, ClosedDate)
VALUES
(3,2,'Shared drive access denied', 'The auditors cannot open the link to the shared drive', 'In Progress', 'High', '2026-09-21', NULL),
(5, 1, 'Printer offline', 'The printer in sales is offline, so no one can print', 'In Progress', 'Normal', '2026-09-23', NULL),
(4, 3, 'Software license renewal needed', 'Users are getting a pop up notification about, our CRM needing renewal', 'New', 'High', '2026-09-23', NULL),
(2, 1, 'New employee laptop setup', 'We have a new employee starting next, can we have a laptop ready for them before next week Wednesday', 'New', 'Low', '2026-09-22', NULL),
(4, 2, 'Backup job failed overnight', 'I got a notification that the server''s back up failed last night, can we urgently have a look at it', 'Closed', 'High', '2026-09-15', '2026-09-16'),
(3, 1, 'Cannot connect to office Wifi', 'We have internet on Lan but there''s no internet on Wifi', 'Closed', 'High', '2026-09-17', '2026-09-17'),
(5, 1, 'Blue screen error on restart', 'I''ve tried restarting a couple of times now, and I''m still getting a BSOD', 'Closed', 'High', '2026-09-20', '2026-09-21'),
(1,3, 'Request for additional RAM upgrade', 'We notice one of the programs on the sewing machine is resource hungry, can we please get a RAM upgrade on it', 'Waiting for parts', 'Normal', '2026-09-22', NULL),
(1,3, 'Slow network speeds in accounts department', 'Ladies in finance are complaining saying their internet speeds are slow', 'Closed', 'Normal', '2026-08-31', '2026-09-04'),
(2,2, 'VPN connection dropping intermittently', 'Many users are reporting that their not able to work from home because the vpn keeps on dropping', 'New', 'High', '2026-09-25', NULL),
(2, 2, 'Two factor authentication not working', 'When I''m trying to logged into our client portal, I''m not receiving a login code', 'In Progress', 'Low', '2026-09-19', NULL),
(4, 1, 'Email bouncing back to sender', 'When we trying to send invoices out invoices, they keep bouncing back', 'Closed', 'High', '2026-09-19', '2026-09-20'),
(3,3, 'Outlook keeps freezing', 'Everytime I try opening attachments, outlook keeps freezing', 'New', 'Low', '2026-09-23', NULL),
(3,3, 'Password reset request', 'I''ve locked myself out of the office app, can you please reset my password', 'Closed', 'Normal', '2026-07-25', '2026-07-25');
