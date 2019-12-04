import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        # self.driver.set_window_size(1128, 648)
        porscheFlag = False
        searchText = "PORSCHE"
        element = None

        ### SSearch exotics in search tab and hot Enter
        self.driver.find_element(By.ID, "input-search").click()
        self.driver.find_element(By.ID, "input-search").send_keys("exotics")
        self.driver.find_element(By.ID, "input-search").send_keys(Keys.ENTER)

        ###  Wait for 5 seconds for the table to load on page
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, ".//table[@id='serverSideDataTable']")))
        except :
            print("Data table did not load")

        #If table is found, search for PORSCHE in every row, 'Make' cloumn of the table
        if element!=None:
            if element.is_displayed():
                table_tbody = self.driver.find_elements_by_xpath(".//table[@id='serverSideDataTable']/tbody")
                for row in table_tbody[0].find_elements_by_xpath(".//tr"):
                    for make in row.find_elements_by_xpath("//td[5]/span"):
                        if (make.text.casefold() == searchText.casefold()):
                            porscheFlag = True
                self.assertTrue(porscheFlag, "Couldn't find " + searchText)
        else:
            assert False, "Couldn't find " + searchText


if __name__ == '__main__':
    unittest.main()
