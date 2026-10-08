from models.user import User


class Mentor(User):
    def __init__(self, user_id, name, email, expertise):
        super().__init__(user_id, name, email)
        self.expertise = expertise
        self.courses = []

    def get_role(self):
        return "Mentor"

    def create_course(self, course):
        self.courses.append(course)
        print(f"{self.name} created course: {course.title}")

    def show_courses(self):
        print(f"\nCourses created by {self.name}:")

        if not self.courses:
            print("No courses created.")
            return

        for course in self.courses:
            print(f"- {course.title}")