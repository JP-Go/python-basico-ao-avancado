from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from time import sleep


class FirefoxAuto:
    def __init__(self, driver_path: str = "./geckodriver") -> None:
        self.driver_path = driver_path
        self.service = FirefoxService(executable_path=self.driver_path)
        self.options = FirefoxOptions()
        self.firefox = Firefox(service=self.service, options=self.options)

    def test(self, url: str) -> None:
        self.firefox.get(url)


def main():
    firefox = FirefoxAuto()
    firefox.test("https://www.google.com")


if __name__ == "__main__":
    main()
