from requests import get
import json
import gdown
import pymupdf
import io

url = 'https://tools.nptel.ac.in/npteldata/translation.php'


def GetData(data: dict) -> str:
    if data['Marathi'] != "Completed":
        return ''
    link = 'https://tools.nptel.ac.in/npteldata/downloads.php?id=' + \
        data['Course_Id']
    data = json.loads(get(link).text)['data']['books']
    for byte in data:
        title = byte['title']
        if title == 'marathi':
            head = 'https://drive.google.com/uc?id='
            url = byte['url'].split('/')
            id_ = url[url.index('d') + 1]
            url = head + id_
            print(url)
            output = 'file.pdf'
            gdown.download(url, output, quiet=False)
            reader = pymupdf.open(output)
            writer = io.open('Data-NPTEL.txt', 'a', encoding='utf-8')
            for page in reader:
                data = page.get_text()
                writer.write(data)
            writer.close()
            reader.close()

    # course_page = BeautifulSoup(get(link).text, 'html.parser')


course_data = json.loads(get(url=url).text)['data']
for data in course_data:
    GetData(data)
# for data in course_data:
