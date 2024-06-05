import requests
from bs4 import BeautifulSoup 
import sqlite3

conn = sqlite3.connect('broadway.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS syllabus
            (id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT)
            ''')
url = "https://broadwayinfosys.com/business-analysis-training-in-nepal"

response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.content, "html.parser")
print(soup)

#Extract Syllabus 
syllabus_section = soup.find("ul", class_="course-accordion")
print(syllabus_section)

syllabus_items = syllabus_section.find_all("li")
#print(syllabus_items)
for item in syllabus_items:
    print("-", item.get_text(strip=True))

    content = item.get_text(strip=True)
    c.execute('''INSERT INTO syllabus (title, content) VALUES (?,?)''',  ("business-analysis-training-in-nepal", content))
conn.commit()
conn.close()
    