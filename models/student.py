from models.user import User


class Student(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.enrolled_courses = []

    def get_role(self):
        return "Student"

    def enroll_course(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)
            print(f"{self.name} enrolled in {course.title}")
        else:
            print(f"{self.name} is already enrolled in {course.title}")

    def show_courses(self):
        print(f"\nCourses of {self.name}:")

        if not self.enrolled_courses:
            print("No courses enrolled.")
            return

        for course in self.enrolled_courses:
            print(f"- {course.title}")