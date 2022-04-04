from pathlib import Path
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.common.by import By
from creds import my_user, my_pass
from time import sleep

current_file_path = Path(__file__).parent
gecko_path = str(current_file_path / "bin" / "chromedriver")


class FirefoxAuto:
    def __init__(self, driver_path: str = gecko_path) -> None:
        self.driver_path = driver_path
        self.service = FirefoxService(executable_path=self.driver_path)
        self.options = FirefoxOptions()
        self.browser = Firefox(service=self.service, options=self.options)
        FirefoxService()

    def open(self, url: str) -> None:
        self.browser.get(url)

    def close(self) -> None:
        self.browser.quit()

    def github_panel_loaded(self) -> bool:
        return self.browser.title == "GitHub"

    def login_github(self, creds: dict[str, str]) -> None:
        try:
            sign_in_button = self.browser.find_element(by=By.LINK_TEXT, value="Sign in")
            sign_in_button.click()
            login_field = self.browser.find_element(by=By.ID, value="login_field")
            pass_field = self.browser.find_element(by=By.ID, value="password")
            login_button = self.browser.find_element(by=By.NAME, value="commit")
            login_field.send_keys(creds["login"])
            pass_field.send_keys(creds["pass"])
            login_button.click()
            sleep(1)
            if self.github_panel_loaded():
                menu_button = self.browser.find_elements(
                    by=By.CSS_SELECTOR, value=".Header-item"
                )[-1]
                menu_button.click()
                sleep(1)
                logout_button = self.browser.find_element(
                    by=By.CSS_SELECTOR, value=".dropdown-signout"
                )
                logout_button.click()
            sleep(2)

        except Exception as e:
            print(f"Erro: {e}")

        self.browser.close()

    def test(self, url: str) -> None:
        self.browser.get(url)
        sleep(1)
        self.browser.close()


def main():
    creds = {"login": my_user, "pass": my_pass}
    firefox = FirefoxAuto()
    firefox.open("https://www.github.com")
    sleep(1)
    firefox.login_github(creds)


if __name__ == "__main__":
    main()
