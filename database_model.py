# Ben: implement get function to pull data from database
from config import *

##### Template
        # mycursor = conn.cursor()
        # sql = ""
        # mycursor.execute(sql)
        # result = mycursor.fetchall()
        # return result   


############################ Pull Data from DB #############################
class database_model:
    # db connection function
    def connect_db():
        conn = mysql.connector.connect(user=CONFIG_USER, password=CONFIG_PASSWORD,host=CONFIG_HOST,database=CONFIG_DATABASE)
        return conn

    ## Usage: for the redirection of the mainpage button 
    ## Variable: user_id
    ## Return: is there any course that will be started in an hours
    ## Return Type: Boolean
    def get_is_course_start_in_an_hour(conn, user_id):
        pass
        ##### Template
        # mycursor = conn.cursor()
        # sql = ""
        # mycursor.execute(sql)
        # result = mycursor.fetchall()
        # return result   

    ## Usage: for the redirection of the mainpage button 
    ## Return: is there any course that will be started in an hours
    ## Return Type: Array
    def get_user_data():
        pass

    ## Usage: get course data in course table
    ## Return: ....
    ## Return Type: Array
    def get_course_data():
        pass

    ## Usage: get course time table of an user
    ## Return: ....
    ## Return Type: Array
    def get_course_timetable():
        pass

    ############################ Update Data from DB #############################
    ##Usage: Update the login time of user after login
    def update_login_time():
        pass