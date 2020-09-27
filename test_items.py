import pytest
from selenium import webdriver
import time
link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        time.sleep(5)

    def test_basket_in(self, browser,language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
        browser.find_element_by_css_selector("button:nth-child(3)")
        assert True