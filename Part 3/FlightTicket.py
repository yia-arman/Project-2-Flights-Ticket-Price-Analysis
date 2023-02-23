from selenium import webdriver
import os

URL = 'https://www.kayak.com/'



class FlightTicket(webdriver.Chrome):
    def __init__(self, driver_path='/usr/local/bin', exit=False):
        self.driver_path = driver_path
        self.exit = exit
        super(FlightTicket,self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()

    def get_webpage(self):
        self.get(URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.exit:
            self.quit()


    def fly_from(self, location):

        clear_box = self.find_element_by_css_selector(
            'div[aria-label="Remove"]'
        )
        clear_box.click()

        from_box = self.find_element_by_css_selector(
            'input[aria-label="Flight origin input"]'
        )
        from_box.click()
        from_box.clear()
        from_box.send_keys(location)

        drop_down = self.find_element_by_id('flight-origin-smarty-input-list')
        drop_down.click()

    def fly_to(self, location):
        from_box = self.find_element_by_css_selector(
            'input[aria-label="Flight destination input"]'
        )
        from_box.click()
        from_box.clear()
        from_box.send_keys(location)

        drop_down = self.find_element_by_id('flight-destination-smarty-input-list')
        drop_down.click()

    def flight_date(self):
        start_date = self.find_element_by_css_selector(
            'span[aria-label="Start date calendar input"]'
        )
        start_date.click()

        monthly_calaneder = self.find_element_by_class_name('ATGJ-monthWrapper')
        month = self.find_element_by_css_selector(
            'div[data-month = "2023-03"]'
        )
        day = month.find_element_by_css_selector(
            'div[aria-label="Friday March 24, 2023"]'
        )
        day.click()







    def submit(self):
        button = self.find_element_by_css_selector(
            'button[aria-label="Search"]'
        )
        button.click()






