class Course:
    def __init__(self, course_id, title, description, mentor):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.mentor = mentor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def show_course(self):
        print(f"\nCourse ID: {self.course_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Mentor: {self.mentor.name}")
        print(f"Number of Students: {len(self.students)}")