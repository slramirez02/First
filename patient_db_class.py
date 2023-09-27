class Patient:

    def __init__(self):
        '''
        initialization func in python has this special name
        self.variable refers to variables that will be local to class instance itself
        '''
        self.first_name = ""    
        self.last_name = ""
        self.mrn = None
        self.age = None
        self.tests = []
        z = "hello"
    
    def print(self):
        out_string = "Name: {}".format(self.full_name())
        out_string += " Age: {}".format(self.age)
        return out_string
    
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)