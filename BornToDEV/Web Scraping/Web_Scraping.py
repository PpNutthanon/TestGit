from bs4 import BeautifulSoup # libraries ในการใช้งาน web scraping
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
print(soup.find(string="bad")) #Todo: หาคำว่า bad
print(soup.find(string="pp"))
print(soup.find(string="HTML"))

print(soup.i) #TODO: 
print(soup.p)
print(soup.b) #TODO: ดึงข้อมูลทั้งก้อนของ Tag b มาทั้งหมด

