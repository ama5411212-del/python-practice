import getpass #لعدم رؤية كلمة المرور عند كتابتها
import os #للتأكد من وجود ملف البيانات  
data_file = 'user_data.txt'# ملف لتخزين بيانات المستخدمين
if not os.path.exists(data_file):
        print('first time stup! Please enter your personal information to create an account: ')
        prenom_saved = input('Enter your first name: ')
        nom_saved = input('Enter your last name: ')
        age_saved = input('Enter your age: ')
        email_saved = input('Enter your email: ')
        username_saved = input('Create a username: ')
        password_saved = input('Create a password: ')
        with open(data_file, 'w') as f:
            f.write(f"{username_saved}\n{password_saved}\n{prenom_saved}\n{nom_saved}\n{age_saved}\n{email_saved}\n")
            print("Account created successfully! Please restart the program to log in.")
else:
    with open(data_file, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        correct_username = lines [0]
        correct_password = lines [1]
        print("Welcome back! Please log in to continue.")
        input_prenom = input ("Enter your first name: ")#pour verifier le nom et le prénom de l'utilisateur
        input_nom = input ("Enter your last name: ")
        input_username = input("Enter your username: ")
        input_password = getpass.getpass("Enter your password: ")
        if ( input_username == correct_username and input_password == correct_password and input_prenom == lines[2] and input_nom == lines[3]):
            print("Login successful! Welcome back!")#للمطابقة بين اسم المستخدم وكلمة المرور المدخلة مع البيانات المخزنة في الملف
        else:
                print("Invalid credentials. Please try again.") 
    print("Welcome to the login system!")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("-"*40)
        print("Login successful!")
        name =  "ahmed"
        age = int(input("Enter your age: "))
        if age < 15:
            print("We regret to inform you that you cannot proceed to the next stage because your recent data does not comply with the requirements.")
    else:
            print("Welcome! Let's continue!")
            maths   = float(input("Enter your maths note: "))
            physics = float(input("Enter your physics note: "))
            svt = float(input("Enter your svt note: "))
            math_coef = float(input("Enter your maths coefficient: "))
            physics_coef = float(input("Enter your physics coefficient: "))
            svt_coef = float(input("Enter your svt coefficient: "))
            total_points = ( maths * math_coef) + (physics * physics_coef) + (svt * svt_coef)
            average = total_points / (math_coef + physics_coef + svt_coef)
            print("-"*40)
            NAME = input("Enter your name: ")
            prénom = input("Enter your first name: ")
            print(f"Age: {age}")
            print(f"Total Points: {total_points}")
            print(f"Average: {average:.2f}")
            print(f"SVT: {svt}")
            print(f"Maths Coefficient: {math_coef}")
            print(f"Physics Coefficient: {physics_coef}")
            print(f"SVT Coefficient: {svt_coef}")
            if average >= 10:
                    print("Congratulations! You have passed the exam.")
            else:
                    print("Unfortunately, you have failed the exam. Better luck next time!")
                    print("-"*40)
                    z

