import sys

from models.admin import Admin
from models.course import Course
from models.mentor import Mentor
from models.payment import CardPayment, NetBankingPayment, UPIPayment
from models.student import Student
from services.enrollment_service import EnrollmentService
from services.payment_service import PaymentService


if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def main():
    print("=" * 60)
    print("ONLINE LEARNING PLATFORM")
    print("=" * 60)

    student = Student(1, "Rahul", "rahul@example.com")
    mentor = Mentor(2, "Anita", "anita@example.com", "Python")
    admin = Admin(3, "Admin User", "admin@example.com")

    print("\n--- USERS ---")
    student.display_info()
    mentor.display_info()
    admin.display_info()

    print("\n--- LOGIN ---")
    student.login()
    mentor.login()
    admin.login()

    print("\n--- COURSE CREATION ---")
    course = Course(
        101,
        "Python OOP",
        "Learn Object-Oriented Programming with Python",
        mentor,
    )
    mentor.create_course(course)

    print("\n--- ENROLLMENT ---")
    EnrollmentService.enroll(student, course)

    print("\n--- COURSE DETAILS ---")
    course.show_course()
    EnrollmentService.show_enrollment(student)

    print("\n--- ADMIN ---")
    admin.manage_course(course)
    admin.manage_user(student)

    print("\n--- PAYMENT POLYMORPHISM ---")
    payments = [
        UPIPayment(1500),
        CardPayment(2000),
        NetBankingPayment(2500),
    ]
    for payment in payments:
        PaymentService.process_payment(payment)

    print("\n--- LOGOUT ---")
    student.logout()
    mentor.logout()
    admin.logout()


if __name__ == "__main__":
    main()