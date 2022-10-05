INSERT INTO clients (username, password, loyalty_points, joined_on) VALUES('user1', 'pass1', 23, '2020-01-01'), 
('user2', 'pass2', 233, '2021-02-02'), ('user3', 'pass3', 26, '2020-03-03'), ('user4', 'pass4', 50, '2022-05-05'), 
('user5', 'pass5', 123, '2021-06-06');


SELECT username, loyalty_points, joined_on FROM clients;

CALL get_client_info();