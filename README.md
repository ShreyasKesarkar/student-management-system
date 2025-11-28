# 🎓 Student Management System

A comprehensive Python-based Object-Oriented Programming (OOP) project to manage students, teachers, courses, and school operations.

## 📋 Features

- ✅ Student enrollment and grade tracking
- ✅ GPA calculation system
- ✅ Teacher and salary management
- ✅ Course capacity management
- ✅ Search functionality for students and teachers
- ✅ Input validation and error handling

## 🛠️ Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
  - Inheritance
  - Encapsulation
  - Data Validation

## 🏗️ Classes

### 1. Person (Base Class)
- Attributes: `name`, `age`, `email`
- Methods: `get_info()`

### 2. Student (Inherits from Person)
- Additional: `student_id`, `enrolled_courses`, `grades`
- Methods: `enroll_course()`, `add_grade()`, `get_gpa()`, `get_enrolled_courses()`

### 3. Teacher (Inherits from Person)
- Additional: `employee_id`, `subject`, `__salary` (private)
- Methods: `get_salary()`, `set_salary()`, `teach()`

### 4. Course
- Attributes: `course_name`, `course_code`, `teacher`, `enrolled_students`, `max_students`
- Methods: `add_student()`, `remove_student()`, `get_student_count()`, `get_course_info()`

### 5.  School
- Attributes: `school_name`, `students`, `teachers`, `courses`
- Methods: Student/teacher/course management, search functionality, statistics

## 🚀 How to Run

``bash
python StudentManagement1.py


## 💡 Key Concepts Demonstrated
- **Inheritance:** `Student` and `Teacher` classes extend a common `Person` base class
- **Encapsulation:** Private attributes like salary are protected with proper getters/setters
- **Data Validation:** Built-in checks such as course capacity limits and salary validation
- **Composition:** `School` class manages students, teachers, and courses as a structured system

## 🎯 Future Enhancements
- Integrate with a **SQLite database** for persistent data
- Add a **GUI interface** (Tkinter / PyQt)
- Enable **PDF report generation**
- Implement **attendance tracking** and analytics

## 👨‍💻 Author
**Shreyas Kesarkar**

⭐ If you found this project helpful, consider giving it a star!


