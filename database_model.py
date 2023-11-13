# Ben: implement get function to pull data from database
from config import *

##### Template
        # mycursor = conn.cursor()
        # sql = ""
        # mycursor.execute(sql)
        # result = mycursor.fetchall()
        # return result   


############################ Pull Data from DB #############################
    # db connection function
def connect_db():
    conn = mysql.connector.connect(user=CONFIG_USER, password=CONFIG_PASSWORD,host=CONFIG_HOST,database=CONFIG_DATABASE)
    return conn

    ## Usage: for the redirection of the mainpage button 
    ## Variable: user_id
    ## Return: is there any course that will be started in an hours
    ## Return Type: Boolean
def get_is_course_start_in_an_hour(conn, user_id, time, weekday):
        #### Dummy Template (time should be range not equal)
        mycursor = conn.cursor()
        sql = """select count(*) as is_class from Registercourses rc 
        join Coursetimeslots cs on rc.course_id = cs.course_id 
        where rc.user_id = '""" + user_id +"""' 
        and  cs.start_time = '""" + time +"""' 
        and cs.day_in_week = '""" + weekday +"""' 
        """
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for row in result:
            return row[0]

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


# Testing
# conn= connect_db()
# print(get_is_course_start_in_an_hour(conn))
