"""Class-Level Pytest Fixtures (Recommended Approach)
Pytest with Class-Based Setup and Teardown
"""
import pytest

@pytest.fixture(scope="class")
def resource_setup(request):

    print("\n[SETUP] Setting up shared resource")
    request.cls.shared_data = {"message": "Hello, Pytest!"}
    yield

    print("\n[TEARDOWN] Cleaning up shared resource")
    del request.cls.shared_data


@pytest.mark.usefixtures("resource_setup")
class TestExampleFixture:
    
    def test_1(self):
        assert self.shared_data["message"] == "Hello, Pytest!"

    def test_2(self):
        assert isinstance(self.shared_data, dict)
