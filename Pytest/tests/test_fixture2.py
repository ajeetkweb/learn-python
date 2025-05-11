"""Pytest with Class-Based Setup and Teardown"""


import pytest

class TestExample:
    
    @classmethod
    def setup_class(cls):
        """ Runs once before all tests in this class """
        print("\n[SETUP] Initializing resources")
        cls.shared_data = {"message": "Hello, Pytest!"}

    @classmethod
    def teardown_class(cls):
        """ Runs once after all tests in this class """
        print("\n[TEARDOWN] Cleaning up resources")
        del cls.shared_data

    def test_1(self):
        assert self.shared_data["message"] == "Hello, Pytest!"

    def test_2(self):
        assert isinstance(self.shared_data, dict)
