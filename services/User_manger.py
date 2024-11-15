from repositories.User_repositary import UserRepository
class UserManager:
    def add_user(user):
        UserRepository.save_user(user)
    def edit_user(new_username,
                  new_password,user):
        user.username=new_username
        user.password=new_password
    def view_user_details(user_id):
        user = next((user for user in UserRepository.Users if user.User_id == user_id), None)
        if user.isActive:
            status="active"
        else:
            status="not active"
        print("-"*40)
        print(f"username: {user.username}") 
        print(f"login id: {user.login_id}")
        print(f"day of creation: {user.created_date}")
        print(f"active status: {status}")
        print("-"*40)
    def activate_user(self, user_id):
        user =next((user for user in UserRepository.Users if user.User_id==user_id),None)
        if user:
            user.isActive = True
        else:
            print("invalid user id")

    def inactivate_user(self, user_id):
        #Inactivates the User
        user =next((user for user in UserRepository.Users if user.User_id==user_id),None)
        if user:
            user.isActive = False
        else:
            print("invalid user id")

    
    

