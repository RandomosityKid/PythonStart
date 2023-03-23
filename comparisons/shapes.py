#Java uses camelCasing, Python uses snake_case naming style
def peri(width, height):
    return 2 * width + 2 * height

def area(width, height):
    return width * height

def calc_all(width, height):
    local_perm = peri(width, height)
    local_area = area(width, height)
    
    print("Perimeter: ", local_perm)
    print("Area: ", local_area)

# The following code is used to ensure that the code inside the if statement is only executed
# if the script is run directly (not imported as a module by another script)
# Same as public static void main(String arge[])
if __name__ == '__main__':
    while True:
        rect_width = int(input("Enter rectangle width: "))
        rect_height = int(input("Enter rectangle height: "))
        
        choice = input("Enter calculation: (Perimeter/Area): ")
        if choice.lower() == "perimeter":
            #print("Perimeter: " + str(peri(width, height))), but comma more valid
            print("Perimeter: ", peri(rect_width, rect_height))
        elif choice.lower() == "area":
            print("Area: ", area(rect_width, rect_height))
        
        display_both = input("Display both? [y/n]: ")
        if display_both.lower() == "y":
            calc_all(rect_width, rect_height)
            
        print("Done.\n")