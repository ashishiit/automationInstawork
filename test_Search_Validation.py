# Import the 'modules' that are required for execution
import time
import pytest
#import pytest_html
from selenium import webdriver
from time import sleep

#Fixture for the multiple browsers
@pytest.fixture(params=[ "chrome", "firefox", "edge"],scope="class")
def driver_init(request):
    if request.param == "chrome":
      web_driver = webdriver.Chrome()
    if request.param == "firefox":
      web_driver = webdriver.Firefox()
    if request.param == "edge":
      web_driver = webdriver.Edge()
    
    request.cls.driver = web_driver
    
    yield
    web_driver.close()
#pre defined search pattern	
search_pattern = 'www.zomato.com'

#accept Google search terms as input
search_terms = input("enter search string ").strip()

@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass
class Test_URL(BasicTest):
        
        def test_validate_search(self):
            self.driver.get("https://www.google.com")
            #validate search engine			
            assert('Google' in self.driver.title)
            search_criteria = self.driver.find_element_by_name("q")
            search_criteria.clear()
            search_criteria.send_keys(search_terms)
            search_criteria.submit()
            time.sleep(5)
			#validate search terms
            assert(search_terms in self.driver.title)
			#store Next button on Google search engine
            next = self.driver.find_element_by_xpath('//a[@id="pnnext"]/span[2]')
			#default position is initialized to 1
            position = 1
			
			#browse through the search pages of the results to determine the position
            while next is not None:            
              a = False
			  #store element of links on the search page except the Ad links
              elem = self.driver.find_elements_by_xpath("//cite[contains(@class,'iUh30')]")
			  
              print('---links on the %s page exluding Ad links---' % self.driver.name)
              for i in elem:
                if len(i.text)>0:
                    print(i.text)  
               					
              #check if www.instawork.com is a substring of the links on the search page           
              for i in elem:                
                  if (len(i.text) == 0):
                      continue
                  else:
                      if search_pattern in i.text:  
                          a = True                      
                          
                          break
                      position = position+1
              #validate the position					  
              if a is True:
                if position != 1:
                    print("---position in %s = %d---" %(self.driver.name, position))                    
                else:
                    print("---Success ! %s appears first in search in %s---" %(search_pattern, self.driver.name))
                    
                break
              else:
                time.sleep(5)                
                next.click()
                next = self.driver.find_element_by_xpath('//a[@id="pnnext"]/span[2]')
                print('----GOING TO NEXT PAGE-----')