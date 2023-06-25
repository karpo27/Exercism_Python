class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        if students is not None:
            self.students = students
        else:
            self.students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
        self.students.sort()
        
        row_division = self.diagram.index("\n")
        self.row_1 = self.diagram[:row_division + 1]
        self.row_2 = self.diagram[row_division + 1:]
        
    def plants(self, student):
        plants_types = {
            "C": "Clover",
            "G": "Grass",
            "R": "Radishes",
            "V": "Violets"
        }
        index = self.students.index(student)
        index = index * 2
        student_plants = []
        for plant in self.row_1[index:index + 2] + self.row_2[index:index + 2]:
            student_plants.append(plants_types[plant])
        
        return student_plants
