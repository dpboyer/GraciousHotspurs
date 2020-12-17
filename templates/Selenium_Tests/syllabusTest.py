# from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.by import By
# from CS351_Project.models import Instructor,TA, Section, Course

# from django.contrib.auth.models import User




# from CS351_Project.models import Instructor, Course, Section, TA
import unittest


class SyllabusDisplayTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def test_title_in_syllabus(self):
        self.browser.get('http://127.0.0.1:8000/syllabus/123/1')
        self.assertIn('Syllabus', self.browser.title)
        instructor_phone = self.browser.find_element_by_id("i_phone")
        self.assertIn('12345', instructor_phone.get_attribute('text'))


if __name__ == '__main__':
    unittest.main()



'''
        #  build instructor
        instUser = User(username="TestInstructor", password="weak", first_name="fname", last_name="lname", email="eml")
        instUser.save()
        self.newInstructor = Instructor(user=instUser)
        self.newInstructor.save()
        # build TA
        TaUser = User(username='TestTa', password="weak", first_name='fnameTA', last_name='lnameTA', email='e')
        TaUser.save()
        self.newTa = TA(user=TaUser)
        self.newTa.save()
        # build course
'''

# self.newTa.delete()
# self.newInstructor.delete()