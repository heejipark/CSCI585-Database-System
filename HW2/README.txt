Hee Ji Park
Oracle DB (https://livesql.oracle.com/)

CONDITION
- I added a 'meeting_date' column to the meeting table.
- Employees who did self-report should conduct the COVID test.
- Employees who did scan test should conduct the COVID test.
- Notifications are sent in batches at 11:59PM on the same day that one employee has POSITIVE as a result of the COVID test.
- In Q3, I define 'sickest floor' as the floor with the highest number of positive patients so far.
- In Q4, The period were divided into the first half of September and the second half of September.
- In Q5, I made two queries. One of them involves 'table division.'
- Q5-2. Using 'Table division' : Extract the IDs of employees who have both positive and negative results in the COVID test.
	- Table 'T1':(SELECT EID, test_result FROM test) 
	- Table 'ts':(SELECT distinct(test_result) FROM test)
	- As a result, I try to calculate 'T1 % ts'.