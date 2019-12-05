import unittest
from selenium import webdriver

class Challenge3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")

        makesModelsElement = self.driver.find_elements_by_xpath(".//*[@id='tabTrending']/div[1]/div[2]")
        for subdiv in makesModelsElement[0].find_elements_by_xpath(".//div"):
            for list in subdiv.find_elements_by_xpath(".//ul/li"):
                makemodel = list.find_elements_by_xpath(".//a")[0].text
                hrefvalue = list.find_elements_by_xpath(".//a")[0].get_attribute("href")
                print(makemodel+" - "+hrefvalue)

if __name__ == '__main__':
    unittest.main()
