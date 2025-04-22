import os # Used in this program to refresh/clear the terminal screen before starting a new function or specific instruction (os.system("cls"))
import time # Used to let the system sleep for a designated time (time.sleep("time in seconds"))
from operator import itemgetter # Used to sort list using a key in the list's item

# MARYAM BINTI NORAZMAN 
class Home_Page():
    def welcome():
        os.system("cls")
        welcome_text = " WELCOME TO HAPPY PHYSICS "
        print("\n" + welcome_text.center(70, "-") + "\n")

        page_options = [">> 1. LECTURER", ">> 2. STUDENT"]
        print("OPTIONS TO GO TO PAGE :")
        for i in page_options:
            print(i)
        print("\nOTHER OPTIONS:\n>> E. END SESSION\n\n")

        condition = True
        while condition == True:
            page = input("-->  SELECT AN OPTION [1|2|E]: ")
            if page == "1":
                condition = False
                Home_Page.login_lecturer()
            elif page == "2":
                condition = False
                Home_Page.student_signup()
            elif page == "E":
                condition = False
                UserPAge.logout()
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION! EITHER TYPE '1', '2', OR 'E'", end="\r")
                time.sleep(1)
                Home_Page.welcome()
    

    def student_signup():
        os.system("cls")
        student = "  <<  STUDENT SIGN UP  >>  "
        print("\n" + student.center(70, "-") + "\n")

        options = [">> 1. LOGIN", ">> 2. REGISTER", ">> 3. EXIT"]
        print("OPTIONS TO :")
        for i in options:
            print(i)

        condition = True
        while condition == True:
            page = input("\n" + "-->  SELECT AN OPTION [1|2|3]: ")
            if page == "1":
                Home_Page.login_student()
                condition = False
            elif page == "2":
                Home_Page.register()
                condition = False
            elif page == "3":
                Home_Page.welcome()

    def login_student():
        os.system("cls")
        welcome_admin_login = "  <<  STUDENT LOGIN PAGE  >>  "
        print("\n" + welcome_admin_login.center(70, "-") + "\n" + " HAPPY PHYSICS ".center(70) + "\n\n")
        users = {}
        name_details = {}
        exist_username = []
        exist_password = []
        exist_details = []

        with open('./Text_file/Student.txt','r') as file:
                for line in file:
                    (key, val, more) = line.split(", ")
                    exist_username.append(key)
                    exist_password.append(val)
                    exist_details.append(more)
                    users[key] = val
                    name_details[key] = more
        # Input for admin's username and validation      
        valid = "Not Found"
        while valid == "Not Found":
            print("IF YOU WANT TO GO TO THE  TYPE WELCOME PAGE [EXIT]")
            user_student = input("\nUSERNAME: ")
            if user_student.upper() == "EXIT":
                Home_Page.welcome()
                break
            pass_student = input("\nPASSWORD: ")
            
            if user_student in exist_username:
                valid = "Not Found"
                if pass_student == users[user_student]:
                    UserPAge.StudentsPage()

                    valid = "Found"
                    break
                    
                else:
                    print("\nPASSWORD ARE WRONG !")
                    valid = "Not Found"
                    forget_pass = input("\nDID YOU FORGET YOUR PASSWORD? [YES/NO] : ")
                    if forget_pass.upper() == "YES":
                        password = "Problem"
                        while password == "Problem":
                            os.system("cls")
                            change_pass = input("\nDO YOU WANT TO CHANGE YOUR PASSWORD? [YES/NO] : ")
                            if change_pass.upper() == "YES":
                                Home_Page.change_student()
                            elif change_pass.upper() == "NO":
                                password = "No Problem"
                                number = "Not Pass"
                                while number == "Not Pass":
                                    # VERIFICATION
                                    print("\nPLEASE WRITE YOUR HANDPHONE NUMBER FOR VERIFICATION PURPOSE.")
                                    print("\nRULES FOR HANDPHONE NUMBER: ")
                                    print("\n- ONLY NUMBERS ARE ALLOWED")
                                    print("\n- NUMBERS SHOULD BE 10 OR 11 DIGITS")
                                    print("\n EXAMPLE: 0171234567")
                                    try:
                                        details = int(input("\nHANDPHONE NUMBER: "))
                                        print(name_details[user_student])
                                        if str(details) in name_details[user_student]:
                                            password = "No Problem"
                                            number = "Pass"
                                            print("\nTHIS YOUR PASSWORD, MAKE SURE YOU REMEMBER IT ! \nPASSWORD: " + str(users[user_student]))
                                            to_back = input("\n\n-->  PRESS [ENTER] TO GO TO WELCOME PAGE\n")
                                            Home_Page.welcome()
                                        else:
                                            time.sleep(2)
                                            print("\nWRONG INPUT! ONLY 10 OR 11 DIGITS NUMBER ARE ALLOWED.")
                                            number = "Not Pass"
                                    except ValueError:
                                        time.sleep(2)
                                        print("\nHANDPHONE NUMBER SHOULD ONLY BE INTEGER ! ")
                                        number = "Not Pass"
                                        time.sleep(1)
                            else:
                                time.sleep(2)
                                print("\nWRONG INPUT! YOU SHOULD WRITE 'YES' OR 'NO' ONLY. ")
                                password = "Problem"
                    elif forget_pass.upper() == "NO":
                        Home_Page.login_student()
                        break
                    else:
                        time.sleep(2)
                        print("\nWRONG INPUT! YOU SHOULD WRITE 'YES' OR 'NO' ONLY. ")
                        valid = "Not Found"     
            else:
                print("\nUSERNAME DOESN'T EXIST !")
                valid = "Not Found"
                time.sleep(2)

            if valid == "Found":
                print("\nYOU HAVE LOG IN")
                UserPAge.StudentsPage()
            else:
                continue
            
                
    def change_student():
        users = {}
        name_details = {}
        exist_username = []
        exist_password = []
        exist_details = []

        with open('./Text_file/Student.txt','r') as file:
                for line in file:
                    (key, val, more) = line.split(", ")
                    exist_username.append(key)
                    exist_password.append(val)
                    exist_details.append(more)
                    users[key] = val
                    name_details[key] = more

        # Finding the user to change the password
        user_data = "Not Found"
        while user_data == "Not Found":
            os.system("cls")
            print("\n-->  IF YOU WANT TO CHANGE YOUR PASSWORD PLEASE ENTER YOUR USERNAME BELOW.")
            print("\n-->  IF NOT, ENTER 'EXIT' TO GO TO THE LOG IN PAGE")
            user_student = input("\nUSERNAME: ")
            if user_student.upper() == "EXIT":
                Home_Page.login_lecturer()
                break
            else:
                if user_student in exist_username:
                    # Changing to a new password
                        user_data = "Found"
                        valid_pass = "No"
                        while valid_pass == "No":
                            # VERIFICATION
                            os.system("cls")
                            print("\nPLEASE WRITE YOUR HANDPHONE NUMBER FOR VERIFICATION PURPOSE.")
                            print("\nRULES FOR HANDPHONE NUMBER: ")
                            print("\n- ONLY NUMBERS ARE ALLOWED")
                            print("\n- NUMBERS SHOULD BE 10 OR 11 DIGITS")
                            print("\n EXAMPLE: 0171234567")
                            try:
                                details = int(input("\nHANDPHONE NUMBER: "))
                                if str(details) in name_details[user_student]:
                                    valid_pass = "Yes"
                                    os.system("cls")
                                    print("\nRULES FOR PASSWORD: ")
                                    print("\n- NO SPACES (' ') ARE ALLOWED")
                                    print("\n- SHOULD BE 6 OR MORE CHARACTERS LONG")
                                    pass_student = input("\n-->  ENTER NEW PASSWORD: ")
                                    if (" " in pass_student) == True:
                                        valid_pass = "No"
                                        print("--> INVALID PASSWORD! TRY AGAIN")
                                        time.sleep(1)
                                    elif len(pass_student) < 6:
                                        valid_pass = "No"
                                        print("--> PASSWORD LENGTH SHOULD BE 6 OR MORE")
                                        time.sleep(1)
                                    else:
                                        valid_pass = "Yes"
                                        # Writing data back to text file including updated password for the specific user
                                        data_file  = open("./Text_file/Student.txt",'r')
                                        lines = data_file.readlines()
                                        data_file.close()

                                        write_file = open("./Text_file/Student.txt",'w')
                                        for line in lines:
                                            user_info = line.split(", ")
                                            user_id = user_info[0]
                                            print(user_id)
                                            print(user_student)
                                            if  user_student != user_id:
                                                write_file.write(line)
                                        write_file.close()
                                        
                                        new_user_info = (user_student + ", " + pass_student + ", 0" + str(details))
                                        user_info_file = open("./Text_file/Student.txt", "a")
                                        user_info_file.write( "\n" + new_user_info)
                                        user_info_file.close()
                                        for x in lines:
                                            if x == "\n":
                                                write_file.write(x)
                                            else:
                                                continue

                                        os.system("cls")

                                        print("\n\n  >>  USER PASSWORD HAS BEEN CHANGED!")
                                        print("      RETURNING TO LOG IN STUDENT'S PAGE.\n\n")

                                        time.sleep(3)
                                        os.system("cls")
                                        valid_pass = "Yes"
                                        user_data = "Found"
                                        Home_Page.login_student()
                                        break
                                else:
                                    time.sleep(2)
                                    valid_pass = "No"
                                    print("\n- PHONE NUMBER DOESN'T EXIST!")

                            except ValueError:
                                print("\nHANDPHONE NUMBER SHOULD ONLY BE INTEGER ! ")
                                valid_pass = "No"
                                time.sleep(1)
                else:
                    user_data == "Not Found"
                    print("-->  USERNAME NOT FOUND! PLEASE ENTER YOUR USERNAME CAREFULLY")
                    time.sleep(1)

    def login_lecturer():
        os.system("cls")
        welcome_admin_login = "  <<  LECTURER LOGIN PAGE  >>  "
        print("\n" + welcome_admin_login.center(70, "-") + "\n" + " HAPPY PHYSICS ".center(70) + "\n\n")
        users = {}
        name_details = {}
        exist_username = []
        exist_password = []
        exist_details = []

        with open('./Text_file/Lecturer.txt','r') as file:
                for line in file:
                    (key, val, more) = line.split(", ")
                    exist_username.append(key)
                    exist_password.append(val)
                    exist_details.append(more)
                    users[key] = val
                    name_details[key] = more
        # Input for admin's username and validation      
        valid = "Not Found"
        while valid == "Not Found":
            print("IF YOU WANT TO GO TO THE  TYPE WELCOME PAGE [EXIT]")
            user_student = input("\nUSERNAME: ")
            if user_student.upper() == "EXIT":
                Home_Page.welcome()
                break
            pass_student = input("\nPASSWORD: ")
            
            if user_student in exist_username:
                valid = "Not Found"
                if pass_student == users[user_student]:
                    Admin_UserPage.LecturerPage()

                    valid = "Found"
                    break
                    
                else:
                    print("\nPASSWORD ARE WRONG !")
                    valid = "Not Found"
                    forget_pass = input("\nDID YOU FORGET YOUR PASSWORD? [YES/NO] : ")
                    if forget_pass.upper() == "YES":
                        password = "Problem"
                        while password == "Problem":
                            os.system("cls")
                            change_pass = input("\nDO YOU WANT TO CHANGE YOUR PASSWORD? [YES/NO] : ")
                            if change_pass.upper() == "YES":
                                Home_Page.change_lecturer()
                            elif change_pass.upper() == "NO":
                                password = "No Problem"
                                number = "Not Pass"
                                while number == "Not Pass":
                                    # VERIFICATION
                                    print("\nPLEASE WRITE YOUR HANDPHONE NUMBER FOR VERIFICATION PURPOSE.")
                                    print("\nRULES FOR HANDPHONE NUMBER: ")
                                    print("\n- ONLY NUMBERS ARE ALLOWED")
                                    print("\n- NUMBERS SHOULD BE 10 OR 11 DIGITS")
                                    print("\n EXAMPLE: 0171234567")
                                    try:
                                        details = int(input("\nHANDPHONE NUMBER: "))
                                        print(name_details[user_student])
                                        if str(details) in name_details[user_student]:
                                            password = "No Problem"
                                            number = "Pass"
                                            print("\nTHIS YOUR PASSWORD, MAKE SURE YOU REMEMBER IT ! \nPASSWORD: " + str(users[user_student]))
                                            to_back = input("\n\n-->  PRESS [ENTER] TO GO TO WELCOME PAGE\n")
                                            Home_Page.welcome()
                                        else:
                                            time.sleep(2)
                                            print("\nWRONG INPUT! ONLY 10 OR 11 DIGITS NUMBER ARE ALLOWED.")
                                            number = "Not Pass"
                                    except ValueError:
                                        time.sleep(2)
                                        print("\nHANDPHONE NUMBER SHOULD ONLY BE INTEGER ! ")
                                        number = "Not Pass"
                                        time.sleep(1)
                            else:
                                time.sleep(2)
                                print("\nWRONG INPUT! YOU SHOULD WRITE 'YES' OR 'NO' ONLY. ")
                                password = "Problem"
                    elif forget_pass.upper() == "NO":
                        Home_Page.login_lecturer()
                        break
                    else:
                        time.sleep(2)
                        print("\nWRONG INPUT! YOU SHOULD WRITE 'YES' OR 'NO' ONLY. ")
                        valid = "Not Found"     
            else:
                print("\nUSERNAME DOESN'T EXIST !")
                valid = "Not Found"
                time.sleep(2)

            if valid == "Found":
                print("\nYOU HAVE LOG IN")
                Admin_UserPage.LecturerPage()
            else:
                continue
            
                
    def change_lecturer():
        users = {}
        name_details = {}
        exist_username = []
        exist_password = []
        exist_details = []

        with open('./Text_file/Lecturer.txt','r') as file:
                for line in file:
                    (key, val, more) = line.split(", ")
                    exist_username.append(key)
                    exist_password.append(val)
                    exist_details.append(more)
                    users[key] = val
                    name_details[key] = more

        # Finding the user to change the password
        user_data = "Not Found"
        while user_data == "Not Found":
            os.system("cls")
            print("\n-->  IF YOU WANT TO CHANGE YOUR PASSWORD PLEASE ENTER YOUR USERNAME BELOW.")
            print("\n-->  IF NOT, ENTER 'EXIT' TO GO TO THE LOG IN PAGE")
            user_student = input("\nUSERNAME: ")
            if user_student.upper() == "EXIT":
                Home_Page.login_lecturer()
                break
            else:
                if user_student in exist_username:
                    # Changing to a new password
                        user_data = "Found"
                        valid_pass = "No"
                        while valid_pass == "No":
                            # VERIFICATION
                            os.system("cls")
                            print("\nPLEASE WRITE YOUR HANDPHONE NUMBER FOR VERIFICATION PURPOSE.")
                            print("\nRULES FOR HANDPHONE NUMBER: ")
                            print("\n- ONLY NUMBERS ARE ALLOWED")
                            print("\n- NUMBERS SHOULD BE 10 OR 11 DIGITS")
                            print("\n EXAMPLE: 0171234567")
                            try:
                                details = int(input("\nHANDPHONE NUMBER: "))
                                if str(details) in name_details[user_student]:
                                    valid_pass = "Yes"
                                    os.system("cls")
                                    print("\nRULES FOR PASSWORD: ")
                                    print("\n- NO SPACES (' ') ARE ALLOWED")
                                    print("\n- SHOULD BE 6 OR MORE CHARACTERS LONG")
                                    pass_student = input("\n-->  ENTER NEW PASSWORD: ")
                                    if (" " in pass_student) == True:
                                        valid_pass = "No"
                                        print("--> INVALID PASSWORD! TRY AGAIN")
                                        time.sleep(1)
                                    elif len(pass_student) < 6:
                                        valid_pass = "No"
                                        print("--> PASSWORD LENGTH SHOULD BE 6 OR MORE")
                                        time.sleep(1)
                                    else:
                                        valid_pass = "Yes"
                                        # Writing data back to text file including updated password for the specific user
                                        data_file  = open("./Text_file/Lecturer.txt",'r')
                                        lines = data_file.readlines()
                                        data_file.close()

                                        write_file = open("./Text_file/Lecturer.txt",'w')
                                        for line in lines:
                                            user_info = line.split(", ")
                                            user_id = user_info[0]
                                            print(user_id)
                                            print(user_student)
                                            if  user_student != user_id:
                                                write_file.write(line)
                                        write_file.close()
                                        
                                        new_user_info = (user_student + ", " + pass_student + ", 0" + str(details))
                                        user_info_file = open("./Text_file/Lecturer.txt", "a")
                                        user_info_file.write( "\n" + new_user_info)
                                        user_info_file.close()
                                        for x in lines:
                                            if x == "\n":
                                                write_file.write(x)
                                            else:
                                                continue

                                        os.system("cls")

                                        print("\n\n  >>  USER PASSWORD HAS BEEN CHANGED!")
                                        print("      RETURNING TO LOG IN LECTURER'S PAGE.\n\n")

                                        time.sleep(3)
                                        os.system("cls")
                                        valid_pass = "Yes"
                                        user_data = "Found"
                                        Home_Page.login_lecturer()
                                        break
                                else:
                                    time.sleep(2)
                                    valid_pass = "No"
                                    print("\n- PHONE NUMBER DOESN'T EXIST!")

                            except ValueError:
                                print("\nHANDPHONE NUMBER SHOULD ONLY BE INTEGER ! ")
                                valid_pass = "No"
                                time.sleep(1)
                else:
                    user_data == "Not Found"
                    print("-->  USERNAME NOT FOUND! PLEASE ENTER YOUR USERNAME CAREFULLY")
                    time.sleep(1)

    def register():
        os.system("cls")
        welcome_user_register = "  << STUDENT REGISTER PAGE  >>  "
        print("\n" + welcome_user_register.center(70, "-") + "\n" + " HAPPY PHYSICS ".center(70) + "\n\n")
        print(" RULES TO CREATE USERNAME & PASSWORD ".center(50, "="))
        print("\n>>  [USERNAME] : NO SPACES (' ') ARE ALLOWED")
        print(">>  [PASSWORD] : NO SPACES (' ') ARE ALLOWED")
        print("                 SHOULD BE 6 OR MORE CHARACTERS LONG")
        print(">>  [HANDPHONE NUMBER] : ONLY NUMBERS ARE ALLOWED")
        print("                         NUMBERS SHOULD BE 10 OR 11 DIGITS\n")

        users = {}
        exist_username = []
        exist_password = []
        exist_details = []

        with open('./Text_file/Student.txt','r') as file:
                for line in file:
                    (key, val, more) = line.split(",")
                    exist_username.append(key)
                    exist_password.append(val)
                    exist_details.append(more)
                    users[key] = val

        # Input for admin's username and validation      
        valid = "Not Found"
        while valid == "Not Found":
            print("\nIF YOU WANT TO EXIT TYPE [EXIT]")
            name_student = input("\nENTER NEW USERNAME: ")
            if name_student.upper() == "EXIT":
                Home_Page.student_signup()
                break 
            pass_student = input("\nENTER NEW PASSWORD: ")

            if name_student in exist_username:
                print("\nUSERNAME ALREADY EXIST ! TRY AGAIN")
                valid = "Not Found"
                time.sleep(1)
                
            else:
                if (" " in name_student) == True:
                    print("\nUSERNAME CONTAIN ' ' (SPACE) ! TRY AGAIN")
                    valid = "Not Found"
                    time.sleep(1)
                    break
                elif (" " in pass_student) == True:
                    print("\nPASSWORD CONTAIN ' ' (SPACE) ! TRY AGAIN")
                    valid = "Not Found"
                    time.sleep(1)
                    break
                else:
                    if len(pass_student) < 6:
                        print("\nPASSWORD LENGTH SHOULD BE 6 OR MORE ! TRY AGAIN")
                        valid = "Not Found"
                        time.sleep(1)
                        break
                    else:
                        
                            try:
                                details_student = int(input("\nENTER YOUR HANDPHONE NUMBER: "))
                                valid = "True"
                                
                            except ValueError:
                                print("\nHANDPHONE NUMBER SHOULD ONLY BE INTEGER ! TRY AGAIN")
                                valid = "Not Found"
                                time.sleep(1)
                                break

            if valid == "True":
                if len(str(details_student)) != 9 and len(str(details_student)) != 10:
                    print ("\nONLY 10 OR 11 DIGITS ALLOWED FOR HANDPHONE NUMBER ! TRY AGAIN")
                    valid = "Not Found"
                    time.sleep(2)
                    
                else:
                    valid = "Found"
                    if valid == "Found":
                        confirm_pass = input("\nENTER YOUR CONFIRMATION PASSWORD: ")
                        if confirm_pass == pass_student:
                            print("\nYOUR REGISTRATION ARE BEING PROCESSED.", end = "\r")
                            time.sleep(1)
                            print("YOUR REGISTRATION ARE BEING PROCESSED..", end = "\r")
                            time.sleep(1)
                            print("YOUR REGISTRATION ARE BEING PROCESSED...")
                            time.sleep(3)
                            print("\n\n  >>  CONGRATULATIONS! NEW USER HAS BEEN CREATED :)")
                            print("      PLEASE PROCEED TO LOGIN WITH REGISTERED USERNAME.\n\n")
                            new_user_info = (name_student + ", " + pass_student + ", " + "0" + str(details_student))
                            user_info_file = open("./Text_file/Student.txt", "a")
                            user_info_file.write("\n" + new_user_info)
                            user_info_file.close()
                            print("\n" + "-->  REDIRECTING TO STUDENT SIGN UP PAGE.")
                            Home_Page.student_signup()
                        else:
                            print("\nYOUR CONFIRMATION PASSWORD ARE NOT SAME WITH PASSWORD !") 
                            time.sleep(1)
                    else:
                        time.sleep(1)
                        continue

# NUR ADIBAH BINTI KHAIRUL ANUAR
class UserPAge():
    def StudentsPage():
        os.system("cls")
        welcome_text = " STUDENT'S PAGE "
        print("\n" + welcome_text.center(70, "-") + "")
        print(""" 
        1. NOTES
        2. EXERCISES
        3. CALCULATOR
        4. COMMENT SECTION
        5. LOG OUT """)
        try:
            students_option = int(input("\n-->  SELECT AN OPTION [1|2|3|4|5]: "))
            if students_option == 1:
                UserPAge.NotesPage()
            elif students_option == 2:
                UserPAge.ExercisesPage()
            elif students_option == 3:
                UserPAge.Calculator()
            elif students_option == 4:
                UserPAge.ReviewPage()
            elif students_option == 5:
                print("\n" + "-->  PLEASE WAIT A MOMENT.", end = "\r")
                time.sleep(1)
                print("-->  PLEASE WAIT A MOMENT..", end = "\r")
                time.sleep(1)
                print("-->  PLEASE WAIT A MOMENT...")
                time.sleep(1)
                Home_Page.welcome()
            else:
                print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
                time.sleep(1)
                UserPAge.StudentsPage()
        except ValueError:
            print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
            time.sleep(1)
            UserPAge.StudentsPage()

    def NotesPage():
        os.system("cls")
        welcome_text = " NOTES PAGE "
        print("\n" + welcome_text.center(70, "-") + "\n")
        data_file = open("./Text_file/Notes.txt", "r")
        lines = data_file.readlines()
        data_file.close()
        print("-" * 62)
        print(f"""|  CODE  |                    TOPICS                         |""")
        print("-" * 62)
        for line in lines:
            Notes_info = line.split(", ")
            Notes_topic = Notes_info[1][:-1]
            if "A" in Notes_info[0]:
                print("|" + Notes_info[0].center(8) + "| " + Notes_topic.ljust(50) + "|")
        print("-" * 62)
        for line in lines:
            Notes_info = line.split(", ")
            Notes_topic = Notes_info[1][:-1]
            if "B" in Notes_info[0]:
                print("|" + Notes_info[0].center(8) + "| " + Notes_topic.ljust(50) + "|")
        print("-" * 62)
        for line in lines:
            Notes_info = line.split(", ")
            Notes_topic = Notes_info[1][:-1]
            if "C" in Notes_info[0]:
                print("|" + Notes_info[0].center(8) + "| " + Notes_topic.ljust(50) + "|")
        print("-" * 62)
        for line in lines:
            Notes_info = line.split(", ")
            Notes_topic = Notes_info[1][:-1]
            if "D" in Notes_info[0]:
                print("|" + Notes_info[0].center(8) + "| " + Notes_topic.ljust(50) + "|")
        print("-" * 62)
        code = True
        while code == True:
            print("IF YOU WANT TO GO TO THE REVIEW PAGE TYPE [EXIT]")
            choice_topic = input("\nSEARCH TOPIC USING CODE [Eg: A100]: \n")
            if choice_topic.upper() == "EXIT":
                UserPAge.StudentsPage()
                break
            code_found = "no"
            for line in lines:
                Notes_info = line.split(", ")
                Notes_topic = Notes_info[1][:-1]
                if choice_topic.upper() in Notes_info[0]:
                    confirmation = True
                    while confirmation == True:
                        os.system("cls")
                        print(f"""\nFROM THE CODE, IT IS {Notes_topic}""")
                        print("\n>>  Y = YES\n>>  N = NO\n")
                        proceed = input(f"""\nDO YOU WANT TO PROCEED? [Y|N]:\n""")
                        if proceed.upper() == "N" or proceed.upper() == "NO":
                            os.system("cls")
                            print("\n" + "-->  REDIRECTING TO STUDENT'S PAGE.", end = "\r")
                            time.sleep(1)
                            print("-->  REDIRECTING TO STUDENT'S PAGE..", end = "\r")
                            time.sleep(1)
                            print("-->  REDIRECTING TO STUDENT'S PAGE...", end = "\r")
                            time.sleep(1)
                            confirmation = False
                            code_found = "yes"
                            UserPAge.StudentsPage()
                        elif proceed.upper() == "Y" or proceed.upper() == "YES":
                            print("\n" + "-->  REDIRECTING TO NOTES")
                            time.sleep(1)
                            confirmation = False
                            code_found = "yes"
                            UserPAge.Notes_Page(choice_topic)
                        else:
                            print("\n--> WRONG INPUT! ONLY TYPE 'Y' OR 'N'!")
                            time.sleep(1)
                            confirmation = True
                            code_found = "yes"
            if code_found == "no":
                os.system("cls")
                print("\n--> WRONG INPUT! ONLY TYPE CODES FROM THE TABLE GIVEN!")
                print("\n--> EXAMPLE : A100 ")
                time.sleep(1)
                print("\n" + "-->  REDIRECTING TO NOTES PAGE.", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO NOTES PAGE..", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO NOTES PAGE...", end = "\r")
                time.sleep(1)
                UserPAge.NotesPage()

    def Notes_Page(choice_topic):
        os.system("cls")
        if choice_topic.upper() == "A100":
            UserPAge.Notes1()
        elif choice_topic.upper() == "B100":
            UserPAge.Notes2()
        elif choice_topic.upper() == "C100":
            UserPAge.notes3()
        elif choice_topic.upper() == "D100":
            UserPAge.notes4()

    def Notes1():
        os.system("cls")
        welcome_text = " TOPIC 1: INTRODUCTION TO SI UNIT & DERIVED UNIT PAGE "
        print("\n" + welcome_text.center(78, "-"))
        print("NOTES".center(78) + "\n")
        data_file = open("./Text_file/Notes1.txt", "r")
        lines = data_file.readlines()
        data_file.close()
        print("-" * 78)
        print(f"""|     QUANTITY    |                    NAME                      |   SYMBOL  |""")
        print("-" * 78)
        for line in lines:
            Notes_info = line.split("| ")
            if "A" in Notes_info[0]:
                print("|" + Notes_info[1].center(15) + "  | " + Notes_info[2].center(45) + "| " + Notes_info[3].center(10) + "|")
        print("-" * 78)
        for line in lines:
            Notes_info = line.split("| ")
            if "B" in Notes_info[0]:
                print("|" + Notes_info[1].center(15) + "  | " + Notes_info[2].center(45) + "| " + Notes_info[3].center(10) + "|")
        print("-" * 78)
        for line in lines:
            Notes_info = line.split("| ")
            if "C" in Notes_info[0]:
                print("|" + Notes_info[1].center(15) + "  | " + Notes_info[2].center(45) + "| " + Notes_info[3].center(10) + "|")
        print("-" * 78)
        for line in lines:
            Notes_info = line.split("| ")
            if "D" in Notes_info[0]:
                print("|" + Notes_info[1].center(15) + "  | " + Notes_info[2].center(45) + "| " + Notes_info[3].center(10) + "|")
        print("-" * 78)
        for line in lines:
            Notes_info = line.split("| ")
            if "E" in Notes_info[0]:
                print("|" + Notes_info[1].center(15) + "  | " + Notes_info[2].center(45) + "| " + Notes_info[3].center(10) + "|")
        print("-" * 78)
        confirmation = input("\n\n-->  PRESS [ENTER] TO GO TO BACK TO STUDENT'S PAGE\n")
        UserPAge.StudentsPage()

    def Notes2():
        os.system("cls")
        welcome_text = " TOPIC 2: STANDARD PREFIXES "
        print("\n" + welcome_text.center(102, "-"))
        print("NOTES".center(102) + "\n")
        data_file = open("./Text_file/Notes2.txt", "r")
        lines = data_file.readlines()
        data_file.close()
        print("-" * 102)
        print(f"""|     PREFIX    |   SYMBOL  |   ACTUAL VALUE OF THE SYMBOL  |  VALUE OF THE SYMBOL IN STANDARD FORM  |""")
        print("-" * 102)
        for line in lines:
            Notes_info = line.split("| ")
            if "A" in Notes_info[0]:
                print("|" + Notes_info[1].center(13) + "  | " + Notes_info[2].center(10) + "| " + Notes_info[3].center(30) + "|" + Notes_info[4].center(40) + "|")
        print("-" * 102)
        for line in lines:
            Notes_info = line.split("| ")
            if "B" in Notes_info[0]:
                print("|" + Notes_info[1].center(13) + "  | " + Notes_info[2].center(10) + "| " + Notes_info[3].center(30) + "|" + Notes_info[4].center(40) + "|")
        print("-" * 102)
        for line in lines:
            Notes_info = line.split("| ")
            if "C" in Notes_info[0]:
                print("|" + Notes_info[1].center(13) + "  | " + Notes_info[2].center(10) + "| " + Notes_info[3].center(30) + "|" + Notes_info[4].center(40) + "|")
        print("-" * 102)
        for line in lines:
            Notes_info = line.split("| ")
            if "D" in Notes_info[0]:
                print("|" + Notes_info[1].center(13) + "  | " + Notes_info[2].center(10) + "| " + Notes_info[3].center(30) + "|" + Notes_info[4].center(40) + "|")
        print("-" * 102)
        for line in lines:
            Notes_info = line.split("| ")
            if "E" in Notes_info[0]:
                print("|" + Notes_info[1].center(13) + "  | " + Notes_info[2].center(10) + "| " + Notes_info[3].center(30) + "|" + Notes_info[4].center(40) + "|")
        print("-" * 102)
        for line in lines:
            Notes_info = line.split("| ")
            if "F" in Notes_info[0]:
                print("|" + Notes_info[1].center(13) + "  | " + Notes_info[2].center(10) + "| " + Notes_info[3].center(30) + "|" + Notes_info[4].center(40) + "|")
        print("-" * 102)
        for line in lines:
            Notes_info = line.split("| ")
            if "G" in Notes_info[0]:
                print("|" + Notes_info[1].center(13) + "  | " + Notes_info[2].center(10) + "| " + Notes_info[3].center(30) + "|" + Notes_info[4].center(40) + "|")
        print("-" * 102)
        for line in lines:
            Notes_info = line.split("| ")
            if "H" in Notes_info[0]:
                print("|" + Notes_info[1].center(13) + "  | " + Notes_info[2].center(10) + "| " + Notes_info[3].center(30) + "|" + Notes_info[4].center(40) + "|")
        print("-" * 102)
        for line in lines:
            Notes_info = line.split("| ")
            if "I" in Notes_info[0]:
                print("|" + Notes_info[1].center(13) + "  | " + Notes_info[2].center(10) + "| " + Notes_info[3].center(30) + "|" + Notes_info[4].center(40) + "|")
        print("-" * 102)
        for line in lines:
            Notes_info = line.split("| ")
            if "J" in Notes_info[0]:
                print("|" + Notes_info[1].center(13) + "  | " + Notes_info[2].center(10) + "| " + Notes_info[3].center(30) + "|" + Notes_info[4].center(40) + "|")
        print("-" * 102)
        for line in lines:
            Notes_info = line.split("| ")
            if "K" in Notes_info[0]:
                print("|" + Notes_info[1].center(13) + "  | " + Notes_info[2].center(10) + "| " + Notes_info[3].center(30) + "|" + Notes_info[4].center(40) + "|")
        print("-" * 102)
        confirmation = input("\n\n-->  PRESS [ENTER] TO GO TO BACK TO STUDENT'S PAGE\n")
        UserPAge.StudentsPage()

    # NURULAIN AFIQAH BINTI ABDULLAH 
    def notes3():
        os.system("cls")
        print("\n" + "TOPIC 3: DISTANCE & DISPLACEMENT".center(70, "-") + "\n" + "NOTES".center(70))
        print("\n--> DISTANCE : \n\n       - The total length of the path that the object travels\n       - Scalar Quantities\n       - Has magnitude only")
        print("\n--> DISPLACEMENT :\n\n       - the shortest length between an object's start and endpoint \n         as well as the direction of the motion\n       - vector quantities\n       - has magnitude and direction")
        confirmation = input("\n\n-->  PRESS [ENTER] TO GO TO EXAMPLES OF QUESTION\n")
        os.system("cls")
        print("\n" + "TOPIC 3: DISTANCE & DISPLACEMENT".center(70, "-") + "\n" + "EXAMPLES OF QUESTION".center(70))
        print("\n--> Examples of questions :\n\n       1. A car drives three blocks north and four blocks east.\n\n       - The total distance the object travels is 4 + 3 = 7 blocks.\n\n       - The total displacement is the shortest distance from where\n         the car begins and ends its trip, which is a diagonal line,\n         the hypotenuse of a right triangle with legs 3 and 4\n\n       - From the Pythagorean theorem, 3^2 + 4^2 = 25, so the length \n         of the hypotenuse is the square root of this value, which is 5. ")
        print("\nExamples of questions :\n\n        1. A person walks north from their house 100 meters to the park,\n           and then returns home before continuing 20 meters south to\n           check the mail.\n\n         - total distance walked of 100 m + 100 m + 20 m = 220 m.\n\n         - But if the starting point is the house situated at the\n           origin (the point 0, 0 on a coordinate plane) and the final\n           position is the mailbox, which is at (0, −20), the person ends\n           up only 20 meters away from where they began, making the\n           total displacement −20 m.")
        confirmation = input("\n\n-->  PRESS [ENTER] TO GO TO BACK TO STUDENT'S PAGE\n")
        UserPAge.StudentsPage()

    def notes4():
        os.system("cls")
        print("\n" + "TOPIC 4: SPEED & VELOCITY".center(70, "-") + "\n" + "NOTES".center(70))
        print("\n--> SPEED : \n\n       - Speed is defined as the rate of change of distance\n       - Scalar Quantities\n       - Unit: m/s\n       - Formula: v = d/t\n       - Example: 50 km/hr describes the speed at which a car is\n         traveling along a road")
        print("\n--> VELOCITY :\n\n       - Velocity is defined as the rate of change of displacement\n       - Vector Quantities\n       - Unit: m/s\n       - formula: v = s/t\n       - Example: 50 km/hr west describes the velocity at which\n         it is traveling.")
        confirmation = input("\n\n-->  PRESS [ENTER] TO GO TO EXAMPLES OF QUESTION\n")
        os.system("cls")
        print("\n" + "TOPIC 4: SPEED & VELOCITY".center(70, "-") + "\n" + "EXAMPLES OF QUESTION".center(70))
        print("\nExamples of questions (1):\n\n       - The physics teacher walked a distance of 12 meters in 24 seconds\n\n       - By using a formula her average speed was 0.50 m/s. \n\n       - However, since her displacement is 0 meters, her average\n         velocity is 0 m/s. - - - -Remember that the displacement refers\n         to the change in position and the velocity is based upon this\n         position change. In this case of the teacher's motion, there is a\n         position change of 0 meters and thus an average velocity of 0 m/s.")
        confirmation = input("\n\n-->  PRESS [ENTER] TO GO TO BACK TO STUDENT'S PAGE\n")
        UserPAge.StudentsPage()

        
    # NUR ADIBAH BINTI KHAIRUL ANUAR
    def ExercisesPage():
        os.system("cls")
        welcome_text = " EXERCISES PAGE "
        print("\n" + welcome_text.center(70, "-") + "\n")
        data_file = open("./Text_file/Notes.txt", "r")
        lines = data_file.readlines()
        data_file.close()
        print("-" * 62)
        print(f"""|  CODE  |                    TOPICS                         |""")
        print("-" * 62)
        for line in lines:
            Notes_info = line.split(", ")
            Notes_topic = Notes_info[1][:-1]
            if "A" in Notes_info[0]:
                print("|" + Notes_info[0].center(8) + "| " + Notes_topic.ljust(50) + "|")
        print("-" * 62)
        for line in lines:
            Notes_info = line.split(", ")
            Notes_topic = Notes_info[1][:-1]
            if "B" in Notes_info[0]:
                print("|" + Notes_info[0].center(8) + "| " + Notes_topic.ljust(50) + "|")
        print("-" * 62)
        for line in lines:
            Notes_info = line.split(", ")
            Notes_topic = Notes_info[1][:-1]
            if "C" in Notes_info[0]:
                print("|" + Notes_info[0].center(8) + "| " + Notes_topic.ljust(50) + "|")
        print("-" * 62)
        for line in lines:
            Notes_info = line.split(", ")
            Notes_topic = Notes_info[1][:-1]
            if "D" in Notes_info[0]:
                print("|" + Notes_info[0].center(8) + "| " + Notes_topic.ljust(50) + "|")
        print("-" * 62)
        code = True
        while code == True:
            print("IF YOU WANT TO REFER TO THE STUDENTS PAGE TYPE [EXIT]")
            question_topic = input("\nSEARCH TOPIC USING CODE [Eg: A100]: \n")
            if question_topic.upper() == "EXIT":
                UserPAge.StudentsPage()
                break
            code_found = "no"
            for line in lines:
                Notes_info = line.split(", ")
                Notes_topic = Notes_info[1][:-1]
                if question_topic.upper() in Notes_info[0]:
                    confirmation = True
                    while confirmation == True:
                        os.system("cls")
                        #.......................................................................
                        print(f"""\nFROM THE CODE, IT IS {Notes_topic}""")
                        print("\n>>  Y = YES\n>>  N = NO\n")
                        proceed = input(f"""\nDO YOU WANT TO PROCEED? [Y|N]:\n""")
                        if proceed.upper() == "N" or proceed.upper() == "NO":
                            os.system("cls")
                            print("\n" + "-->  REDIRECTING TO STUDENT'S PAGE.", end = "\r")
                            time.sleep(1)
                            print("-->  REDIRECTING TO STUDENT'S PAGE..", end = "\r")
                            time.sleep(1)
                            print("-->  REDIRECTING TO STUDENT'S PAGE...", end = "\r")
                            time.sleep(1)
                            confirmation = False
                            code_found = "yes"
                            UserPAge.StudentsPage()
                        elif proceed.upper() == "Y" or proceed.upper() == "YES":
                            print("\n" + "-->  REDIRECTING TO QUESTIONS.", end = "\r")
                            time.sleep(1)
                            print("-->  REDIRECTING TO QUESTIONS..", end = "\r")
                            time.sleep(1)
                            print("-->  REDIRECTING TO QUESTIONS...", end = "\r")
                            time.sleep(1)
                            UserPAge.QuestionPage(question_topic)
                            confirmation = False
                            code_found = "yes"
                        else:
                            print("\n--> WRONG INPUT! ONLY TYPE 'Y' OR 'N'!")
                            time.sleep(1)
                            confirmation = True
                            code_found = "yes"
            if code_found == "no":
                os.system("cls")
                print("\n--> WRONG INPUT! ONLY TYPE CODES FROM THE TABLE GIVEN!")
                print("\n--> EXAMPLE : A100 ")
                time.sleep(1)
                print("\n" + "-->  REDIRECTING TO EXERCISES PAGE.", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO EXERCISES PAGE..", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO EXERCISES PAGE...", end = "\r")
                time.sleep(1)
                UserPAge.ExercisesPage()

    def QuestionPage(question_topic):
        os.system("cls")
        number = 0
        marks = 0
        if question_topic.upper() == "A100":
            UserPAge.Quiz_1(number, marks)
        elif question_topic.upper() == "B100":
            UserPAge.Quiz_2(number,marks)
        elif question_topic.upper() == "C100":
            UserPAge.Quiz_3(number, marks)
        elif question_topic.upper() == "D100":
            UserPAge.Quiz_4(number, marks)

    # NURULAIN AFIQAH BINTI ABDULLAH
    #***************QUIZ 1************************************************* 
    def Quiz_1(number, marks):
        os.system('cls')
        with open(r'./Text_file/Quiz1.txt', 'r') as Quiz1:
            length = len(Quiz1.readlines())
        with open(r'./Text_file/Quiz1.txt', 'r') as Quiz1:
            lines = Quiz1.readlines()
            number = number + 1
            word = "Q0" + str(number)
            for line in lines:
                line_oo = line.split('|')
                if line.find(word) != -1:    
                    print(line_oo[0],". ",line_oo[1],"\n")
                    print("     A.", line_oo[2])
                    print("     B.", line_oo[3])
                    print("     C.", line_oo[4])
                    print("     D.", line_oo[5],"\n")
                    ans_input = input("Answer : ")
                    modified_ans = ans_input.upper()
                    if modified_ans == "A" or modified_ans == "B" or modified_ans == "C" or modified_ans == "D" :
                        if modified_ans in line_oo[6] :
                            time.sleep(1)
                            marks = marks + 1
                            UserPAge.Quiz_1(number, marks)
                        else :
                            time.sleep(1)
                            UserPAge.Quiz_1(number, marks)
                    else:
                        print("--> WRONG INPUT! ANSWER SHOULD BE 'A','B','C', OR 'D'!")
                        time.sleep(1)
                        number = number - 1
                        UserPAge.Quiz_1(number, marks)
        os.system('cls')
        print("CONGRATS! YOU HAVE COMPLETED THE QUIZ!\n")
        print("TOTAL MARKS : ",marks,"/",length)
        to_back = input("\n\n-->  PRESS [ENTER] TO GO BACK TO STUDENT'S PAGE ")
        UserPAge.StudentsPage()

        
    #***************QUIZ 2*************************************************
    def Quiz_2(number,marks):
        os.system('cls')
        with open(r'./Text_file/Quiz2.txt', 'r') as Quiz2:
            length = len(Quiz2.readlines())
        with open(r'./Text_file/Quiz2.txt', 'r') as Quiz2:
            lines = Quiz2.readlines()
            number = number + 1
            word = "Q0" + str(number)
            for line in lines:
                line_oo = line.split('|')
                if line.find(word) != -1:    
                    print(line_oo[0],". ",line_oo[1],"\n")
                    print("     A.", line_oo[2])
                    print("     B.", line_oo[3])
                    print("     C.", line_oo[4])
                    print("     D.", line_oo[5],"\n")
                    ans_input = input("Answer : ")
                    modified_ans = ans_input.upper()
                    if modified_ans == "A" or modified_ans == "B" or modified_ans == "C" or modified_ans == "D" :
                        if modified_ans in line_oo[6] :
                            time.sleep(1)
                            marks = marks + 1
                            UserPAge.Quiz_2(number,marks)
                        else :
                            time.sleep(1)
                            UserPAge.Quiz_2(number,marks)
                    else:
                        print("--> WRONG INPUT! ANSWER SHOULD BE 'A','B','C', OR 'D'!")
                        time.sleep(1)
                        number = number - 1
                        UserPAge.Quiz_2(number,marks)
        os.system('cls')
        print("CONGRATS! YOU HAVE COMPLETED THE QUIZ!\n")
        print("TOTAL MARKS : ",marks,"/",length)
        to_back = input("\n\n-->  PRESS [ENTER] TO GO BACK TO STUDENT'S PAGE ")
        UserPAge.StudentsPage()

    #***************QUIZ 3*************************************************
    def Quiz_3(number, marks):
        os.system('cls')
        with open(r'./Text_file/Quiz3.txt', 'r') as Quiz3:
            length = len(Quiz3.readlines())
        with open(r'./Text_file/Quiz3.txt', 'r') as Quiz3:
            lines = Quiz3.readlines()
            number = number + 1
            word = "Q0" + str(number)
            for line in lines:
                line_oo = line.split('|')
                if line.find(word) != -1:    
                    print(line_oo[0],". ",line_oo[1],"\n")
                    print("     A.", line_oo[2])
                    print("     B.", line_oo[3])
                    print("     C.", line_oo[4])
                    print("     D.", line_oo[5],"\n")
                    ans_input = input("Answer : ")
                    modified_ans = ans_input.upper()
                    if modified_ans == "A" or modified_ans == "B" or modified_ans == "C" or modified_ans == "D" :
                        if modified_ans in line_oo[6] :
                            time.sleep(1)
                            marks = marks + 1
                            UserPAge.Quiz_3(number, marks)
                        else :
                            time.sleep(1)
                            UserPAge.Quiz_3(number, marks)
                    else:
                        print("--> WRONG INPUT! ANSWER SHOULD BE 'A','B','C', OR 'D'!")
                        time.sleep(1)
                        number = number - 1
                        UserPAge.Quiz_3(number, marks)
        os.system('cls')
        print("CONGRATS! YOU HAVE COMPLETED THE QUIZ!\n")
        print("TOTAL MARKS : ",marks,"/",length)
        to_back = input("\n\n-->  PRESS [ENTER] TO GO BACK TO STUDENT'S PAGE ")
        UserPAge.StudentsPage()

    #***************QUIZ 4*************************************************
    def Quiz_4(number, marks):
        os.system('cls')
        with open(r'./Text_file/Quiz4.txt', 'r') as Quiz4:
            length = len(Quiz4.readlines())
        with open(r'./Text_file/Quiz4.txt', 'r') as Quiz4:
            lines = Quiz4.readlines()
            number = number + 1
            word = "Q0" + str(number)
            for line in lines:
                line_oo = line.split('|')
                if line.find(word) != -1:    
                    print(line_oo[0],". ",line_oo[1],"\n")
                    print("     A.", line_oo[2])
                    print("     B.", line_oo[3])
                    print("     C.", line_oo[4])
                    print("     D.", line_oo[5],"\n")
                    ans_input = input("Answer : ")
                    modified_ans = ans_input.upper()
                    if modified_ans == "A" or modified_ans == "B" or modified_ans == "C" or modified_ans == "D" :
                        if modified_ans in line_oo[6] :
                            time.sleep(1)
                            marks = marks + 1
                            UserPAge.Quiz_4(number, marks)
                        else :
                            time.sleep(1)
                            UserPAge.Quiz_4(number, marks)
                    else:
                        print("--> WRONG INPUT! ANSWER SHOULD BE 'A','B','C', OR 'D'!")
                        time.sleep(1)
                        number = number - 1
                        UserPAge.Quiz_4(number, marks)
        os.system('cls')
        print("CONGRATS! YOU HAVE COMPLETED THE QUIZ!\n")
        print("TOTAL MARKS : ",marks,"/",length)
        to_back = input("\n\n-->  PRESS [ENTER] TO GO BACK TO STUDENT'S PAGE ")
        UserPAge.StudentsPage()

    # NUR ADIBAH BINTI KHAIRUL ANUAR
    def Calculator():
        os.system("cls")
        print(f"""\nCALCULATOR\n
1. CM TO INCH
2. MICRO TO PICO
3. VELOCITY
4. ACCELERATION
5. EXIT \n""")
        try:
            calculator_choices = int(input("ENTER THE NUMBER [1|2|3|4|5]: "))
            if calculator_choices == 1:
                os.system("cls")
                cm_value = float(input("ENTER THE VALUE IN POINT (CM): "))
                inch_value = cm_value * 0.3937
                os.system("cls")
                print('{} x 0.3937'.format(cm_value))
                time.sleep(1)
                print(f"""\nTHE INCH VALUE IS {round(inch_value, 4)} in """)
                to_back = input("\n\n-->  PRESS [ENTER] TO GO BACK TO CALCULATOR PAGE ")
                UserPAge.Calculator()
                            
            elif calculator_choices == 2:
                os.system("cls")
                micro_value = float(input("ENTER THE VALUE IN POINT (micro): "))
                pico_value = micro_value * 10**6
                os.system("cls")
                print('{} x 10^6'.format(micro_value))
                time.sleep(1)
                print(f"""\nTHE PICO VALUE IS {round(pico_value, 4)} p """)
                to_back = input("\n\n-->  PRESS [ENTER] TO GO BACK TO CALCULATOR PAGE ")
                UserPAge.Calculator()
            elif calculator_choices == 3:
                os.system("cls")
                metre_value = float(input("ENTER THE VALUE IN POINT (m): "))
                second_value = float(input("ENTER THE VALUE IN POINT (s): "))
                velocity_value = metre_value / second_value
                os.system("cls")
                print('{} / {}'.format(metre_value, second_value ))
                print(f"""\nTHE VELOCITY VALUE IS {round(velocity_value, 2)} m/s """)
                to_back = input("\n\n-->  PRESS [ENTER] TO GO BACK TO CALCULATOR PAGE ")
                UserPAge.Calculator()
            elif calculator_choices == 4:
                os.system("cls")
                velocity_value = float(input("ENTER THE VALUE IN POINT (m/s): "))
                second_value = float(input("ENTER THE VALUE IN POINT (s): "))
                acceleration_value = velocity_value / second_value
                os.system("cls")
                print('{} / {}'.format(velocity_value, second_value ))
                print(f"""\nTHE ACCELERATION VALUE IS {round(acceleration_value, 2)} m/s^2 """)
                to_back = input("\n\n-->  PRESS [ENTER] TO GO BACK TO CALCULATOR PAGE ")
                UserPAge.Calculator()
            elif calculator_choices == 5:
                print("\n" + "-->  REDIRECTING TO STUDENT'S PAGE.", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO STUDENT'S PAGE..", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO STUDENT'S PAGE...", end = "\r")
                time.sleep(1)
                UserPAge.StudentsPage()
            else:
                print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
                time.sleep(1)
                print("\n-->  REDIRECTING TO CALCULATOR'S PAGE")
                time.sleep(1)
                UserPAge.Calculator()
        except ValueError:
            print("\n--> WRONG INPUT! ONLY INTEGER ALLOWED! ")
            time.sleep(1)
            print("\n-->  REDIRECTING TO CALCULATOR'S PAGE")
            time.sleep(1)
            UserPAge.Calculator()

    def ReviewPage():
        os.system("cls")
        welcome_text = " COMMENT SECTION "
        print("\n" + welcome_text.center(70, "-") + "\n")
        data_file = open("./Text_file/Review.txt", "r")
        lines = data_file.readlines()
        data_file.close()
        print("-" * 71)
        print(f"""|  CODE  |                    COMMENT                        |  NAME  |""")
        print("-" * 71)
        for line in lines:
            Review_info = line.split("| ")
            Review_topic = Review_info[1]
            Review_name = Review_info[2][:-1]
            if "A" in Review_info[0]:
                print("|" + Review_info[0].center(8) + "| " + Review_topic.ljust(50) + "|" + Review_name.center(8) + "|")
        print("-" * 71)
        print(f""" 
OPTION:
1. ADD COMMENT
2. DELETE COMMENT
3. EXIT
              """)
        try:
            review_choices = int(input("ENTER THE NUMBER [1|2|3]: "))
            if review_choices == 1:
                UserPAge.Addreview()
            elif review_choices == 2:
                UserPAge.deleteReview()
            elif review_choices == 3:
                print("\n" + "-->  REDIRECTING TO STUDENT'S PAGE.", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO STUDENT'S PAGE..", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO STUDENT'S PAGE...", end = "\r")
                time.sleep(1)
                UserPAge.StudentsPage()
            else:
                print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
                time.sleep(1)
                print("\n-->  REDIRECTING TO COMMENT SECTION")
                time.sleep(1)
                UserPAge.ReviewPage()
        except ValueError:
            print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
            time.sleep(1)
            print("\n-->  REDIRECTING TO COMMENT SECTION")
            time.sleep(1)
            UserPAge.ReviewPage()

    def Addreview():
        os.system("cls")
        welcome_text = " ADD COMMENT SECTION "
        print("\n" + welcome_text.center(70, "-") + "\n")
        code_found = False
        while code_found == False:
            os.system("cls")
            print("IF YOU WANT TO REFER TO THE COMMENT SECTION TYPE [EXIT]")
            item_name = input("\n-->  ADD YOUR NAME [Eg: FULAN]:\n")
            if item_name == "EXIT":
                UserPAge.ReviewPage()
                break
            item_new = item_name + " "
            item_comment = input("\n-->  ADD YOUR COMMENT [Eg: I LOVE IT!]:\n")
            if len(item_comment) > 30:
                print ("\nERROR! ONLY 30 CHARACTERS ALLOWED!")
                code_found = False
            else:
                code_found = True
                try:
                    item_code = int(input("\n-->  ENTER THE CODE [Eg: 100]: "))
                except ValueError:
                    print("\n--> WRONG INPUT! ONLY INTEGER ALLOWED!")
                    time.sleep(1)
                    print("\n--> TRY AGAIN, REDIRECTING TO ADD COMMENT SECTION...")
                    time.sleep(1)
                    UserPAge.Addreview()

                if len(str(item_code)) != 3:
                    print ("\nERROR! ONLY 3 DIGITS ALLOWED!")
                    time.sleep(1)
                    print("\n--> TRY AGAIN, REDIRECTING TO ADD COMMENT SECTION...")
                    time.sleep(1)
                    UserPAge.Addreview()

                else:                         
                    new_code = "A"+ str(item_code)
                    item = ("| ".join([new_code, item_comment, item_new]))
                    item_found = "Not Found"
                    if item_found == "Not Found":
                        with open("./Text_file/Review.txt") as file:
                            for line in file:
                                review_detail = list(line.split("| "))
                                if review_detail[0] == new_code:
                                    print("\n--> CODE ALREADY EXISTS! TRY AGAIN.")
                                    time.sleep(1)
                                    print("\n--> TRY AGAIN, REDIRECTING TO ADD COMMENT SECTION...")
                                    UserPAge.Addreview()
                                    break
                                else:
                                    item_found = "Found"
                        if item_found == "Found":
                            item = ("| ".join([new_code, item_comment, item_new]))
                            review_file = open("./Text_file/Review.txt", "a")
                            review_file.write( item + "\n")
                            review_file.close()
                        else:
                            continue
                    data_file = open("./Text_file/Review.txt", "r")
                    lines= data_file.readlines()
                    data_file.close()   

                    review_1 = []
                    write_file = open("./Text_file/Review.txt",'w')
                    for line in lines:
                        menu_info = line.split("| ")
                        review_1.append(menu_info)
                    review_1.sort(key = itemgetter(0))
                    for i in review_1:
                        write_file.write("| ".join(i))
                    write_file.close()  

                    print("\nTHE COMMENT HAD BEEN UPDATED :)")
                    time.sleep(1)
                    print("\nDIRECTING TO COMMENT SECTION")
                    time.sleep(1)
                    UserPAge.ReviewPage()

    def deleteReview():
        os.system("cls")
        welcome_text = " DELETE COMMENT SECTION "
        print("\n" + welcome_text.center(70, "-") + "\n")
        item_found = "Not Found"
        while item_found == "Not Found":
            print("IF YOU WANT TO REFER TO THE COMMENT SECTION TYPE [EXIT]")
            item_code = input("-->  ENTER THE CODE [Eg: A101]: ")
            if item_code.upper() == "EXIT":
                UserPAge.ReviewPage()
                break
            item_found = "Not Found"
            if item_found == "Not Found":
                with open("./Text_file/Review.txt") as file:
                    for line in file:
                        review_detail = list(line.split("| "))
                        if review_detail[0] == item_code.upper():

                            data_file = open("./Text_file/Review.txt", "r")
                            lines= data_file.readlines()
                            data_file.close()   

                            write_file = open("./Text_file/Review.txt",'w')
                            for review in lines:
                                review_info = review.split("| ")
                                review_code = review_info[0]
                                if item_code.upper() != review_code:
                                    write_file.write(review)
                            write_file.close()

                            print("\n\n  >>  COMMENT HAS BEEN DELETED :)")
                            print("\n-->  PLEASE LOOK AT THE COMMENT SECTION AGAIN :)")
                            time.sleep(2)
                            UserPAge.ReviewPage()
                            item_found = "Found"
                            break
                        else:
                            item_found = "Not Found"

                    if item_found == "Not Found":
                        print("-->  CODE NOT FOUND ! ")
                        time.sleep(1)
                        print("-->  PLEASE LOOK AT THE COMMENT SECTION TO FIND THE CODE :)")
                        to_back = input("\n-->  PRESS [ENTER] TO GO BACK TO COMMENT SECTION:\n")
                        UserPAge.ReviewPage()
                        break

    def logout():
        os.system("cls")
        print("\n" + " END SESSION PAGE ".center(50, "="))
        print("\n>>  Y = YES\n>>  N = NO\n")
        exit = str(input("\nDO YOU WANT TO END THE SESSION? [Y/N]: "))
        if exit.upper() == "Y" or exit.upper() == "YES":
            print("\n" + "-->  PLEASE WAIT A MOMENT.", end = "\r")
            time.sleep(1)
            print("-->  PLEASE WAIT A MOMENT..", end = "\r")
            time.sleep(1)
            print("-->  PLEASE WAIT A MOMENT...")
            time.sleep(1)
            print("-->  DONE")
            print("-->  THANK YOU! <3")
            

        elif exit.upper() == "N" or exit.upper() == "NO":
            print("\n" + "-->  REDIRECTING TO STUDENT'S PAGE.", end = "\r")
            time.sleep(1)
            print("-->  REDIRECTING TO STUDENT'S PAGE..", end = "\r")
            time.sleep(1)
            print("-->  REDIRECTING TO STUDENT'S PAGE...", end = "\r")
            time.sleep(1)
            UserPAge.StudentsPage() 
        
        else:
            print("\n--> WRONG INPUT! PLEASE TYPE EITHER 'Y' OR 'N'")
            time.sleep(1)
            UserPAge.logout()

class Admin_UserPage():
    def LecturerPage():
        os.system("cls")
        welcome_text = " LECTURER'S PAGE "
        print("\n" + welcome_text.center(70, "-") + "")
        print(""" 
        1. ADD LECTURER [ADMIN]
        2. REMOVE STUDENT'S ACCOUNT
        3. MANAGE QUESTION
        4. VIEW COMMENT SECTION
        5. LOG OUT """)
        try:
            students_option = int(input("\n-->  SELECT AN OPTION [1|2|3|4|5]: "))
            if students_option == 1:
                Admin_UserPage.addLecturer()
            elif students_option == 2:
                Admin_UserPage.remove_student()
            elif students_option == 3:
                Admin_UserPage.manage_question()
            elif students_option == 4:
                Admin_UserPage.Lecturer_ReviewPAge()
            elif students_option == 5:
                print("\n" + "-->  PLEASE WAIT A MOMENT.", end = "\r")
                time.sleep(1)
                print("-->  PLEASE WAIT A MOMENT..", end = "\r")
                time.sleep(1)
                print("-->  PLEASE WAIT A MOMENT...")
                time.sleep(1)
                Home_Page.welcome()
            else:
                print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
                time.sleep(1)
                Admin_UserPage.LecturerPage()
        except ValueError:
            print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
            time.sleep(1)
            Admin_UserPage.LecturerPage()

    # MUHAMMAD MUHAIMIN AFIF BIN MUHSIN
    def addLecturer():
        os.system('cls')
        print("\n" + "ADD LECTURER".center(70, "-") + "\n\n")
        print(" RULES TO CREATE USERNAME & PASSWORD ".center(50, "="))
        print("\n>> [USERNAME] : NO SPACES (' ') ARE ALLOWED")
        print(">> [PASSWORD] : NO SPACES ('') ARE ALLOWED")
        print("         SHOULD BE 6 OR MORE CHARACTERS LONG")
        print(">> [HANDPHONE NUMBER] : ONLY NUMBERS ARE ALLOWED")
        print("             NUMBERS SHOULD BE 10 OR 11 DIGITS\n")

        exist_username = []
        exist_password = []
        exist_details = []

        with open('./Text_file/Lecturer.txt','r') as file:
            for line in file:
                (key, val, more) = line.split(",")
                exist_username.append(key)
                exist_password.append(val)
                exist_details.append(more)

        # Input for admin's username and validation
        valid = "Not Found"
        while valid == "Not Found":
            print("\n--> TYPE [EXIT] TO GO TO LECTURER'S PAGE")
            name_lecturer = input("\nENTER NEW USERNAME: ")
            if name_lecturer.upper() == "EXIT":
                Admin_UserPage.LecturerPage()
                break
            pass_lecturer = input("\nENTER NEW PASSWORD: ")

            if name_lecturer in exist_username:
                    print("\nUSERNAME ALREADY EXIST ! ")
                    print("\nPLEASE ENTER THE USERNAME AGAIN :(")
                    valid = "Not Found"
                    time.sleep(1)

            else:
                if (" " in name_lecturer) == True:
                    print("\nUSERNAME CONTAIN '' (SPACE) ! TRY AGAIN ")
                    print("\nPLEASE ENTER THE USERNAME AGAIN :(")
                    valid = "Not Found"
                    time.sleep(1)
                elif (" " in pass_lecturer) == True:
                    print("\nPASSWORD CONTAIN '' (SPACE) ! TRY AGAIN ")
                    print("\nPLEASE ENTER THE USERNAME AND PASSWORD AGAIN :(")
                    valid = " NOT FOUND"
                    time.sleep(1)
                else:
                    if len(pass_lecturer) < 6:
                        print("\nPASSWORD LENGTH SHOULD BE 6 OR MORE ")
                        print("\nPLEASE ENTER THE USERNAME AND PASSWORD AGAIN :(")
                        valid = "Not Found"
                        time.sleep(1)
                    else:
                        try:
                            details_lecturer = int(input("\nENTER YOUR HANDPHONE NUMBER: "))
                            valid = "True"
                        except ValueError:
                            print("\nHANDPHONE NUMBER SHOULD ONLY BE INTEGER ! ")
                            print("\nPLEASE ENTER THE USERNAME, PASSWORD AND HANDPHONE NUMBER AGAIN :(")
                            valid = "Not Found"
                            time.sleep(3)
                            break
                    
                if valid == "True":

                    if len(str(details_lecturer)) != 9 and len(str(details_lecturer)) != 10:
                        print ("\nERROR! ONLY 10 OR 11 DIGITS ALLOWED!")
                        print("\nPLEASE ENTER THE USERNAME, PASSWORD AND HANDPHONE NUMBER AGAIN :(")
                        valid = "Not found"
                        time.sleep(3)

                    else:
                        valid = "Found"
                        if valid == "Found":
                            confirm_pass = input("\nENTER YOUR CONFIRMATION PASSWORD: ")
                            if confirm_pass == pass_lecturer:
                                print("\nYOUR REGISTRATION ARE BEING PROCESSED.", end = "\r")
                                time.sleep(1)
                                print("YOUR REGISTRATION ARE BEING PROCESSED..", end = "\r")
                                time.sleep(1)
                                print("YOUR REGISTRATION ARE BEING PROCESSED...")
                                time.sleep(3)
                                print("\n\n  >>  CONGRATULATIONS! NEW LECTURER HAS BEEN CREATED :)")
                                print("      PLEASE PROCEED TO LOGIN WITH REGISTERED USERNAME.\n\n")
                                new_user_info = (name_lecturer + ", " + pass_lecturer + ", " + "0" + str(details_lecturer))
                                user_info_file = open("./Text_file/Lecturer.txt", "a")
                                user_info_file.write("\n" + new_user_info)
                                user_info_file.close()
                                print("\n" + "  >>  REDIRECTING TO LECTURER PAGE.")
                                time.sleep(1)
                                Admin_UserPage.LecturerPage()

                            else:
                                print("\nYOUR CONFIRMATION PASSWORD ARE NOT SAME WITH PASSWORD !")
                                print("\nPLEASE ENTER THE USERNAME, PASSWORD AND HANDPHONE NUMBER AGAIN :(")
                                time.sleep(1)
                                valid = "Not Found"

    def remove_student():
        os.system("cls")
        print("\n" + "REMOVE STUDENT'S ACCOUNT".center(70, "-") + "\n\n")
        item_found = "Not Found"
        while item_found == "Not Found":
            print("\n--> TYPE [EXIT] TO GO TO LECTURER'S PAGE \n")
            student_name = input("--> ENTER STUDENT NAME [Eg: Fulan]:\n")
            if student_name == "EXIT":
                Admin_UserPage.LecturerPage()
                break
            else:
                item_found = "Not Found"
                if item_found == "Not Found":
                    with open("./Text_file/Student.txt") as file:
                        for line in file:
                            student_detail = list(line.split(", "))
                            if student_detail[0] == student_name:
                                data_file = open("./Text_file/Student.txt",'r')
                                lines = data_file.readlines()
                                data_file.close()
                                write_file = open("./Text_file/Student.txt",'w')
                                for student in lines:
                                    student_info = student.split(", ")
                                    student_code = student_info[0]
                                    if student_name != student_code:
                                        write_file.write(student)
                                write_file.close()

                                print("\n\n  >>  STUDENT ACCOUNT HAS BEEN DELETED :)")
                                time.sleep(1)
                                print("\n" + "  >>  REDIRECTING TO LECTURER PAGE.", end = "\r")
                                time.sleep(1)
                                print("  >>  REDIRECTING TO LECTURER PAGE..", end = "\r")
                                time.sleep(1)
                                print("  >>  REDIRECTING TO LECTURER PAGE...", end = "\r")
                                time.sleep(1)
                                Admin_UserPage.LecturerPage()
                                item_found = "Found"
                                break
                            else:
                                item_found = "Not Found"

                        if item_found == "Not Found":
                            print("--> STUDENT ACCOUNT NOT FOUND ! PLEASE CHECK THE NAME CORRECTLY :D", end = "\r")
                            time.sleep(1)
                            Admin_UserPage.remove_student()
                            break
                        else:
                            continue

    # NUR ADIBAH BINTI KHAIRUL ANUAR
    def manage_question():
        os.system("cls")
        welcome_text = " MANAGE QUESTION "
        print("\n" + welcome_text.center(70, "-"))
        print(f""" 
OPTION:
1. ADD QUESTION
2. EDIT QUESTION              
3. DELETE QUESTION
4. EXIT
              """)
        try:
            question_choices = int(input("ENTER THE NUMBER [1|2|3|4]: "))
            if question_choices == 1:
                Admin_UserPage.Add_Question_Page()
            elif question_choices == 2:
                Admin_UserPage.Edit_Question_Page()
            elif question_choices == 3:
                Admin_UserPage.Delete_Question_Page()
            elif question_choices == 4:
                print("\n" + "-->  REDIRECTING TO LECTURER PAGE.", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO LECTURER PAGE..", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO LECTURER PAGE...", end = "\r")
                time.sleep(1)
                Admin_UserPage.LecturerPage()
            else:
                print("\n--> WRONG INPUT! ONLY TYPE '1','2','3', OR '4'! ")
                time.sleep(1)
                print("\n-->  REDIRECTING TO MANAGE QUESTION")
                time.sleep(1)
                Admin_UserPage.manage_question()
        except ValueError:
            print("\n--> WRONG INPUT! ONLY TYPE '1','2','3', OR '4'! ")
            time.sleep(1)
            print("\n-->  REDIRECTING TO MANAGE QUESTION")
            time.sleep(1)
            Admin_UserPage.manage_question()

    # NURULAIN AFIQAH BINTI ABDULLAH
    def Add_Question_Page():
        os.system("cls")
        welcome_text = " ADD QUESTION "
        print("\n" + welcome_text.center(70, "-"))
        print(f""" 
TOPIC:
1. INTRODUCTION TO SI UNIT & DERIVED UNIT
2. STANDARD PREFIXES            
3. DISTANCE & DISPLACEMENT
4. SPEED & VELOCITY
5. EXIT
              """)
        try:
            topic_choices = int(input("ENTER THE NUMBER [1|2|3|4|5]: "))
            if topic_choices == 1:
                b=0
                while b==0:
                    os.system('cls')
                    with open('./Text_file/Quiz1.txt', 'r') as Add_Question1_r:
                        x = len(Add_Question1_r.readlines()) + 1
                    with open('./Text_file/Quiz1.txt', 'a') as Add_Question1:
                            welcome_text = " TOPIC 1 "
                            print("\n" + welcome_text.center(70, "-"))
                            print("\nIF YOU WANT TO REFER TO THE MANAGE QUESTION [EXIT]")
                            question = input(str("\nQUESTION [Eg: What is 1 + 1?]: "))
                            if question.upper() == "EXIT":
                                print("\n--> REDIRECTING TO THE MANAGE QUESTION")
                                time.sleep(1)
                                Admin_UserPage.manage_question()
                                break
                            a = input(str("\nA : "))
                            b = input(str("B : "))
                            c = input(str("C : "))
                            d = input(str("D : "))
                            m = 0
                            while m == 0:
                                ans = input(str("\nANSWER : ")).upper()
                                if ans == "A" or ans == "B" or ans == "C" or ans == "D" :
                                    m = 1
                                    n = 0
                                    while n == 0:
                                        print("\n>>  Y = YES\n>>  N = NO\n")
                                        confirmation = input("DO YOU WANT TO ADD THIS QUESTION? [Y/N] : ")
                                        if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                                            n=1
                                            num = "Q0" + str(x)
                                            new_question = num+"|"+str(question)+"|"+a+"|"+b+"|"+c+"|"+d+"|"+ans
                                            Add_Question1.write("\n"+new_question)
                                            b=0
                                            
                                            time.sleep(1)
                                            os.system('cls')
                                            print("--> QUESTION SUCCESSFULLY ADDED :)")
                                            time.sleep(1)
                                        
                                        elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                                            n=1
                                            os.system('cls')
                                            print ("--> REDIRECTING TO LECTURER PAGE")
                                            time.sleep(1)
                                            Admin_UserPage.LecturerPage()
                                        else :
                                            print ("--> WRONG INPUT! ONLY TYPE EITHER 'Y' OR 'N'!")

                                else:
                                    print("--> WRONG INPUT! ANSWER SHOULD BE 'A','B','C', OR 'D'!")
                                    time.sleep(1)

            elif topic_choices == 2:
                b=0
                while b==0:
                    os.system('cls')
                    with open('./Text_file/Quiz2.txt', 'r') as Add_Question2_r:
                        x = len(Add_Question2_r.readlines()) + 1
                    with open('./Text_file/Quiz2.txt', 'a') as Add_Question2:
                            welcome_text = " TOPIC 2 "
                            print("\n" + welcome_text.center(70, "-"))
                            print("\nIF YOU WANT TO REFER TO THE MANAGE QUESTION [EXIT]")
                            question = input(str("\nQUESTION [Eg: What is 1 + 1?]: "))
                            if question.upper() == "EXIT":
                                print("\n--> REDIRECTING TO THE MANAGE QUESTION")
                                time.sleep(1)
                                Admin_UserPage.manage_question()
                                break
                            a = input(str("\nA : "))
                            b = input(str("B : "))
                            c = input(str("C : "))
                            d = input(str("D : "))
                            m = 0
                            while m == 0:
                                ans = input(str("\nANSWER : ")).upper()
                                if ans == "A" or ans == "B" or ans == "C" or ans == "D" :
                                    m = 1
                                    n = 0
                                    while n == 0:
                                        print("\n>>  Y = YES\n>>  N = NO\n")
                                        confirmation = input("DO YOU WANT TO ADD THIS QUESTION? [Y/N] : ")
                                        if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                                            n=1
                                            num = "Q0" + str(x)
                                            new_question = num+"|"+str(question)+"|"+a+"|"+b+"|"+c+"|"+d+"|"+ans
                                            Add_Question2.write("\n"+new_question)
                                            b=0
                                            
                                            time.sleep(1)
                                            os.system('cls')
                                            print("--> QUESTION SUCCESSFULLY ADDED.")
                                            time.sleep(1)
                                        
                                        elif confirmation.upper() == "N" or confirmation.upper() ==  "NO":
                                            n=1
                                            os.system('cls')
                                            print ("--> REDIRECTING TO LECTURER PAGE.")
                                            time.sleep(1)
                                            Admin_UserPage.LecturerPage()
                                        else :
                                            print ("--> WRONG INPUT! ONLY TYPE EITHER 'Y' OR 'N'!")

                                else:
                                    print("--> WRONG INPUT! ANSWER SHOULD BE 'A','B','C', OR 'D'!")
                                    time.sleep(1)
            elif topic_choices == 3:
                b=0
                while b==0:
                    os.system('cls')
                    with open('./Text_file/Quiz3.txt', 'r') as Add_Question3_r:
                        x = len(Add_Question3_r.readlines()) + 1
                    with open('./Text_file/Quiz3.txt', 'a') as Add_Question3:
                            welcome_text = " TOPIC 3 "
                            print("\n" + welcome_text.center(70, "-"))
                            print("\nIF YOU WANT TO REFER TO THE MANAGE QUESTION [EXIT]")
                            question = input(str("\nQUESTION [Eg: What is 1 + 1?]: "))
                            if question.upper() == "EXIT":
                                print("\n--> REDIRECTING TO THE MANAGE QUESTION")
                                time.sleep(1)
                                Admin_UserPage.manage_question()
                                break
                            a = input(str("\nA : "))
                            b = input(str("B : "))
                            c = input(str("C : "))
                            d = input(str("D : "))
                            m = 0
                            while m == 0:
                                ans = input(str("\nANSWER : ")).upper()
                                if ans == "A" or ans == "B" or ans == "C" or ans == "D" :
                                    m = 1
                                    n = 0
                                    while n == 0:
                                        print("\n>>  Y = YES\n>>  N = NO\n")
                                        confirmation = input("DO YOU WANT TO ADD THIS QUESTION? [Y/N] : ")
                                        if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                                            n=1
                                            num = "Q0" + str(x)
                                            new_question = num+"|"+str(question)+"|"+a+"|"+b+"|"+c+"|"+d+"|"+ans
                                            Add_Question3.write("\n"+new_question)
                                            b=0
                                            
                                            time.sleep(1)
                                            os.system('cls')
                                            print("--> QUESTION SUCCESSFULLY ADDED.")
                                            time.sleep(1)
                                        
                                        elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                                            n=1
                                            os.system('cls')
                                            print ("--> REDIRECTING TO LECTURER PAGE")
                                            time.sleep(1)
                                            Admin_UserPage.LecturerPage()
                                        else :
                                            print ("--> WRONG INPUT! ONLY TYPE EITHER 'Y' OR 'N'!")

                                else:
                                    print("--> WRONG INPUT! ANSWER SHOULD BE 'A','B','C', OR 'D'!")
                                    time.sleep(1)
            elif topic_choices == 4:
                b=0
                while b==0:
                    os.system('cls')
                    with open('./Text_file/Quiz4.txt', 'r') as Add_Question4_r:
                        x = len(Add_Question4_r.readlines()) + 1
                    with open('./Text_file/Quiz4.txt', 'a') as Add_Question4:
                            welcome_text = " TOPIC 4 "
                            print("\n" + welcome_text.center(70, "-"))
                            print("\nIF YOU WANT TO REFER TO THE MANAGE QUESTION [EXIT]")
                            question = input(str("\nQUESTION [Eg: What is 1 + 1?]: "))
                            if question.upper() == "EXIT":
                                print("\n--> REDIRECTING TO THE MANAGE QUESTION")
                                time.sleep(1)
                                Admin_UserPage.manage_question()
                                break
                            a = input(str("\nA : "))
                            b = input(str("B : "))
                            c = input(str("C : "))
                            d = input(str("D : "))
                            m = 0
                            while m == 0:
                                ans = input(str("\nANSWER : ")).upper()
                                if ans == "A" or ans == "B" or ans == "C" or ans == "D" :
                                    m = 1
                                    n = 0
                                    while n == 0:
                                        print("\n>>  Y = YES\n>>  N = NO\n")
                                        confirmation = input("DO YOU WANT TO ADD THIS QUESTION? [Y/N] : ")
                                        if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                                            n=1
                                            num = "Q0" + str(x)
                                            new_question = num+"|"+str(question)+"|"+a+"|"+b+"|"+c+"|"+d+"|"+ans
                                            Add_Question4.write("\n"+new_question)
                                            b=0
                                            
                                            time.sleep(1)
                                            os.system('cls')
                                            print("--> QUESTION SUCCESSFULLY ADDED.")
                                            time.sleep(1)
                                        
                                        elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                                            n=1
                                            os.system('cls')
                                            print ("--> REDIRECTING TO LECTURER PAGE")
                                            time.sleep(1)
                                            Admin_UserPage.LecturerPage()
                                        else :
                                            print ("--> WRONG INPUT! ONLY TYPE EITHER 'Y' OR 'N'!")

                                else:
                                    print("--> WRONG INPUT! ANSWER SHOULD BE 'A','B','C', OR 'D'!")
                                    time.sleep(1)
            elif topic_choices == 5:
                print("\n" + "-->  REDIRECTING TO MANAGE QUESTION.", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO MANAGE QUESTION..", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO MANAGE QUESTION...", end = "\r")
                time.sleep(1)
                Admin_UserPage.manage_question()
            else:
                print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
                time.sleep(1)
                print("\n-->  REDIRECTING TO ADD QUESTION")
                time.sleep(1)
                Admin_UserPage.Add_Question_Page()
        except ValueError:
            print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
            time.sleep(1)
            print("\n-->  REDIRECTING TO ADD QUESTION")
            time.sleep(1)
            Admin_UserPage.Add_Question_Page()

    # NURULAIN AFIQAH BINTI ABDULLAH & NUR ADIBAH BINTI KHAIRUL ANUAR
    def Edit_Question_Page():
        os.system("cls")
        welcome_text = " EDIT QUESTION "
        print("\n" + welcome_text.center(70, "-") + "\n")
        print(f""" 
TOPIC:
1. INTRODUCTION TO SI UNIT & DERIVED UNIT
2. STANDARD PREFIXES            
3. DISTANCE & DISPLACEMENT
4. SPEED & VELOCITY
5. EXIT
              """)
        try:
            topic_choices = int(input("ENTER THE NUMBER: "))
            if topic_choices == 1:
                Admin_UserPage.editQuestion1()
            elif topic_choices == 2:
                Admin_UserPage.editQuestion2()
            elif topic_choices == 3:
                Admin_UserPage.editQuestion3()
            elif topic_choices == 4:
                Admin_UserPage.editQuestion4()
            elif topic_choices == 5:
                print("\n" + "-->  REDIRECTING TO MANAGE QUESTION.", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO MANAGE QUESTION..", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO MANAGE QUESTION...", end = "\r")
                time.sleep(1)
                Admin_UserPage.manage_question()
            else:
                print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
                time.sleep(1)
                print("\n-->  REDIRECTING TO EDIT QUESTION")
                time.sleep(1)
                Admin_UserPage.Edit_Question_Page()
        except ValueError:
            print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
            time.sleep(1)
            print("\n-->  REDIRECTING TO EDIT QUESTION")
            time.sleep(1)
            Admin_UserPage.Edit_Question_Page()


#***************EDIT QUESTION TOPIC1*************************************************
    def editQuestion1():
        os.system("cls")
        welcome_text = "<< EDIT QUESTION >>"
        print("\n" + welcome_text.center(70, "-") + "\n" + "QUESTIONS TOPIC 1".center(70) + "\n")
        data_file = open("./Text_file/Quiz1.txt", "r")
        lines = data_file.readlines()
        data_file.close()
        condition = True
        for line in lines:
            Notes_info = line.split("|")
            if "Q" in Notes_info[0]:
                print(Notes_info[0] + " : " + Notes_info[1])

        while condition == True:
                print("\nIF YOU WANT TO REFER TO THE STUDENTS PAGE TYPE [EXIT]")
                code = input("\nQUESTION CODE [Eg: Q01]: ").upper()
                if code.upper() == "EXIT":
                    print("--> REDIRECTING TO THE LECTURER PAGE")
                    Admin_UserPage.LecturerPage()
                    break
                for line in lines:
                    edit_info = line.split("|")
                    edit_question = edit_info[0]
                    if code in edit_question:
                        print("\n",edit_question,". ",edit_info[1])
                        n = 0
                        while n == 0:
                            print("\n>>  Y = YES\n>>  N = NO\n")
                            confirmation = input("DO YOU WANT TO EDIT THIS QUESTION? [Y/N] : ")
                            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                                n=1
                                with open(r'./Text_file/Quiz1.txt', 'r',encoding='utf-8') as Edit_Question1_r:
                                    data = Edit_Question1_r.readlines()
                                    for line in data:
                                        if line.find(code) != -1:
                                            os.system('cls')
                                            print("EDIT QUESTION\n")
                                            question = input("NEW QUESTION [Eg : What is 1 + 1?]: ")
                                            a = input(str("\nA : "))
                                            b = input(str("B : "))
                                            c = input(str("C : "))
                                            d = input(str("D : "))
                                            condition = True 
                                            while condition == True:
                                                ans = input(str("\nANSWER : "))
                                                if ans.upper() == "A" or ans.upper() == "B" or ans.upper() == "C" or ans.upper() == "D":
                                                    condition = False
                                                    n = 0
                                                    while n == 0:
                                                        print("\n>>  Y = YES\n>>  N = NO\n")
                                                        confirmation = input("ARE YOU SURE YOU WANT TO EDIT THIS QUESTION? [Y/N] : ")
                                                        if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                                                            item_added = "found"
                                                            if item_added == "found":
                                                                write_file = open("./Text_file/Quiz1.txt",'w')
                                                                n = 1
                                                                for line in lines:
                                                                    edit_info = line.split("|")
                                                                    edit_question = edit_info[0]
                                                                    if code != edit_question:
                                                                        write_file.write(line)
                                                                write_file.close()

                                                                if n == 1:
                                                                    item = ("|".join([code, question, a, b, c, d, ans.upper()]))
                                                                    quiz_file = open("./Text_file/Quiz1.txt", "a")
                                                                    if code == "Q01":
                                                                        quiz_file.write( "\n" + item + "\n")
                                                                        quiz_file.close()
                                                                    else:
                                                                        quiz_file.write(  item + "\n")
                                                                        quiz_file.close()
                                                                    
                                                                else:
                                                                    continue
                                                            data_file = open("./Text_file/Quiz1.txt", "r")
                                                            lines = data_file.readlines()
                                                            data_file.close()
                                                            
                                                                
                                                            
                                                            edit_new = []
                                                            write_file = open("./Text_file/Quiz1.txt",'w')
                                                            for line in lines:
                                                                edit_info = line.split("|")
                                                                edit_new.append(edit_info)
                                                                if line == "\n":
                                                                    write_file.write(line)
                                                                else:                
                                                                    continue
                                                            edit_new.sort(key = itemgetter(0))
                                                            for i in edit_new:
                                                                write_file.write("|".join(i))
                                                            write_file.close()
                                                            

                                                            print("--> QUESTION SUCCESSFULLY EDITED.")
                                                            time.sleep(2)
                                                            print("\n--> DIRECTING TO LECTURER PAGE")
                                                            time.sleep(1)
                                                            Admin_UserPage.LecturerPage()

                                                        elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                                                            print("\n" + "-->  REDIRECTING TO EDIT QUESTION.")
                                                            time.sleep(1)
                                                            Admin_UserPage.Edit_Question_Page()  
                                                          
                                                        else:
                                                            print("WRONG INPUT! TYPE EITHER 'Y' OR 'N'! ")
                                                            n = 0

                                                else:
                                                    print("--> ONLY A, B, C, D, FOR THE ANSWER! ")
                                                    condition = True
                                        
                            elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                                n=1
                                os.system('cls')
                                print("\n" + "-->  REDIRECTING TO EDIT QUESTION.")
                                time.sleep(1)
                                Admin_UserPage.Edit_Question_Page()
                            else :
                                print ("WRONG INPUT! TYPE EITHER 'Y' OR 'N'! ")
                                time.sleep(1)
                                n = 0

#***************EDIT QUESTION TOPIC2*************************************************
    def editQuestion2():
        os.system("cls")
        welcome_text = "<< EDIT QUESTION >>"
        print("\n" + welcome_text.center(70, "-") + "\n" + "QUESTIONS TOPIC 2".center(70) + "\n")
        data_file = open("./Text_file/Quiz2.txt", "r")
        lines = data_file.readlines()
        data_file.close()
        condition = True
        for line in lines:
            Notes_info = line.split("|")
            if "Q" in Notes_info[0]:
                print(Notes_info[0] + " : " + Notes_info[1])

        while condition == True:
                print("\nIF YOU WANT TO REFER TO THE STUDENTS PAGE TYPE [EXIT]")
                code = input("\nQUESTION CODE [Eg : Q01]: ")
                if code.upper() == "EXIT":
                    print("--> REDIRECTING TO THE LECTURER PAGE")
                    Admin_UserPage.LecturerPage()
                    break
                for line in lines:
                    edit_info = line.split("|")
                    edit_question = edit_info[0]
                    if code in edit_question:
                        print("\n",edit_question,". ",edit_info[1])
                        n = 0
                        while n == 0:
                            print("\n>>  Y = YES\n>>  N = NO\n")
                            confirmation = input("DO YOU WANT TO EDIT THIS QUESTION? [Y/N] : ")
                            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                                n=1
                                with open(r'./Text_file/Quiz2.txt', 'r',encoding='utf-8') as Edit_Question2_r:
                                    data = Edit_Question2_r.readlines()
                                    for line in data:
                                        if line.find(code) != -1:
                                            os.system('cls')
                                            print("EDIT QUESTION\n")
                                            question = input("NEW QUESTION [Eg : What is 1 + 1?]:   ")
                                            a = input(str("\nA : "))
                                            b = input(str("B : "))
                                            c = input(str("C : "))
                                            d = input(str("D : "))
                                            condition = True 
                                            while condition == True:
                                                ans = input(str("\nANSWER : "))
                                                if ans.upper() == "A" or ans.upper() == "B" or ans.upper() == "C" or ans.upper() == "D":
                                                    condition = False
                                                    n = 0
                                                    while n == 0:
                                                        print("\n>>  Y = YES\n>>  N = NO\n")
                                                        confirmation = input("ARE YOU SURE YOU WANT TO EDIT THIS QUESTION? [Y/N] : ")
                                                        if confirmation.upper() == "Y" or confirmation.upper() == "YES" :
                                                            item_added = "found"
                                                            if item_added == "found":
                                                                write_file = open("./Text_file/Quiz2.txt",'w')
                                                                n = 1
                                                                for line in lines:
                                                                    edit_info = line.split("|")
                                                                    edit_question = edit_info[0]
                                                                    if code != edit_question:
                                                                        write_file.write(line)
                                                                write_file.close()

                                                                if n == 1:
                                                                    item = ("|".join([code, question, a, b, c, d, ans.upper()]))
                                                                    quiz_file = open("./Text_file/Quiz2.txt", "a")
                                                                    if code == "Q01":
                                                                        quiz_file.write( "\n" + item + "\n")
                                                                        quiz_file.close()
                                                                    else:
                                                                        quiz_file.write(  item + "\n")
                                                                        quiz_file.close()
                                                                else:
                                                                    continue
                            
                                                            data_file = open("./Text_file/Quiz2.txt", "r")
                                                            lines = data_file.readlines()
                                                            data_file.close()
                                                            
                                                            edit_new = []
                                                            write_file = open("./Text_file/Quiz2.txt",'w')
                                                            for line in lines:
                                                                edit_info = line.split("|")
                                                                edit_new.append(edit_info)
                                                                if line == "\n":
                                                                        write_file.write(line)
                                                                else:                
                                                                    continue
                                                            edit_new.sort(key = itemgetter(0))
                                                            for i in edit_new:
                                                                write_file.write("|".join(i))
                                                            write_file.close()  

                                                            print("--> QUESTION SUCCESSFULLY EDITED.")
                                                            time.sleep(2)
                                                            print("\n--> DIRECTING TO LECTURER PAGE")
                                                            time.sleep(1)
                                                            Admin_UserPage.LecturerPage()

                                                        elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                                                            print("\n" + "-->  REDIRECTING TO EDIT QUESTION.")
                                                            time.sleep(1)    
                                                            Admin_UserPage.Edit_Question_Page()

                                                        else:
                                                            print("WRONG INPUT! TYPE EITHER 'Y' OR 'N'! ")
                                                            n = 0
                                                else:
                                                    print("--> ONLY A, B, C, D, FOR THE ANSWER! ")
                                                    condition = True
                                        
                            elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                                n=1
                                os.system('cls')
                                print("\n" + "-->  REDIRECTING TO EDIT QUESTION.")
                                time.sleep(1)
                                Admin_UserPage.Edit_Question_Page()
                            else :
                                print("WRONG INPUT! TYPE EITHER 'Y' OR 'N'! ")
                                time.sleep(1)
                                n = 0

#***************EDIT QUESTION TOPIC3*************************************************
    def editQuestion3():
        os.system("cls")
        welcome_text = "<< EDIT QUESTION >>"
        print("\n" + welcome_text.center(70, "-") + "\n" + "QUESTIONS TOPIC 3".center(70) + "\n")
        data_file = open("./Text_file/Quiz3.txt", "r")
        lines = data_file.readlines()
        data_file.close()
        condition = True
        for line in lines:
            Notes_info = line.split("|")
            if "Q" in Notes_info[0]:
                print(Notes_info[0] + " : " + Notes_info[1])

        while condition == True:
                print("\nIF YOU WANT TO REFER TO THE STUDENTS PAGE TYPE [EXIT]")
                code = input("\nQUESTION CODE [Eg : Q01]: ").upper()
                if code.upper() == "EXIT":
                    print("--> REDIRECTING TO THE LECTURER PAGE")
                    Admin_UserPage.LecturerPage()
                    break
                for line in lines:
                    edit_info = line.split("|")
                    edit_question = edit_info[0]
                    if code in edit_question:
                        print("\n",edit_question,". ",edit_info[1])
                        n = 0
                        while n == 0:
                            print("\n>>  Y = YES\n>>  N = NO\n")
                            confirmation = input("DO YOU WANT TO EDIT THIS QUESTION? [Y/N] : ")
                            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                                n=1
                                with open(r'./Text_file/Quiz3.txt', 'r',encoding='utf-8') as Edit_Question3_r:
                                    data = Edit_Question3_r.readlines()
                                    for line in data:
                                        if line.find(code) != -1:
                                            os.system('cls')
                                            print("EDIT QUESTION\n")
                                            question = input("NEW QUESTION [Eg : What is 1 + 1?]: ")
                                            a = input(str("\nA : "))
                                            b = input(str("B : "))
                                            c = input(str("C : "))
                                            d = input(str("D : "))
                                            condition = True 
                                            while condition == True:
                                                ans = input(str("\nANSWER : "))
                                                if ans.upper() == "A" or ans.upper() == "B" or ans.upper() == "C" or ans.upper() == "D":
                                                    condition = False
                                                    n = 0
                                                    while n == 0:
                                                        print("\n>>  Y = YES\n>>  N = NO\n")
                                                        confirmation = input("ARE YOU SURE YOU WANT TO EDIT THIS QUESTION? [Y/N] : ")
                                                        if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                                                            item_added = "found"
                                                            if item_added == "found":
                                                                write_file = open("./Text_file/Quiz3.txt",'w')
                                                                n = 1
                                                                for line in lines:
                                                                    edit_info = line.split("|")
                                                                    edit_question = edit_info[0]
                                                                    if code != edit_question:
                                                                        write_file.write(line)
                                                                write_file.close()

                                                                if n == 1:
                                                                    item = ("|".join([code, question, a, b, c, d, ans.upper()]))
                                                                    quiz_file = open("./Text_file/Quiz3.txt", "a")
                                                                    if code == "Q01":
                                                                        quiz_file.write( "\n" + item + "\n")
                                                                        quiz_file.close()
                                                                    else:
                                                                        quiz_file.write(  item + "\n")
                                                                        quiz_file.close()
                                                                else:
                                                                    continue
                                                            data_file = open("./Text_file/Quiz3.txt", "r")
                                                            lines = data_file.readlines()
                                                            data_file.close()
                                                            
                                                            edit_new = []
                                                            write_file = open("./Text_file/Quiz3.txt",'w')
                                                            for line in lines:
                                                                edit_info = line.split("|")
                                                                edit_new.append(edit_info)
                                                                if line == "\n":
                                                                        write_file.write(line)
                                                                else:                
                                                                    continue
                                                            edit_new.sort(key = itemgetter(0))
                                                            for i in edit_new:
                                                                write_file.write("|".join(i))
                                                            write_file.close() 

                                                            print("--> QUESTION SUCCESSFULLY EDITED.")
                                                            time.sleep(2)
                                                            print("\n--> DIRECTING TO LECTURER PAGE")
                                                            time.sleep(1)
                                                            Admin_UserPage.LecturerPage()

                                                        elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                                                            print("\n" + "-->  REDIRECTING TO EDIT QUESTION.")
                                                            time.sleep(1)    
                                                            Admin_UserPage.Edit_Question_Page()
                                                        else:
                                                            print("WRONG INPUT! TYPE EITHER 'Y' OR 'N'! ")
                                                            n = 0
                                                else:
                                                    print("--> ONLY A, B, C, D, FOR THE ANSWER! ")
                                                    condition = True
                                        
                            elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                                n=1
                                os.system('cls')
                                print("\n" + "-->  REDIRECTING TO EDIT QUESTION.")
                                time.sleep(1)
                                Admin_UserPage.Edit_Question_Page()
                            else :
                                print("WRONG INPUT! TYPE EITHER 'Y' OR 'N'! ")
                                time.sleep(1)
                                n = 0

#***************EDIT QUESTION TOPIC4*************************************************
    def editQuestion4():
        os.system("cls")
        welcome_text = "<< EDIT QUESTION >>"
        print("\n" + welcome_text.center(70, "-") + "\n" + "QUESTIONS TOPIC 4".center(70) + "\n")
        data_file = open("./Text_file/Quiz4.txt", "r")
        lines = data_file.readlines()
        data_file.close()
        condition = True
        for line in lines:
            Notes_info = line.split("|")
            if "Q" in Notes_info[0]:
                print(Notes_info[0] + " : " + Notes_info[1])

        while condition == True:
                print("\nIF YOU WANT TO REFER TO THE STUDENTS PAGE TYPE [EXIT]")
                code = input("\nQUESTION CODE [Eg : Q01]: ").upper()
                if code.upper() == "EXIT":
                    print("--> REDIRECTING TO THE LECTURER PAGE")
                    Admin_UserPage.LecturerPage()
                    break
                for line in lines:
                    edit_info = line.split("|")
                    edit_question = edit_info[0]
                    if code in edit_question:
                        print("\n",edit_question,". ",edit_info[1])
                        n = 0
                        while n == 0:
                            print("\n>>  Y = YES\n>>  N = NO\n")
                            confirmation = input("DO YOU WANT TO EDIT THIS QUESTION? [Y/N] : ")
                            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                                n=1
                                with open(r'./Text_file/Quiz4.txt', 'r',encoding='utf-8') as Edit_Question4_r:
                                    data = Edit_Question4_r.readlines()
                                    for line in data:
                                        if line.find(code) != -1:
                                            os.system('cls')
                                            print("EDIT QUESTION\n")
                                            question = input("NEW QUESTION [Eg : What is 1 + 1?]: ")
                                            y = data.index(line)
                                            a = input(str("\nA : "))
                                            b = input(str("B : "))
                                            c = input(str("C : "))
                                            d = input(str("D : "))
                                            condition = True 
                                            while condition == True:
                                                ans = input(str("\nANSWER : "))
                                                if ans.upper() == "A" or ans.upper() == "B" or ans.upper() == "C" or ans.upper() == "D":
                                                    condition = False
                                                    n = 0
                                                    while n == 0:
                                                        print("\n>>  Y = YES\n>>  N = NO\n")
                                                        confirmation = input("ARE YOU SURE YOU WANT TO EDIT THIS QUESTION? [Y/N] : ")
                                                        if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                                                            item_added = "found"
                                                            if item_added == "found":
                                                                write_file = open("./Text_file/Quiz4.txt",'w')
                                                                n = 1
                                                                for line in lines:
                                                                    edit_info = line.split("|")
                                                                    edit_question = edit_info[0]
                                                                    if code != edit_question:
                                                                        write_file.write(line)
                                                                write_file.close()

                                                                if n == 1:
                                                                    item = ("|".join([code, question, a, b, c, d, ans.upper()]))
                                                                    quiz_file = open("./Text_file/Quiz4.txt", "a")
                                                                    if code == "Q01":
                                                                        quiz_file.write( "\n" + item + "\n")
                                                                        quiz_file.close()
                                                                    else:
                                                                        quiz_file.write(  item + "\n")
                                                                        quiz_file.close()
                                                                else:
                                                                    continue
                                                            data_file = open("./Text_file/Quiz4.txt", "r")
                                                            lines = data_file.readlines()
                                                            data_file.close()
                                                            
                                                            edit_new = []
                                                            write_file = open("./Text_file/Quiz4.txt",'w')
                                                            for line in lines:
                                                                edit_info = line.split("|")
                                                                edit_new.append(edit_info)
                                                                if line == "\n":
                                                                        write_file.write(line)
                                                                else:                
                                                                    continue
                                                            edit_new.sort(key = itemgetter(0))
                                                            for i in edit_new:
                                                                write_file.write("|".join(i))
                                                            write_file.close()
                                        
                                                            print("--> QUESTION SUCCESSFULLY EDITED.")
                                                            time.sleep(2)
                                                            print("\n--> DIRECTING TO LECTURER PAGE")
                                                            time.sleep(1)
                                                            Admin_UserPage.LecturerPage()

                                                        elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                                                            print("\n" + "-->  REDIRECTING TO EDIT QUESTION.")
                                                            time.sleep(1)  
                                                        else:
                                                            print("WRONG INPUT! TYPE EITHER 'Y' OR 'N'! ")
                                                            n = 0  
                                                else:
                                                    print("--> ONLY A, B, C, D, FOR THE ANSWER! ")
                                                    condition = True
                                        
                            elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                                n=1
                                os.system('cls')
                                print("\n" + "-->  REDIRECTING TO EDIT QUESTION.")
                                time.sleep(1)
                                Admin_UserPage.Edit_Question_Page()
                            else :
                                print("WRONG INPUT! TYPE EITHER 'Y' OR 'N'! ")
                                time.sleep(1)
                                n = 0

    # NURULAIN AFIQAH BINTI ABDULLAH
    def Delete_Question_Page():
        os.system("cls")
        welcome_text = " DELETE QUESTION "
        print("\n" + welcome_text.center(70, "-"))
        print(f""" 
TOPIC:
1. INTRODUCTION TO SI UNIT & DERIVED UNIT
2. STANDARD PREFIXES            
3. DISTANCE & DISPLACEMENT
4. SPEED & VELOCITY
5. EXIT
              """)
        try:
            topic_choices = int(input("ENTER THE NUMBER: "))
            if topic_choices == 1:
                Admin_UserPage.deleteQuestion1()
            elif topic_choices == 2:
                Admin_UserPage.deleteQuestion2()
            elif topic_choices == 3:
                Admin_UserPage.deleteQuestion3()
            elif topic_choices == 4:
                Admin_UserPage.deleteQuestion4()
            elif topic_choices == 5:
                print("\n" + "-->  REDIRECTING TO MANAGE QUESTION.", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO MANAGE QUESTION..", end = "\r")
                time.sleep(1)
                print("-->  REDIRECTING TO MANAGE QUESTION...", end = "\r")
                time.sleep(1)
                Admin_UserPage.manage_question()
            else:
                print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
                time.sleep(1)
                print("\n-->  REDIRECTING TO DELETE QUESTION")
                time.sleep(1)
                Admin_UserPage.Delete_Question_Page()
        except ValueError:
            print("\n--> WRONG INPUT! ONLY TYPE '1','2','3','4', OR '5'! ")
            time.sleep(1)
            print("\n-->  REDIRECTING TO DELETE QUESTION")
            time.sleep(1)
            Admin_UserPage.Delete_Question_Page()

    def deleteQuestion1():
        os.system("cls")
        item_found = "Not Found"
        while item_found == "Not Found":
            welcome_text = "<< TOPIC 1 >>"
            print("\n" + welcome_text.center(70, "-") + "\n")
            data_file = open("./Text_file/Quiz1.txt", "r")
            lines = data_file.readlines()
            data_file.close()
            for line in lines:
                Notes_info = line.split("|")
                if "Q" in Notes_info[0]:
                    print(Notes_info[0] + " : " + Notes_info[1])

            print("\n-->  TYPE [EXIT] TO GO TO MANAGE QUESION ")
            item_code = input("\n-->  ENTER QUESTION'S CODE [Eg : Q01]: ").upper()
            if item_code.upper() == "EXIT":
                Admin_UserPage.manage_question()
                break
            else:
                item_found = "Not Found"
                if item_found == "Not Found":
                    with open("./Text_file/Quiz1.txt") as file:
                        for line in file:
                            question_detail = list(line.split("|"))
                            if question_detail[0] == item_code:
                                data_file  = open("./Text_file/Quiz1.txt",'r')
                                lines = data_file.readlines()
                                data_file.close()
                                write_file = open("./Text_file/Quiz1.txt",'w')
                                x = -1
                                for question in lines:
                                    question_info = question.split("|")
                                    question_code = question_info[0]
                                    if item_code != question_code:
                                        x = x + 1
                                        Question = "Q0"+str(x+1)+"|"+question_info[1]+"|"+question_info[2]+"|"+question_info[3]+"|"+question_info[4]+"|"+question_info[5]+"|"+question_info[6]
                                        write_file.write(Question)
                                write_file.close()
                                print("\n\n  >>  ITEM HAS BEEN DELETED :)")
                                time.sleep(2)
                                item_found = "Found"
                                Admin_UserPage.deleteQuestion1()
                                break
                            else:
                                item_found = "Not Found"
            
                    if item_found == "Not Found":
                        print("-->  CODE NOT FOUND! PLEASE CHECK THE CODE CORRECTLY!", end = "\r")
                        time.sleep(1)
                        Admin_UserPage.deleteQuestion1()
                        break
                    else:
                        continue

    def deleteQuestion2():
        os.system("cls")
        item_found = "Not Found"
        while item_found == "Not Found":
            welcome_text = "<< TOPIC 2 >>"
            print("\n" + welcome_text.center(70, "-") + "\n")
            data_file = open("./Text_file/Quiz2.txt", "r")
            lines = data_file.readlines()
            data_file.close()
            for line in lines:
                Notes_info = line.split("|")
                if "Q" in Notes_info[0]:
                    print(Notes_info[0] + " : " + Notes_info[1])

            print("\n-->  TYPE [EXIT] TO GO TO MANAGE QUESTION")
            item_code = input("\n-->  ENTER QUESTION'S CODE [Eg : Q01]: ").upper()
            if item_code.upper() == "EXIT":
                Admin_UserPage.manage_question()
                break
            else:
                item_found = "Not Found"
                if item_found == "Not Found":
                    with open("./Text_file/Quiz2.txt") as file:
                        for line in file:
                            question_detail = list(line.split("|"))
                            if question_detail[0] == item_code:
                                data_file  = open("./Text_file/Quiz2.txt",'r')
                                lines = data_file.readlines()
                                data_file.close()
                                write_file = open("./Text_file/Quiz2.txt",'w')
                                x = -1
                                for question in lines:
                                    question_info = question.split("|")
                                    question_code = question_info[0]
                                    if item_code != question_code:
                                        x = x + 1
                                        Question = "Q0"+str(x+1)+"|"+question_info[1]+"|"+question_info[2]+"|"+question_info[3]+"|"+question_info[4]+"|"+question_info[5]+"|"+question_info[6]
                                        write_file.write(Question)
                                write_file.close()
                                print("\n\n  >>  ITEM HAS BEEN DELETED :)")
                                time.sleep(2)
                                item_found = "Found"
                                Admin_UserPage.deleteQuestion2()
                                break
                            else:
                                item_found = "Not Found"
            
                    if item_found == "Not Found":
                        print("-->  CODE NOT FOUND! PLEASE CHECK THE CODE CORRECTLY!", end = "\r")
                        time.sleep(1)
                        Admin_UserPage.deleteQuestion2()
                        break
                    else:
                        continue

    def deleteQuestion3():
        os.system("cls")
        item_found = "Not Found"
        while item_found == "Not Found":
            welcome_text = "<< TOPIC 3 >>"
            print("\n" + welcome_text.center(70, "-") + "\n")
            data_file = open("./Text_file/Quiz3.txt", "r")
            lines = data_file.readlines()
            data_file.close()
            for line in lines:
                Notes_info = line.split("|")
                if "Q" in Notes_info[0]:
                    print(Notes_info[0] + " : " + Notes_info[1])

            print("\n-->  TYPE [EXIT] TO GO TO MANAGE QUESTION")
            item_code = input("\n-->  ENTER QUESTION'S CODE [Eg : Q01]: ").upper()
            if item_code.upper() == "EXIT":
                Admin_UserPage.manage_question()
                break
            else:
                item_found = "Not Found"
                if item_found == "Not Found":
                    with open("./Text_file/Quiz3.txt") as file:
                        for line in file:
                            question_detail = list(line.split("|"))
                            if question_detail[0] == item_code:
                                data_file  = open("./Text_file/Quiz3.txt",'r')
                                lines = data_file.readlines()
                                data_file.close()
                                write_file = open("./Text_file/Quiz3.txt",'w')
                                x = -1
                                for question in lines:
                                    question_info = question.split("|")
                                    question_code = question_info[0]
                                    if item_code != question_code:
                                        x = x + 1
                                        Question = "Q0"+str(x+1)+"|"+question_info[1]+"|"+question_info[2]+"|"+question_info[3]+"|"+question_info[4]+"|"+question_info[5]+"|"+question_info[6]
                                        write_file.write(Question)
                                write_file.close()
                                print("\n\n  >>  ITEM HAS BEEN DELETED :)")
                                time.sleep(2)
                                item_found = "Found"
                                Admin_UserPage.deleteQuestion3()
                                break
                            else:
                                item_found = "Not Found"
            
                    if item_found == "Not Found":
                        print("-->  CODE NOT FOUND! PLEASE CHECK THE CODE CORRECTLY", end = "\r")
                        time.sleep(1)
                        Admin_UserPage.deleteQuestion3()
                        break
                    else:
                        continue

    def deleteQuestion4():
        os.system("cls")
        item_found = "Not Found"
        while item_found == "Not Found":
            welcome_text = "<< TOPIC 4 >>"
            print("\n" + welcome_text.center(70, "-") + "\n")
            data_file = open("./Text_file/Quiz4.txt", "r")
            lines = data_file.readlines()
            data_file.close()
            for line in lines:
                Notes_info = line.split("|")
                if "Q" in Notes_info[0]:
                    print(Notes_info[0] + " : " + Notes_info[1])

            print("\n-->  TYPE [EXIT] TO GO TO MANAGE QUESTION")
            item_code = input("\n-->  ENTER QUESTION'S CODE [Eg : Q01]: ").upper()
            if item_code.upper() == "EXIT":
                Admin_UserPage.manage_question()
                break
            else:
                item_found = "Not Found"
                if item_found == "Not Found":
                    with open("./Text_file/Quiz4.txt") as file:
                        for line in file:
                            question_detail = list(line.split("|"))
                            if question_detail[0] == item_code:
                                data_file  = open("./Text_file/Quiz4.txt",'r')
                                lines = data_file.readlines()
                                data_file.close()
                                write_file = open("./Text_file/Quiz4.txt",'w')
                                x = -1
                                for question in lines:
                                    question_info = question.split("|")
                                    question_code = question_info[0]
                                    if item_code != question_code:
                                        x = x + 1
                                        Question = "Q0"+str(x+1)+"|"+question_info[1]+"|"+question_info[2]+"|"+question_info[3]+"|"+question_info[4]+"|"+question_info[5]+"|"+question_info[6]
                                        write_file.write(Question)
                                write_file.close()
                                print("\n\n  >>  ITEM HAS BEEN DELETED :)")
                                time.sleep(2)
                                item_found = "Found"
                                Admin_UserPage.deleteQuestion4()
                                break
                            else:
                                item_found = "Not Found"
            
                    if item_found == "Not Found":
                        print("-->  CODE NOT FOUND! PLEASE CHECK THE CODE CORRECTLY", end = "\r")
                        time.sleep(1)
                        Admin_UserPage.deleteQuestion4()
                        break
                    else:
                        continue
        
    # NUR ADIBAH BINTI KHAIRUL ANUAR
    def Lecturer_ReviewPAge():
        os.system("cls")
        welcome_text = " COMMENT SECTION "
        print("\n" + welcome_text.center(70, "-") + "\n")
        data_file = open("./Text_file/Review.txt", "r")
        lines = data_file.readlines()
        data_file.close()
        print("-" * 71)
        print(f"""|  CODE  |                    COMMENT                        |  NAME  |""")
        print("-" * 71)
        for line in lines:
            Review_info = line.split("| ")
            Review_topic = Review_info[1]
            Review_name = Review_info[2][:-1]
            if "A" in Review_info[0]:
                print("|" + Review_info[0].center(8) + "| " + Review_topic.ljust(50) + "|" + Review_name.center(8) + "|")
        print("-" * 71)
        to_back = input("\n\n-->  PRESS [ENTER] TO GO BACK TO LECTURER PAGE\n")
        Admin_UserPage.LecturerPage()

Home_Page.welcome()