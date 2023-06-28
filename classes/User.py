import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()


class User:
    def __init__(self, userID, username, password):
        self.userID = userID
        self.username = username
        self.password = password
        self.hashedPassword = ""
        self.salt = str(os.getenv('SALT'))

    def hashPassword(self):
        pswrd = self.password.encode('utf-8')
        self.hashedPassword = bcrypt.hashpw(  # is not working due to issues with Python's inbuilt encode :(
            pswrd, self.salt)

    def verifyPassword(self, candidatePassword):
        candidateBytes = candidatePassword.encode('utf8')
        # is not working due to issues with Python's inbuilt encode :(
        return bcrypt.checkpw(candidatePassword, self.hashedPassword)

    def getSQLInsertionTuple(self):
        return (self.userID, self.username, self.hashedPassword)
