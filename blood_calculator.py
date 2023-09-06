def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    choice = input("Enter your choice: ")
    if choice=='9':
        return
        
def HDL_input():
    HDL_value = input("Enter the HDL Value: ")
    HDL_value = int(HDL_value)
    return HDL_value
    
def HDL_analysis(HDL):
    if HDL >= 60:
        return "Normal"
    elif 40 <= HDl <= 60:
        return "Borderline Low"
    else:
        return "Low"
        
def HDL_output(HDL_value, HDL_result):
    print("The HDL value of {} is {}.".format(HDL_value, HDL_result))
    
def HDL_driver():
    value = HDL_input():
    result = HDL_analysis(value)
    HDL_output(value, result)

interface()