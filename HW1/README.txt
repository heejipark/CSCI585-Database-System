Hee Ji Park
CSCI585 Database System - HW1 - Covid-19 tracking system database

-----------------------------------------------------------------------------------------------------------------------------------------------
ERD entity and relationship (* [table name])  

- [COMPANY] contains [EMPLOYEE].
- [MOVEMENT] is recorded by [EMPLOYEE] through the app.
- [EMPLOYEE] fills out [SELF_REPORT] through the app.
- [TEST_LOCATION] is one of the parts of [SELF_REPORT].
- Data about people who tested positive [POSTIVE] are extracted from [SELF_REPORT].
- [DAILY_CHECK] is recorded daily by people who tested positive [POSITIVE].


-----------------------------------------------------------------------------------------------------------------------------------------------
Highlight and Assumptions  

1. As it is a COVID-19 contact tracking system in a building, each building has a different database.
2. There are several companies and meeting rooms per floor in each building. All companies can use meeting rooms on other floors as well as on their own floors.
3. For COVID-19 contact tracking, each company's employees must sign up for the tracking system. Also, they should provide their company code, employee identification number, mobile phone number and optionally an email address when signing up.
4. Assume that people can get COVID-19 several times.
5. The company would randomly scan employees as they enter the building or when they exit, taking their temperature.
    - 1) If a high temperature is detected at this time, the employees must do a self-report through their app and then get a COVID-19 test, which is to catch pre-symptomatic cases. After the COVID-19 test, they have to update their information on when and where they were tested and the test results through the app again.
    - 2) Sometimes, even though they do not have a fever, they must get a COVID test, which is to catch asymptomatic cases. In this case as well, the employees must write a self-report through the app and then get a COVID-19 test. After the test, they have to update their information on when and where they were tested and the test results through the app again. (* In this case, when filling out a self-report via the app, they can select 'No' when asked if you have had any symptoms of COVID-19.) (ex) COVID-19_SYMTOMS = No
6. If an employee personally conducts a COVID-19 test without going through the company and the result is positive, the employee must fill out a self-report through the app.
7. It is assumed that some data of employees who had the positive result for the COVID-19 test and filled out self-report on the app are automatically inserted into the [POSITIVE] table every midnight. (ex) some data => report ID and positive diagnosis date


-----------------------------------------------------------------------------------------------------------------------------------------------
Entities and Attributes

1. [COMPANY]: This table stores the company's code, name, address, floor, and room number.
2. [EMPLOYEE]: This table contains information on employees. Basically, it contains the ID ('EMPLOYEE_SYS_ID') and password ('EMPLOYEE_SYS_PWD') created when employees signed up for the COVID-19 contact tracking system. It also has the company code and employee identification number to determine which company this employee belongs to. In addition, it has a mobile phone number and email information to be contacted in case of contact with a COVID patient.
3. [MOVEMENT]: This table is for tracking the movements of employees. First of all, whenever employees report their movements, a new index is created and this becomes the primary key of this table. In addition, in order to determine which meeting room was used by which employee, the employee’s system ID, the meeting room number, the floor where the meeting room is located, and the time schedule are needed. Those are provided by employees through the app.
4. [SELF_REPORT]: This table contains self-report information about COVID-19 by employees through the app. This also automatically generates an index every time a self-report is made, which becomes a primary key. Employees will first self-report their tracking system ID and whether they have experienced at least one of the five symptoms of COVID (Yes/No). After conducting the COVID-19 test, they have to update their record again. The list of records to be updated includes the date when they were tested, where they were tested, what was the result, and the date the result was diagnosed.
5. [TEST_LOCATION]: This table contains information about places where employees can get a COVID-19 test. For example, LA Public Health Center, Irvine Health Center, In-company Pharmacy, etc. Details include the name, address and phone number of the place.
6. [POSITIVE]: This table contains information about employees who have tested positive for COVID-19 in the [SELF_REPORT] table. The index called 'CONFIRMED_CASE_ID' is set as a primary key, and the 'REPORT_ID' from the [SELF_REPORT] table will be a foreign key. This table also contains the COVID-19 diagnosis date ('TEST_DIAGNOSIS_DATE'), recovery status ('RECOVERED_TF'), and recovery date ('RECOVERED_DATE'). Later on, if the patient's covid-19 symptoms improve, the recovered date ('RECOVERED_DATE') will be updated, and immediately the value of 'RECOVERED_TF' will be updated from False to True. (The default value of attribute 'RECOVERED_TF' is False and the default value of attribute 'RECOVERED_DATE' is NULL.)
The value of the [POSITIVE] table will be inserted using this SQL syntax: 
	insert into POSITIVE 
	select report_id, test_diagnosis_date
	from SELF_REPORT 
	where test_result = 'Positive'

7. [DAILY_CHECK]: People who are positive for the COVID-19 test have to report their daily status check for 2 weeks during self-quarantine. So, this table contains information on their daily status and date. Also, 'CONFIRMED_CASE_ID' from the [POSITIVE] table will be a foreign key.

