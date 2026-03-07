import allure


@allure.step("Opening browser")
def open_browser():
    with allure.step("Get browser"):
        ...

    with allure.step("Start browser"):
        ...


@allure.step("Creating course")
def create_course(title: str):
    with allure.step(f"Creating course with title '{title}'"):
        ...


@allure.step("Closing browser {browser}")
def close_browser(browser: str):
    ...


def test_feature():
    with allure.step("Opening browser"):
        ...

    with allure.step("Creating course"):
        ...

    with allure.step("Closing browser"):
        ...
