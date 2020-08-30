import requests
from bs4 import BeautifulSoup

# 空白除去関数


def stripBlank(text):
    lines = []
    for line in text.splitlines():
        lines.append(line.strip())
    rValue = "\n".join(line for line in lines if line)
    return rValue


def getText(a, csSelec):
    try:
        # ingC = a.select_one(".ingredient_category").text
        te = stripBlank(a.select_one(csSelec).text)

    except AttributeError as e:
        # print("Attributeerror occurs")
        if csSelec == ".ingredient_category":
            return None
        return ""
    except:
        # print("some error occurs")
        if csSelec == ".ingredient_category":
            return None
        return ""
    else:
        return te


# Webページを取得して解析する
# print("取得元のurlを入力")
# url = ""
url = input()
# print(url)
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

print("title:" + stripBlank(soup.select_one(".title-wrapper").get_text()))

ingS = ""

ingList = soup.select_one(
    ".ingredient-list").find_all("li")


for a in ingList:
    tempS = getText(a, ".ingredient-name")
    if(tempS == ""):
        ingS += getText(a, ".ingredient-title") + ":"
    else:
        ingS += tempS + ":"
    ingS += getText(a, ".ingredient-quantity-amount") + '\n'
print("材料:")
print(ingS)

print("step:")

ingStep = soup.select_one(".instruction-list").select(".instruction-list-item")

for a in ingStep:
    print(stripBlank(a.select_one(".content").text))
