import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://topai.tools/browse"
response = requests.get(url)

link1 = []
name1 = []
description1 = []
for r in range(1,40):

    soup = BeautifulSoup(response.text, "lxml")
    tool_boxes = soup.find_all("div", class_="col-xl-4 col-lg-4 col-md-6 tool_box")

    for box in tool_boxes:
        name = box.find("h5").text.strip().replace("/t/", "")
        link = box.find("a").get("href").replace("\n\n", "")
        description = box.find("p").text.strip()

        name1.append(name)
        link1.append(link)
        description1.append(description)




frame=pd.DataFrame({"tool_name":name1,"tool_link":link1,"tool_description":description1})

print(frame)
frame.to_csv("tools.csv")