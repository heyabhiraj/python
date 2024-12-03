#Parent class (cuboid)
class cuboid:
    #Initializing the dimensions of the cuboid
    def __init__(self,length,breadth,height):
        self.length=length #attribute for cuboid length
        self.breadth=breadth #attribute for cuboid breadth
        self.height=height #attribute for cuboid height
        
    #Method to calculate the volume of the cuboid
    def volume(self):
        return self.length*self.breadth*self.height

    #Method to calculate the surface area of the cuboid
    def surface_area(self):
        return 2*(self.length*self.breadth + self.breadth*self.height + self.height*self.length)

#child class (rectangle) inherited from cuboid
class rectangle(cuboid):
    #Initializing the dimensions of the rectangle
    def __init__(self,length,breadth):
        #calling the Parent class (cuboid) constructor
        super().__init__(length,breadth,0) #Height is 0 for rectangle

    #Method to calculate the area of the rectangle
    def area(self):
        return self.length*self.breadth

    #Method th calculate the perimeter of the rectangle
    def perimeter(self):
        return 2*(self.length + self.breadth)

#Taking user input for the dimensions of the rectangle
l=float(input("Enter the Length of the Rectangle in cm: "))
b=float(input("Enter the Breadth of the Rectangle in cm: "))

#creating object of the child class rectangle
rec=rectangle(l,b)

#accessing attributes and methods
print(f"\nLength and Breadth of the Rectangle as entered by the user are {rec.length} cm and {rec.breadth} cm respectively.\n")
print(f"Area of the Rectangle is {rec.area()} cm\N{superscript two}\nPerimeter of the Rectangle is {rec.perimeter()} cm")





