def function_name(string, x):
    try:
        return string[x]
    except IndexError:
        print("Index {} is out of bounds in string '{}'. String '{}' has length {}.".format(x, string, string, len(string)))

def main():
    function_name("hello", 6)
    
if __name__ == "__main__":
    main()