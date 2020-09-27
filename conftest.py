import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")#вывод сообщения,что откр.браузер
    browser = webdriver.Chrome()
    yield browser#после всего закроется браузер
    print("\nquit browser..")
    browser.quit()

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='None1',
                     help="Choose language, example, es")


@pytest.fixture(scope="class")
def language(request):
    language_name = request.config.getoption("language")
    print (language_name)
    language = 'None2'
    if language_name =="es":
        print("\nstart language Spanish for test..")
        language = "es"
    elif language_name =="fr":
        print("\nstart language French for test..")
        language ="fr"
    elif language_name =="ru":
        print("\nstart language Russian for test..")
        language ="ru"
    elif language_name =="en-gb":
        print("\nstart language British English for test..")
        language ="en-gb"
    else:
        raise pytest.UsageError("--language should be, example: es,fr,en-gb,ru")
    return(language)

