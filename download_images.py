import requests
from bs4 import BeautifulSoup

html_file_path = input("Enter html file path: ")
output_folder_path = input("Enter output folder path: ")

with open(html_file_path, encoding="UTF-8") as f:
    soup = BeautifulSoup(f)

images = soup.findAll('img')

for image in images:
    source_url = image.get('src')
    if not source_url is None:
        print(source_url)





















