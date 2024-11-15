#main.py

from views.account_ui import AccountUI
from views.user_ui import UserUI

if __name__ == "__main__":
    user_ui = UserUI()
    user_ui.start()
