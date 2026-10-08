class EnrollmentService:
    @staticmethod
    def enroll(student, course):
        student.enroll_course(course)

    @staticmethod
    def show_enrollment(student):
        student.show_courses()