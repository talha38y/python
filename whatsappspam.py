from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

print("Bekleyin...\n")
print("Web qr tarayıcısı hazırlayınız...\n")

name = input("Göndereceğiniz Kişinin İsimini Girin: ")
count = int(input("Mesaj Sayısı: "))
msg = input("Mesajınızı Yazın: ")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msgBox.send_keys(msg)
    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    sendButton.click()
