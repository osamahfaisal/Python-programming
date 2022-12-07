class  Student:
    #  class itrbaute sharing in the class  most be initailization 
    
    no_of_student=0 
    
    def __init__(self , name , age , courses ):  # instance varaible 
        self.name=name
        self.age=age 
        self.course=courses
        Student.no_of_student+=1
        
        