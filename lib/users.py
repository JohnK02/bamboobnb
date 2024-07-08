class Users:

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email})"
    
    def is_valid(self):
        if self.username == None or self.username == "":
            return False
        if self.email == None or self.email == "":
            return False
        if self.password == None or self.password == "":
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.username == None or self.username == "":
            errors.append("Username can't be blank")
        if self.email == None or self.email == "":
            errors.append("Email can't be blank")
        if self.password == None or self.password == "":
            errors.append("Password can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)