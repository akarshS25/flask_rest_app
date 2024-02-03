import requests
from bs4 import BeautifulSoup
import mysql.connector


url = ("https://bintable.com/card-schemes")
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify())
table = soup.find('table')
#print(table.prettify())

if table:
    data = []
   #  for row in table.find_all('tr'):
    for row in table.select('body > main > div.container > div > div > div > div.table-responsive > table > tbody'):
        cells = row.find_all('td')
        if len(cells) == 2:
            data.append((cells[0].text.strip(), cells[1].text.strip()))



    conn = mysql.connector.connect(host='localhost',password='Akarsh_25',user='root',database='project1')
    cursor = conn.cursor()

    insert_query = "INSERT INTO data (s_no,datacol) VALUES (%s, %s)"

    try:
       cursor.executemany(insert_query,data)
       conn.commit()
       print("Data insertsd into mysql succesfully")
    except Exception as e:
       print(f"Error: {e}") 
       conn.rollback()
    finally:
       cursor.close()
       conn.close()       

else:
    print("No table found")
