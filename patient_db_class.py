class Patient:

    def __init__(self, fn, ln, mrn, age):
        '''
        initialization func in python has this special name
        self.variable refers to variables that will be local to class instance itself
        '''
        self.first_name = fn    
        self.last_name = ln
        self.mrn = mrn
        self.age = age
        self.tests = []
        self.z = "hello"
    
    def print(self):
        out_string = "Name: {}".format(self.full_name())
        out_string += " Age: {}".format(self.age)
        return out_string
    
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def change_age(new_age):
        self.age = new_age
        return None