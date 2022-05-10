import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods

class WegostudyAppPostiveTestCases(unittest.TestCase):

    @staticmethod
    def test_main_wegostudy():
        methods.setUp()
        methods.log_in()
        methods.create_new_student()
        methods.log_out()
        methods.tearDown()
