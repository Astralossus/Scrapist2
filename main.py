from bs4 import BeautifulSoup
from PIL import Image
import requests
import io
import os

def main():
    search_url = "https://upload.wikimedia.org/wikipedia/en/thumb/0/03/Super_Mario_Bros._box.png/220px-Super_Mario_Bros._box.png"
    #s2 = "https://www.google.com/search?client=firefox-b-d&sca_esv=596368808&sxsrf=AM9HkKl8VBgRlJMByRPD3pqg_7FVhte9aA:1704636749199&q=mario&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjJx6DfusuDAxXETKQEHfSABmkQ0pQJegQICRAB&biw=1920&bih=947#imgrc=AJPylwmXJnHc4M"


    download_image(".\\Images\\", search_url, 'downloaded.png')

"""def scrape(search_url):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    response = requests.get(search_url, headers=headers)
    print(response.text)
    
    soup = BeautifulSoup(response.content, "html.parser")"""

def download_image(download_path, url, file_name):

    if not os.path.exists(download_path):
        try:
            os.makedirs(download_path) # Create the path if it does not exist
        except OSError as error:
            print(f"Error Creating folder '{download_path}': {error}")

    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, 'wb') as f:
            image.save(f, "png")
    except Exception as e:
        print('Failed: ' + e)

if __name__ == "__main__":
    main()