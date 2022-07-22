from bs4 import BeautifulSoup
import requests
root = 'https://www.dsebd.org/'
url = f'{root}/company_listing.php'
result = requests.get(url)
content = result.text
soup = BeautifulSoup(content,'html.parser')
box = soup.find('div',class_='BodyContent')
#print(soup.prettify())
Trading_Name = []
for trading_name in soup.find_all('a', class_='abhead'):
    Trading_Name.append(trading_name['href'].split("=")[1])
print(Trading_Name)

Company_URL =[]
for name in box.find_all('a',href=True):
    Company_URL.append(name['href'])

print(Company_URL)


for name in Company_URL:
    url = f'{root}/{Company_URL}'
    result = requests.get(url)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')
    box = soup.find('div', class_='BodyContent')
    HEADER = ["Trading Code", "Company Name"]

    # [0] Market Info Table, [1] Basic Infor Table, [11] Company Address Table
    """ MARKET INFORMATION"""
    # Market Information Table
    MI_table = soup.find('table', class_="table table-bordered background-white", id="company")

    # Headers/Name of data in to Market Information Table
    # MI_headers = []
    for header in MI_table.find_all('th'):
        # print(header.text.strip())
        HEADER.append(header.text.strip())
    HEADER.insert(6 + 2, "Change(%)")  # inserting change(%) again because the html file does't contain data header

    """ BASIC INFORMATION"""
    BI_table = soup.find_all('table', class_="table table-bordered background-white", id="company")[1]

    # BI_headers = []
    for header in BI_table.find_all('th')[0:8]:
        # print(header.text.strip())
        HEADER.append(header.text.strip())

    """ ADDRESS OF THE COMPANY"""
    Ad_table = soup.find_all('table', class_="table table-bordered background-white", id="company")[11]

    # Ad_headers = []
    for i, td in enumerate(Ad_table.find_all('td')):
        data = td.text.strip()
        # print(i, data)
        if i % 2 == 0:
            HEADER.append(data)

    # HEADER.append(MI_headers)
    # HEADER.append(BI_headers)
    # HEADER.append(Ad_headers)

    HEADER

