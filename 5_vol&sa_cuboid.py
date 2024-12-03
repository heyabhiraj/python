#Defining a class cuboid
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

#Taking user input for the dimensions of the cuboid
l=float(input("Enter the Length of the Cuboid in cm: "))
b=float(input("Enter the Breadth of the Cuboid in cm: "))
h=float(input("Enter the Height of the Cuboid in cm: "))

#creating object of the class cuboid
cub=cuboid(l,b,h)

#accessing attributes and methods
print(f"\nLength, Breadth and Height of the Cuboid as entered by the user are {cub.length} cm, {cub.breadth} cm and {cub.height} cm respectively.\n")
print(f"Volume of the Cuboid is {cub.volume()} cm\N{superscript three}\nSurface Area of the Cuboid is {cub.surface_area()} cm\N{superscript two}")
