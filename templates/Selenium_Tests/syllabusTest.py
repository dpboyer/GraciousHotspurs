from selenium import webdriver
from selenium.webdriver.common.by import By

# from CS351_Project.models import Instructor, Course, Section, TA
import unittest


class SyllabusDisplayTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title_in_syllabus(self):
        self.browser.get('http://127.0.0.1:8000/syllabus/111/33')
        self.assertIn('Syllabus', self.browser.title)
        instructor_name = self.browser.find_element_by_id("instructor_name")
        self.assertIn('Jayson', instructor_name.value)


if __name__ == '__main__':
    unittest.main()
