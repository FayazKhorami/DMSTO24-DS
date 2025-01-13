# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students):

    """

    Skapar ett register där namn är nycklar och åldrar är värden.

    """

    student_register = {}

    # Gå igenom varje student i listan
    for student in students:

        name = student[0]

        age = student[1]

        # Lägg till namn och ålder i registret

        student_register[name] = age

    return student_register

students = [("Anna", 20), ("Björn", 22), ("Clara", 19)]

print(create_student_register(students))




