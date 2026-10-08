from models.user import User


class Admin(User):
    def get_role(self):
        return "Admin"

    def manage_course(self, course):
        print(f"Admin {self.name} is managing course: {course.title}")

    def manage_user(self, user):
        print(f"Admin {self.name} is managing user: {user.name}")