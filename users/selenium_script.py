# selenium_script.py
from selenium import webdriver

# Initialize WebDriver (assuming Chrome in this example)
driver = webdriver.Chrome('C:\chrome-win64')

# Access the Django session data and retrieve captured data
driver.get('http://localhost:8000')  # Assuming your Django server is running locally
captured_data = driver.execute_script("return localStorage.getItem('updated_data')")

# Open the other website
driver.get('https://haegl.in/contact_us')

# Fill form elements on the other website with the captured data
driver.find_element_by_name('name').send_keys(captured_data['batch'])
driver.find_element_by_name('msg').send_keys(captured_data['commodity'])
driver.find_element_by_name('msg').send_keys(captured_data['quality'])
driver.find_element_by_name('msg').send_keys(captured_data['rs'])

# Submit the form (assuming there's a submit button)
driver.find_element_by_id('submitButton').click()

# Close the browser window when done
driver.quit()
