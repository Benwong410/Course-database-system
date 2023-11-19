import smtplib, ssl
from datetime import datetime, timedelta
from email.message import EmailMessage

def getUserInfo(conn, user_id):
	sql_select_Query = "SELECT user_name, email from users where user_id = " + str(user_id)
	cursor = conn.cursor(dictionary = True)
	cursor.execute(sql_select_Query)
	info = cursor.fetchall()[0]
	return info

def CourseInfoCheck (connect):
    cursor = connect.cursor()
    now = datetime.now()
    now_time = datetime.strptime(datetime.strftime(now,'%H:%M'),'%H:%M')
    
    query = """
		SELECT DISTINCT T.start_time, T.weekday, students.name, users.email
		FROM coursetimeslots AS T, takes, (SELECT student.user_name, student.user_id
		FROM (SELECT users.user_name, students.user_id
		FROM users, students
		WHERE users.user_id = students.user_id) AS student) AS S, students, users
		WHERE T.course_id = takes.course_id AND takes.user_id = T.course_id AND S.user_id = users.user_id AND S.user_name = users.user_name;
	"""
    
    cursor.execute(query)
    student = cursor.fetchall()
	##time = str(hour) + ":"+ str(minute).zfill(2)
    for timing in student:
        if (timing[1] == int(now.weekday() + 1)):
            time = datetime.strptime(datetime.strftime(datetime.strptime(timing[0],'%H:%M'), '%H:%M'),'%H:%M')
            time_difference = (time - now_time).seconds
            if (time_difference<=3600):
                send_email(timing[2], str(timing[1]), timing[3])


def send_email(receiver_email, conn, user_id, course_id, isTeacher, start_time):
    # email configuration
    mail_host = "smtp.gmail.com"
    mail_user = EMAIL_ACCOUNT
    mail_pass = EMAIL_PASSWORD
 

    # Get user info
    info = getUserInfo(conn, user_id)
    FROM = mail_user
    TO = receiver_email

    # Create email message
    message = EmailMessage()
    message['Subject'] = "Upcoming course notification"
    message['From'] = mail_user
    message['To'] = receiver_email

    # Fetch course information
    sql_select_Query = """
        SELECT c.course_code, c.course_name, ct.course_venue, ct.duration, ct.zoom_link, ct.teacher_message, ct.notes_link
        FROM coursetimeslots as ct
        INNER JOIN courses as c ON c.course_id = ct.course_id
        WHERE ct.weekday = %s AND ct.start_time = %s
    """
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql_select_Query, (weekday, start_time))
    course_info = cursor.fetchone()

    if course_info:
        end_time = str(int(start_time[:2]) + course_info['duration']) + start_time[2:]

        # Fetch course materials
        sql_select_Query = """
            SELECT material_name, material_link
            FROM coursematerials
            WHERE course_id = %s
        """
        if not isTeacher:
            sql_select_Query += " AND visible_to_students = TRUE"

        cursor.execute(sql_select_Query, (course_id,))
        materials = cursor.fetchall()

        # Prepare email body
        message_body = f"Dear student,\n\nHere is the course information for your upcoming class:\n\n"
        message_body += f"Course code: {course_info['course_code']}\n"
        message_body += f"Course name: {course_info['course_name']}\n"
        message_body += f"Classroom address: {course_info['course_venue']}\n"
        message_body += f"Teacher's message: {course_info['teacher_message']}\n"
        message_body += f"Zoom link: {course_info['zoom_link']}\n"
        message_body += f"Tutorial/Lecture Notes: {course_info['notes_link']}\n\n"

        try:
            server = smtplib.SMTP(mail_host, smtp_port)
            server.starttls()
            server.login(mail_user, mail_pass)
            server.send_message(message)
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
