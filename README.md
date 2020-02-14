# automationInstawork
take home assignment


dependencies:

pip3 install pytest

pip3 install selenium

drivers for the multiple browser. 
Chrome https://sites.google.com/a/chromium.org/chromedriver/downloads

Edge https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Firefox https://github.com/mozilla/geckodriver/releases

download the drivers and set their path in the environment variables.

Run the scripts from the command prompt: pytest test_Search_Validation.py -s

It will prompt for search terms to be entered by the user.

The validation will occur for the search terms for 3 browsers.

The scripts contains the search pattern which has been pre defined and that is www.instawork.com.
The script is going to look for the search pattern in the search results and thus determine the position of the search pattern.

