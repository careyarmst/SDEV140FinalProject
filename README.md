# SDEV140FinalProject
Final Project for SDEV140 CEA
	What is the purpose of the Application? The application will take as input (read in) a standard output of SQL Server security/user data and pull out the relevant data for review in a nice little formatted GUI window and hopefully generate a PDF. So far it generates the data I am looking for and saves it to a text file. But it is getting what I need from the output. I need to add the output window and see if I can get the text output to a PDF. 
	List the reason you are creating the Application. As I am ultimately taking this class/getting this degree to assist with my job, one of my main objectives is to learn to automate some of the tasks my team & I have at work. This SQL Script & it’s output was designed by me (and it meets our objectives and our external auditor (PwC’s) objectives) but because of their desire to have something that is not complicated, does not involve extensive exclusions/filters of data, does not obscure what it is doing, etc. it is very simple by design – it uses T-SQL commands and very simple loops to essentially “dump” a bunch of user & group data about SQL Server. Unfortunately, by design, that means that it also includes a lot of extraneous data that isn’t really necessary but is there to show that the output is complete. I am not able to / allowed to actually alter the SQL script ITSELF (the whole purpose is that that script is comprehensive) but I can make it easier to review – right now people are trying to use MS Excel or Notepad++ but I think it could be easier to do
