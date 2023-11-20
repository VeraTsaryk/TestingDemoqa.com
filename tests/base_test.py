import pytest


@pytest.mark.usefixtures("initialize_driver")
class BaseTest:
    driver = None

    pass
