class Person():
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self. email = email
        
    def get_info(self):
        return f'Name: {self. name}, Age: {self.age}, Email: {self.email}'
    
        
class Student(Person):
    
    def __init__(self, name, age, email, student_id, enrolled_courses=None, grades=None):
        super().__init__(name, age, email)    
        self.student_id = student_id
        self.enrolled_courses = enrolled_courses if enrolled_courses is not None else []
        self.grades = grades if grades is not None else {}
        
    def enroll_course(self, course):
        self.enrolled_courses.append(course. course_name)  
    
    def add_grade(self, course_code, grade):
        self.grades[course_code] = grade
        
    def get_gpa(self):
        gpa_dct = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
        
        if len(self.grades) == 0:
            return 0.0  
        
        total = 0
        for grade in self.grades.values():
            total += gpa_dct.get(grade, 0) 
        return total / len(self.grades)
    
    def get_enrolled_courses(self):
        return self.enrolled_courses  
    
    
class Teacher(Person):
    def __init__(self, name, age, email, employee_id, subject, salary):
        super().__init__(name, age, email)
        self.employee_id = employee_id
        self.subject = subject
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary 
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            return f'Salary updated to ₹{new_salary}'   
        return "Please update correct salary"
    
    def teach(self, course_name):
        return f'Prof. {self.name} is teaching {course_name}'
    

class Course():
    
    def __init__(self, course_name, course_code, teacher, max_students, enrolled_students=None):
        self.course_name = course_name
        self. course_code = course_code
        self.teacher = teacher
        self.enrolled_students = enrolled_students if enrolled_students is not None else []
        self.max_students = max_students
        
    def add_student(self, student):
        if len(self. enrolled_students) < self.max_students:
            self.enrolled_students.append(student)
            return f'{student. name} is enrolled in {self. course_name}' 
        return "The capacity of enrolled students is full"
    
    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            return f'The student {student.name} is removed'  
        return "Student not found in this course"
        
    def get_student_count(self):
        return len(self.enrolled_students)  
    
    def get_course_info(self):
        return f'Course: {self.course_name} ({self.course_code})\nTeacher: {self.teacher. name}\nEnrolled: {self.get_student_count()}/{self.max_students}'
        
        
class School():
    
    def __init__(self, school_name, students=None, teachers=None, courses=None):
        self.school_name = school_name  
        self.students = students if students is not None else []
        self.teachers = teachers if teachers is not None else []
        self. courses = courses if courses is not None else []
       
    def add_student(self, student):
        self.students.append(student)
        return f'{student.name} added'
           
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        return f'{teacher.name} added'
        
    def add_course(self, course):
        self.courses.append(course)
        return f'{course. course_name} added'
    
    def find_student_by_id(self, student_id):
        for student in self. students:
            if student.student_id == student_id:
                return student  
        return None
    
    def find_teacher_by_id(self, employee_id):
        for teacher in self.teachers:
            if teacher.employee_id == employee_id:
                return teacher 
        return None
    
    def get_all_students(self):
        return [student.name for student in self. students]  
    
    def get_all_courses(self):
        return [course.course_name for course in self.courses]  
            
    def get_school_stats(self):
        return f'Total Students: {len(self. students)}\nTotal Teachers: {len(self.teachers)}\nTotal Courses: {len(self.courses)}'


# ==================== DEMO / TESTING ====================

if __name__ == "__main__":
    
    print("=" * 60)
    print("STUDENT MANAGEMENT SYSTEM - DEMO")
    print("=" * 60)
    
    # Create school
    school = School("Python High School")
    print(f"\n✅ Created school: {school.school_name}\n")
    
    # Create teachers
    teacher1 = Teacher("Dr. Smith", 45, "smith@school.com", "T001", "Mathematics", 60000)
    teacher2 = Teacher("Prof.  Johnson", 38, "johnson@school.com", "T002", "Physics", 55000)
    teacher3 = Teacher("Dr. Williams", 42, "williams@school.com", "T003", "Chemistry", 58000)
    
    school.add_teacher(teacher1)
    school.add_teacher(teacher2)
    school.add_teacher(teacher3)
    print("✅ Added 3 teachers to school")
    
    # Create courses
    math_course = Course("Calculus", "MATH101", teacher1, max_students=30)
    physics_course = Course("Quantum Physics", "PHYS201", teacher2, max_students=25)
    chem_course = Course("Organic Chemistry", "CHEM101", teacher3, max_students=20)
    
    school.add_course(math_course)
    school.add_course(physics_course)
    school.add_course(chem_course)
    print("✅ Added 3 courses to school\n")
    
    # Create students
    student1 = Student("Shreyas", 20, "shreyas@email.com", "S001")
    student2 = Student("Priya", 21, "priya@email.com", "S002")
    student3 = Student("Rahul", 19, "rahul@email.com", "S003")
    student4 = Student("Ananya", 20, "ananya@email.com", "S004")
    
    school.add_student(student1)
    school.add_student(student2)
    school.add_student(student3)
    school.add_student(student4)
    print("✅ Added 4 students to school\n")
    
    # Enroll students in courses
    print("--- ENROLLING STUDENTS ---")
    print(math_course.add_student(student1))
    student1.enroll_course(math_course)
    
    print(math_course.add_student(student2))
    student2.enroll_course(math_course)
    
    print(physics_course.add_student(student1))
    student1.enroll_course(physics_course)
    
    print(physics_course.add_student(student3))
    student3.enroll_course(physics_course)
    
    print(chem_course.add_student(student2))
    student2.enroll_course(chem_course)
    
    print(chem_course.add_student(student4))
    student4.enroll_course(chem_course)
    
    # Add grades
    print("\n--- ASSIGNING GRADES ---")
    student1.add_grade("MATH101", "A")
    student1.add_grade("PHYS201", "B")
    print(f"✅ {student1.name}: MATH101=A, PHYS201=B")
    
    student2. add_grade("MATH101", "B")
    student2.add_grade("CHEM101", "A")
    print(f"✅ {student2.name}: MATH101=B, CHEM101=A")
    
    student3.add_grade("PHYS201", "C")
    print(f"✅ {student3.name}: PHYS201=C")
    
    student4.add_grade("CHEM101", "A")
    print(f"✅ {student4.name}: CHEM101=A")
    
    # Display school statistics
    print("\n" + "=" * 60)
    print("SCHOOL STATISTICS")
    print("=" * 60)
    print(school.get_school_stats())
    
    print("\nAll Students:", ", ".join(school.get_all_students()))
    print("All Courses:", ", ".join(school.get_all_courses()))
    
    # Display student details
    print("\n" + "=" * 60)
    print("STUDENT PROFILES")
    print("=" * 60)
    
    print(f"\n📚 {student1.name}")
    print(student1.get_info())
    print(f"Student ID: {student1.student_id}")
    print(f"Enrolled Courses: {', '.join(student1.get_enrolled_courses())}")
    print(f"Grades: {student1.grades}")
    print(f"GPA: {student1.get_gpa()}")
    
    print(f"\n📚 {student2.name}")
    print(student2.get_info())
    print(f"Student ID: {student2.student_id}")
    print(f"Enrolled Courses: {', '.join(student2.get_enrolled_courses())}")
    print(f"Grades: {student2. grades}")
    print(f"GPA: {student2.get_gpa()}")
    
    # Display course info
    print("\n" + "=" * 60)
    print("COURSE INFORMATION")
    print("=" * 60)
    
    print(f"\n📖 {math_course.course_name}")
    print(math_course.get_course_info())
    print(f"Enrolled students: {[s.name for s in math_course.enrolled_students]}")
    
    print(f"\n📖 {physics_course.course_name}")
    print(physics_course.get_course_info())
    print(f"Enrolled students: {[s.name for s in physics_course.enrolled_students]}")
    
    # Display teacher info
    print("\n" + "=" * 60)
    print("TEACHER INFORMATION")
    print("=" * 60)
    
    print(f"\n👨‍🏫 {teacher1.name}")
    print(teacher1.get_info())
    print(f"Employee ID: {teacher1.employee_id}")
    print(f"Subject: {teacher1.subject}")
    print(f"Salary: ₹{teacher1. get_salary()}")
    print(teacher1.teach(math_course.course_name))
    
    # Test salary update
    print(f"\n💰 Testing salary update for {teacher1.name}:")
    print(teacher1.set_salary(65000))
    print(f"New salary: ₹{teacher1.get_salary()}")
    
    print(teacher1.set_salary(-1000))  # Should fail
    
    # Test search functionality
    print("\n" + "=" * 60)
    print("SEARCH TESTS")
    print("=" * 60)
    
    found = school.find_student_by_id("S001")
    if found:
        print(f"✅ Found student S001: {found.name}")
    
    found = school.find_teacher_by_id("T002")
    if found:
        print(f"✅ Found teacher T002: {found.name} - {found.subject}")
    
    # Test remove student
    print("\n" + "=" * 60)
    print("REMOVE STUDENT TEST")
    print("=" * 60)
    
    print(f"\nBefore removal: {math_course.get_student_count()} students in {math_course.course_name}")
    print(math_course.remove_student(student1))
    print(f"After removal: {math_course. get_student_count()} students in {math_course.course_name}")
    
    # Test capacity limit
    print("\n" + "=" * 60)
    print("COURSE CAPACITY TEST")
    print("=" * 60)
    
    small_course = Course("Python Basics", "CS101", teacher1, max_students=2)
    print(small_course.add_student(student1))
    print(small_course.add_student(student2))
    print(small_course.add_student(student3))  # Should fail
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETE!")

    print("=" * 60)
