from selenium.webdriver.chrome.options import Options


def pytest_setup_options():
    """Configure headless Chrome for Dash testing."""
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options
