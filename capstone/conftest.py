from datetime import datetime
import pytest
@pytest.fixture(scope="function",autouse=True)
def setup():
    print(datetime.today().strftime("%y-%m-%d %H:%M:%S"))