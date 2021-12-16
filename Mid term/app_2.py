import math


def main():
    print("\nArea and Perimeter of a Rectangle\n")
    
    base = float(input("Insert base:"))
    height = float(input("Insert height:"))
    t = Rectangle(base, height)
    print(t)
   
	
class Rectangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def getArea(self):
        return(self.base*self.height)
    
    def getPerimeter(self):
        return(2*(self.base+ self.height))

    def print(self):
        print("\nArea: ", f'{self.getArea():.2f}')
        print("Perimeter: ", f'{self.getPerimeter():.2f}','\n')

    def __str__(self):
        return("\nArea: "+f'{self.getArea():.2f}'+
        "\nPerimeter: "+f'{self.getPerimeter():.2f}'+'\n')

	
	
# Entry point
if __name__ == '__main__':
	main()
