"""import requests

# Replace "example.com" with the website URL that contains the image you want to download
url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"

# Replace "image.jpg" with the filename you want to save the image as
filename = "haarcascade_frontalface_default.xml"

# Send a GET request to the URL
response = requests.get(url)

# Save the response content to a file
with open(filename, "wb") as f:
    f.write(response.content)
print("hi")"""
"""
import requests
from bs4 import BeautifulSoup
import os

# Replace "example.com" with the website URL that contains the images you want to download
url = "https://en.wikipedia.org/wiki/Robert_Downey_Jr."
# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all image tags in the HTML content
image_tags = soup.find_all("img")

# Create a directory to save the images in
if not os.path.exists("images"):
    os.makedirs("images")

# Download each image and save it to the images directory
for img in image_tags:
    img_url = img.attrs.get("src")
    if not img_url:
        continue

    # Download the image
    img_response = requests.get(img_url)

    # Get the filename from the URL and save the image to the images directory
    filename = os.path.join("images", os.path.basename(img_url))
    with open(filename, "wb") as f:
        f.write(img_response.content)

print("All images downloaded!")
"""
from bs4 import *
import requests
import os
 
# CREATE FOLDER
def folder_create(images):
    try:
        folder_name = input("Enter Folder Name:- ")
        # folder creation
        os.mkdir(folder_name)
 
    # if folder exists with that name, ask another name
    except:
        print("Folder Exist with that name!")
        folder_create()
 
    # image downloading start
    download_images(images, folder_name)
 
 
# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):
   
    # initial count is zero
    count = 0
 
    # print total images found in URL
    print(f"Total {len(images)} Image Found!")
 
    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            # From image tag ,Fetch image Source URL
 
                        # 1.data-srcset
                        # 2.data-src
                        # 3.data-fallback-src
                        # 4.src
 
            # Here we will use exception handling
 
            # first we will search for "data-srcset" in img tag
            try:
                # In image tag ,searching for "data-srcset"
                image_link = image["data-srcset"]
                 
            # then we will search for "data-src" in img
            # tag and so on..
            except:
                try:
                    # In image tag ,searching for "data-src"
                    image_link = image["data-src"]
                except:
                    try:
                        # In image tag ,searching for "data-fallback-src"
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            # In image tag ,searching for "src"
                            image_link = image["src"]
 
                        # if no Source URL found
                        except:
                            pass
 
            # After getting Image Source URL
            # We will try to get the content of image
            try:
                r = requests.get(image_link).content
                try:
 
                    # possibility of decode
                    r = str(r, 'utf-8')
 
                except UnicodeDecodeError:
 
                    # After checking above condition, Image Download start
                    with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
                        f.write(r)
 
                    # counting number of image downloaded
                    count += 1
            except:
                pass
 
        # There might be possible, that all
        # images not download
        # if all images download
        if count == len(images):
            print("All Images Downloaded!")
             
        # if all images not download
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")
 
# MAIN FUNCTION START
def main(url):
   
    # content of URL
    r = requests.get(url)
 
    # Parse HTML Code
    soup = BeautifulSoup(r.text, 'html.parser')
 
    # find all images in URL
    images = soup.findAll('img')
 
    # Call folder create function
    folder_create(images)
 
 
# take url
url = input("Enter URL:- ")
 
# CALL MAIN FUNCTION
main(url)