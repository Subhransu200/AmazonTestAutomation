import pytest
from utils.driver_factory import DriverFactory
import time

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = DriverFactory.get_driver()
        yield
        self.driver.quit()

    def test_amazon(self):
        url = "https://www.amazon.com"
        self.driver.get(url)
        time.sleep(2)
        assert "Amazon" in self.driver.title 