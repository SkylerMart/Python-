#Python Course
# Purpose:Creating my first program in python. Demonstrating how
# to pass variables from function to function while producing a
# functional game.
#
# Remember, function_name(variable) _means that we pass in 
# the variable. return variable _means we are returning the
# variable to back to the calling function.

def start():
    fname = "Sarah"
    lname = "Connor"
    age = 28
    gender = "Female"
    get_info(fname,lname, age, gender)


def get_info(fname, lname, age, gender):
    print("My name is {} {}. I am {} yearold {}.".format(fname,lname,age,gender))






if __name__=="__main__":
    start()
