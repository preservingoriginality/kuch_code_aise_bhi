
from requests import get
import json
import gdown
import pymupdf
import io
url=''


print(url)
output = 'file.pdf'
gdown.download(url,output,quiet=False)
reader = pymupdf.open(output)
writer = io.open('/home/llmmarathi/Pendse/15/vidhan.txt', 'a', encoding='utf-8')
for page in reader:
                data = page.get_text()
                writer.write(data)
writer.close()
reader.close()
