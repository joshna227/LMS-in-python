class RegisterOrLogin:
    data = {'6722': ["asma", "sma", "ma"], '6764': ["krishna", "shna", "hna"]}

    def login(self, data):
        self.data = data
        print("\nLOGIN FORM")
        roll = input("\nEnter UserID or RollNumber:")
        password = input("Enter password:")
        if roll in data:
            info = data[roll]
            if password == info[-1]:
                print("\nYou Have Logged in Successfully\n")
            else:
                print("\nEnter Correct Password")
                self.login(data)
        else:
            print("\nUserID id invalid")
            print("Options:\n1.go to login page\n2.Do not have an account, register")
            option = int(input("Enter the option number:"))
            if option == 1:
                self.login(data)
            elif option == 2:
                self.register(data)

    def register(self, data):
        self.data = data
        print("\nREGISTRATION FORM")
        name = input("\nEnter Name:")
        roll = input("Enter Roll Number:")
        email = input("Enter Mail ID:")
        password = input("Enter password:")

        if roll not in data:
            data_details = [name, email, password]
            data[roll] = data_details

            print("\nYou are Registered Successfully, please login")
            self.login(data)
        else:
            print("\nUsername already exists, please login")
            self.login(data)

    def in_login_page(self, info):
        print("\nOptions:\n1. To view Details\n2. To update details\n3. To logout\n4. To get out of the website")
        options = int(input("Enter option number:"))
        if options == 1:
            self.view_details(info)
        if options == 2:
            self.update(info)
        if options == 3:
            print("Logged Out")
            self.login(self.data)
        if options == 4:
            print("Thankyou for visiting our Website")

    def view_details(self, info):
        print("\nName:", info[0], "\nRoll Number:", info[1], "\nemail:", info[2])
        self.in_login_page(info)

    def update(self, info):
        while True:
            print("\nSelect the option to be updated/changed:\n1. Name\n2. Email\n3. Password\n4. No Updatation")
            option = int(input("Enter the option number:"))
            if option == 1:
                new_name = input("Enter Name to be updated:")
                info[0] = new_name
                print("Name is updated Successfully.")
            if option == 2:
                new_email = input("Enter Email to be updated:")
                info[2] = new_email
                print("Email is updated Successfully.")
            if option == 3:
                prev_pass = input("Enter Original Password:")
                while prev_pass != info[-1]:
                    print("Password do not match")
                    prev_pass = input("Enter Original Password:")
                else:
                    new_pass = input("Enter New Password:")
                    info[-1] = new_pass
                    print("Password is updated Successfully.")
            if option == 4:
                break
        self.in_login_page(info)


ob = RegisterOrLogin()
ob.register(ob.data)
