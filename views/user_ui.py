from services.User_manger import UserManager
from repositories.User_repositary import UserRepository
from models.Users import User
from views.account_ui import AccountUI
class UserUI:
    def start(self):
        while True:
            print("\nWelcome to Global Digital Bank")
            print("\nSelect an option")
            print("1.create user")
            print("2.login user")
            print("3.edit user")
            print("4.view user")
            print("5.Activate user")
            print("6.Deactivate user")
            print("7.view users")
            print("8.exit")
            choice= int(input("enter your choice: "))
            if choice == 1:
                self.create_user()
            elif choice==2:
                self.login()
            elif choice==3:
                self.edit_user()
            elif choice==4:
                self.view_user()
            
            elif choice==5:
                self.activate_user()
            elif choice==6:
                self.inactivate_user()
            elif choice==7:
                self.view_users()
            elif choice==8:
                break
            else:
                print("invalid input try again")
    def create_user(self):
        name=input("enter the username: ")
        login_id=input("enter the login id: ")
        password=input("enter the password: ")
        user = User(name,login_id,password)
        UserManager.add_user(user)
        print(f"the user id is {user.User_id}")
    def edit_user(self):
        user_id=int(input("enter the user id to be edited: "))
        user =next((user for user in UserRepository.Users if user.User_id==user_id),None)
        if user:
            try:
                password=input("enter the password: ")
                if user.password==password:
                    username=input("enter the new name: ")
                    new_password=input("enter the new password: ")
                    UserManager.edit_user(username,new_password,user)
                else:
                    print("Invalid password")
            except Exception as e:
                print(e)
        else:
            print("user not found")
    def view_user(self):
        user_id=int(input("Enter the user id: "))
        UserManager.view_user_details(user_id)
    def login(self):
        user_id=int(input("Enter the user id: "))
        user =next((user for user in UserRepository.Users if user.User_id==user_id),None)
        if user:
            if user.isActive:
                try:
                    password=input("enter the password: ")
                    if user.password==password:
                        accountUI=AccountUI()
                        accountUI.start(user)
                    else:
                        print("invalid password")
                except Exception as e:
                    print(e)
            else:
                print("Account is deactivated")
        else:
            print("user not found")
    def inactivate_user(self):
        user_id = int(input("Enter the user_id to inactivate: "))
        try:
            user_manager = UserManager()
            user_manager.inactivate_user(user_id)
            print(f"User with ID {user_id} has been inactivated successfully.")
        except Exception as e:
            print(e)


    def activate_user(self):
        user_id = int(input("Enter the user_id to activate: "))
        try:
            user_manager = UserManager()
            user_manager.activate_user(user_id)
            print(f"User with ID {user_id} has been activated successfully.")
        except Exception as e:
            print(f"Error: {e}")
    def view_users(self):
        lenght=len(UserRepository.Users)
        print(f"{lenght} number of users")
        print("-"*43)
        for user in UserRepository.Users:
            print(f"\nusername: {user.username}")
        print('-'*43)
            
        


        