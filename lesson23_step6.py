from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	button1 = browser.find_element_by_xpath("//button [contains(text(), 'journey')]").click()

	second_window = browser.window_handles[1]
	browser.switch_to.window(second_window)

	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)

	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)

	button2 = browser.find_element_by_xpath("//button [text() = 'Submit']").click()
	
finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(30)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла