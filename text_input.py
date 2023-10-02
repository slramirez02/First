in_file = open("fruits.txt", "r")
all_lines = in_file.readlines()

in_file.close()
print(all_lines)

for line in all_lines:
    print(line.strip("\n"))
    
def analyze_line(fruit):
    fruit_stripped = fruit.strip("\n")
    if len(fruit_stripped) >= 6:
        return fruit_stripped
    else:
        return "Short"
    
in_file = open("fruits.txt", "r")
long_fruit = []
for fruit in in_file:
    long_fruit.append(analyze_line(fruit))
    

in_file.close()
print(long_fruit)