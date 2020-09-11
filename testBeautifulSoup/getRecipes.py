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
# url =
url = input()
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")
a = ""
b = ""


if(a in url):
    print("title:" + stripBlank(soup.find(
        id="recipe-title").select_one(".recipe-title.fn.clearfix").get_text()))
    ing = soup.find(id="ingredients")
    serv = ing.select_one(".servings_for.yield").text
    print("servings_for yield:" + stripBlank(serv))
    ingS = ""
    ingRow = soup.find(id="ingredients_list").select(".ingredient_row")
    for a in ingRow:
        temp = getText(a, ".ingredient_category")
        if temp != None:
            ingS += temp + '\n'
        ingS += getText(a, ".name") + ":"
        ingS += getText(a, ".ingredient_quantity.amount") + '\n'
    print("材料:")
    print(ingS)
    print("step:")
    ingStep = soup.find(id="steps").select("div[class*=step]")
    # print(len(ingStep))
    for a in ingStep:
        print(stripBlank(a.select_one(".instruction").select_one(".step_text").text))

elif(b in url):
    print("title:" + stripBlank(soup.select_one(".title-wrapper").get_text()))
    ingS = ""
    ingList = soup.select_one(".ingredient-list").find_all("li")
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
    ingStep = soup.select_one(
        ".instruction-list").select(".instruction-list-item")
    for a in ingStep:
        print(stripBlank(a.select_one(".content").text))
else:
    print("そのurlに対応する処理はありません")
