class UserRepository:
    Users=[]
    User_Id=0
    @classmethod
    def generate_user_id(cls):
        cls.User_Id+=1
        return cls.User_Id
    @classmethod
    def save_user(cls,User):
        cls.Users.append(User)
    def get_all_users(self):
        return self.Users

   
