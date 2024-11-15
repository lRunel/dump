from repositories.User_repositary import UserRepository
from datetime import date
class User:
    def __init__(self,username,
                login_id,password):
        self.User_id=UserRepository.generate_user_id()
        self.username=username
        self.login_id=login_id
        self.password=password
        self.created_date=date.today()
        self.isActive=True
        self.useraccounts=[]
