from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Mark has heard about a cool new website where he can say whatever he wants! He goes to checkout it's homepage
        self.browser.get("http://localhost:8000")

        # He notices that the page's title mentions Twitter
        self.assertIn('Twitter', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Twitter', header_text)

        # He is invited to tweet right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a thought')

        # HE types "I could really use a coffee right now"
        inputbox.send_keys('I could really use a coffee right now!')

        # When he hits enter, the page updates, and the page now lists "I could really use a coffee right now"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('I could really use a coffee right now!')

        # There is still a textbox inviting him to tweet again, so he enters "Myspace is so 2008"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Myspace is so 2008')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, showing both his tweets
        self.check_for_row_in_list_table('I could really use a coffee right now!')
        self.check_for_row_in_list_table('Myspace is so 2008')

        # Mark wonders if the site will remember his list, then he sees that the site unqiue url just for him

        # He visits that url and his tweets are still there!

        # Satisfied he goes back to his water bed
        self.fail("Finish the functional tests!")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
