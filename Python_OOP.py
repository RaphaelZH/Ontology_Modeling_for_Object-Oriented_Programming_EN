class Class:

    def __init__(self, students):
        self.students = students

class Person:

    def __init__(self, details):
        self.details = details

class School:

    def __init__(self, address, postCodesAccepted, students):
        self.address = address
        self.postCodesAccepted = postCodesAccepted
        self.students = students


class Employee(Person):

    def __init__(self, salary):
        super().__init__()
        self.salary = salary

class Student(Person):

    def __init__(self, grade):
        super().__init__()
        self.grade = grade

class Teacher(Employee):

    def __init__(self, teaches):
        super().__init__()
        self.teaches = teaches


Transfiguration = Class()
Minerva_McGonagall = Employee(details="Minerva McGonagall is a major character in the Harry Potter franchise. She is the Transfiguration teacher at Hogwarts School of Witchcraft and Wizardry during the events of Harry Potter series. She is the only daughter of Robert McGonagall senior and. McGonagall acts as a stern but caring grandmotherly figure for her students, especially Harry Potter, Ron Weasley and Hermione Granger. She is also loyal to Albus Dumbledore, who she considers one of her closest friends. After the War, she became the Headmistress of the school.", salary=20000.0, )
Rubeus_Hagrid = Employee(details="Rubeus Hagrid is one of the major characters of Harry Potter by JK Rowling. During his sixth year at Hogwarts, Hagrid was expelled from school. However, as an adult, he stayed on as the gameskeeper. Throughout the book series, he supports Harry and becomes one of his many father figures and was one of his first friends and the one to tell Harry of his wizardry heritage.", salary=5000.0, )
Dobby = Person(details="Dobby is one of the supporting characters in Harry Potter. He was a male house-elf who served the Malfoy family. His masters were Dark Wizards who treated him cruelly - Until he was saved by Harry Potter. He served the young wizard and worked in the kitchens of Hogwarts.", )
Harry_Potter = Person(details="Auror Harry James Potter (b. 31 July 1980) was an English half-blood wizard, and one of the most famous wizards of modern times. The only child and son of James and Lily Potter (née Evans), Harry's birth was overshadowed by a prophecy, naming either himself or Neville Longbottom as the one with the power to vanquish his arch-enemy, Lord Voldemort, the most powerful and feared Dark wizard in the world. After half of the prophecy was reported to Voldemort, courtesy of Severus Snape, Harry was chosen as the target due to his many similarities with the Dark Lord. This in turn caused the Potter family to go into hiding.", grade=96.7, )
Minerva_McGonagall = Person(details="Minerva McGonagall is a major character in the Harry Potter franchise. She is the Transfiguration teacher at Hogwarts School of Witchcraft and Wizardry during the events of Harry Potter series. She is the only daughter of Robert McGonagall senior and. McGonagall acts as a stern but caring grandmotherly figure for her students, especially Harry Potter, Ron Weasley and Hermione Granger. She is also loyal to Albus Dumbledore, who she considers one of her closest friends. After the War, she became the Headmistress of the school.", salary=20000.0, )
Rubeus_Hagrid = Person(details="Rubeus Hagrid is one of the major characters of Harry Potter by JK Rowling. During his sixth year at Hogwarts, Hagrid was expelled from school. However, as an adult, he stayed on as the gameskeeper. Throughout the book series, he supports Harry and becomes one of his many father figures and was one of his first friends and the one to tell Harry of his wizardry heritage.", salary=5000.0, )
Hogwarts = School(postCodesAccepted="Unknown", address="Scottish Highlands", )
Harry_Potter = Student(details="Auror Harry James Potter (b. 31 July 1980) was an English half-blood wizard, and one of the most famous wizards of modern times. The only child and son of James and Lily Potter (née Evans), Harry's birth was overshadowed by a prophecy, naming either himself or Neville Longbottom as the one with the power to vanquish his arch-enemy, Lord Voldemort, the most powerful and feared Dark wizard in the world. After half of the prophecy was reported to Voldemort, courtesy of Severus Snape, Harry was chosen as the target due to his many similarities with the Dark Lord. This in turn caused the Potter family to go into hiding.", grade=96.7, )
Minerva_McGonagall = Teacher(details="Minerva McGonagall is a major character in the Harry Potter franchise. She is the Transfiguration teacher at Hogwarts School of Witchcraft and Wizardry during the events of Harry Potter series. She is the only daughter of Robert McGonagall senior and. McGonagall acts as a stern but caring grandmotherly figure for her students, especially Harry Potter, Ron Weasley and Hermione Granger. She is also loyal to Albus Dumbledore, who she considers one of her closest friends. After the War, she became the Headmistress of the school.", salary=20000.0, )
