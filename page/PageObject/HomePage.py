#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/5/31 18:11
# @Author  : wuyfee
# @File    : HomePage.py
# @Software: PyCharm


from page.BasePage import BasePage

class HomePage(BasePage):

    def click_knowGuangfa(self, handleBy, handleLocator, by, locator, jumpPage, resultBy, resultLocator):
        if handleBy != 'None':
            self.handle_mouse(handleBy, handleLocator)
        if self.is_click(by, locator) is not None:
            self.click(by, locator)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        message = self.get_element_text(resultBy, resultLocator)
        if jumpPage == 'Y':
            self.close()
            self.driver.switch_to.window(handles[0])
        elif handleBy != 'None':
            self.back()
        return message

    def click_peopleInGuangfa(self, handleBy, handleLocator, by, locator, resultBy, resultLocator):
        if handleBy != 'None':
            self.handle_mouse(handleBy, handleLocator)
        if self.is_click(by, locator) is not None:
            self.click(by, locator)
        message = self.get_element_text(resultBy, resultLocator)
        if handleBy != 'None':
            self.back()
        return message

    def click_homePage_menu(self,  by, locator, resultBy, resultLocator, isBack):
        self.click(by, locator)
        message = self.get_element_text(resultBy, resultLocator)
        if isBack == 'Y':
            self.back()
        return message

    '''
    def click_home_page_menu(self, by, locator):
        return self.click(by, locator)
    def click_knowGuangfa1(self, byHome, locatorHome, by, locator):
        handles = self.driver.window_handles
        self.handle_mouse(byHome, locatorHome)
        self.click(by, locator)
        self.driver.switch_to.window(handles[-1])
        self.sleep(3)
        self.back()

    def click_companyProfile(self, byHome, locatorHome, by, locator):

        self.handle_mouse(byHome, locatorHome)
        self.click(by, locator)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.sleep(3)
        self.close()
        self.driver.switch_to.window(handles[0])
        self.sleep(3)

    def click_corporateCulture(self, byHome, locatorHome, by, locator):
        self.handle_mouse(byHome, locatorHome)
        self.click(by, locator)
        self.sleep(3)
        self.back()

    def click_departmentIntroduction(self, byHome, locatorHome, by, locator):
        self.handle_mouse(byHome, locatorHome)
        self.click(by, locator)
        self.sleep(3)
        self.back()



    def click_peopleInGuangfa1(self, by, locator):
        self.click(by, locator)
        self.sleep(3)
        self.back()

    def click_employeeAspiration(self, byHome, locatorHome, by, locator):
        self.handle_mouse(byHome, locatorHome)
        self.click(by, locator)
        self.sleep(3)
        self.back()

    def click_careerDevelopment(self, byHome, locatorHome, by, locator):
        self.handle_mouse(byHome, locatorHome)
        self.click(by, locator)
        self.sleep(3)
        self.back()

    def click_personelTrain(self, byHome, locatorHome, by, locator):
        self.handle_mouse(byHome, locatorHome)
        self.click(by, locator)
        self.sleep(3)
        self.back()

    def click_welfareCare(self, byHome, locatorHome, by, locator):
        self.handle_mouse(byHome, locatorHome)
        self.click(by, locator)
        self.sleep(3)
        self.back()

    def click_careOfGuangfa(self, byHome, locatorHome, by, locator):
        self.handle_mouse(byHome, locatorHome)
        self.click(by, locator)
        self.sleep(3)
        self.back()
        #self.quit_driver()

    def click_internshipHirePage(self, by, locator):
        self.click(by, locator)
        self.sleep(3)
        self.back()
        self.quit_driver()

    def goto_login(self,by, locator):
        self.driver.find_element(by, locator)
    '''

if __name__ == '__main__':
    pass
