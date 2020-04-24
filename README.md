# LoginRadiusPollsApp

Download the project into local machine. 

create an virtual environment using 'virtualenv' command

install all requirements.txt dependencies

now enter into the folder containing manage.py run command 'python3 manage.py runserver <port>' <port> is not mandatory it is by default 8000.
  
now you can access the site '127.0.0.1:<port>'
  
1. Requirement 1:
   User visits the URL and User logs in (Email/Password login). A list of candidates will be shown
   new users can be created http://127.0.0.1:8001/admin/login/?next=/admin/ use username: admin@gmail.com password:Admin@123
   
   you can see the login tab and enter the user name and password. Here username is 'pollsuser1@gmail.com' password:'user@123'
   
   
2.Requirement 2:
  They can vote for a candidate by clicking a button
  
  here for the sake of testing i have given dummy names you can click on the radio button and submit to ensure vote is done.
  
3. Requirement 3:
   We have to keep track of the votes in the database

   I have ensured a model consisting of contestant and votes polled.
   
3. Requirement4:
   Admin User can log in and check the votes per candidate
   
   when you enter admin credentials as mentioned above you can see results page. where number of votes polled is shown in the 
   table like form.
   
