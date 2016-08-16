from django.test import TestCase
from django.contrib.auth.models import User
from member.models import Member, Staff, Student


class MemberTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.member_student = Member.objects.create(
            firstname="Club",
            lastname="Cedille",
        )

        cls.member_staff = Member.objects.create(
            firstname="Club",
            lastname="Club",
        )

        cls.staff = Staff.objects.create(
            member=cls.member_staff
        )

        cls.student = Student.objects.create(
            member=cls.member_student
        )

    def testFirstNameStudent(self):

        student = self.student

        self.assertEqual(student.member.firstname, "Club")

    def testLastNameStudent(self):

        student = self.student

        self.assertEqual(student.member.lastname, "Cedille")

    def testFirstNameStaff(self):
        staff = self.staff
        self.assertEqual(staff.member.firstname, "Club")

    def testLastNameStaff(self):
        staff = self.staff
        self.assertEqual(staff.member.lastname, "Club")
