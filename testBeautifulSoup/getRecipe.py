import requests
from bs4 import BeautifulSoup

# 空白除去関数


def stripBlank(text):
    lines = []
    for line in text.splitlines():
        lines.append(line.strip())
    rValue = "\n".join(line for line in lines if line)
    return rValue

# Webページを取得して解析する


# print("取得元のurlを入力")
url =
# url = input()
# print(url)
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

print("title:" + stripBlank(soup.find(
    id="recipe-title").select_one(".recipe-title.fn.clearfix").get_text()))
# print("recipe title:" + title)

"""空行を外す処理
lines = []
for line in title.splitlines():
    lines.append(line.strip())
# print(len(lines))
Ltext = "\n".join(line for line in lines if line)
print(Ltext)
"""


ing = soup.find(id="ingredients")
serv = ing.select_one(".servings_for.yield").text
print("servings_for yield:" + stripBlank(serv))


ingS = ""
ingRow = soup.find(id="ingredients_list").select(".ingredient_row")
# print(len(ingRow))
for a in ingRow:
    try:
        # ingC = a.select_one(".ingredient_category").text
        ingS += stripBlank(a.select_one(".ingredient_category").text) + '\n'

    except AttributeError as e:
        # print("Attributeerror occurs (in category)")
        #
        pass
    except:
        # print("some error occurs(in category)")
        pass
    else:
        pass

    try:
        ingS += stripBlank(a.select_one(".name").text) + ":"
    except AttributeError as e:
        # print("Attributeerror occurs (in name)")
        pass
        # continue
    except:
        # print("some error occurs(in name)")
        # continue
        pass
    else:
        # print(name)
        pass

    try:
        ingS += stripBlank(a.select_one(".ingredient_quantity.amount").text) + '\n'
    except AttributeError as e:
        # print("Attributeerror occurs (in quantity)")
        ingS += '\n'
        pass
        # continue
    except:
        # print("some error occurs(in quantity)")
        # continue
        pass
    else:
        # print(qAmount)
        pass
print("材料:")
print(ingS)

print("step:")
ingStep = soup.find(id="steps").select(".step")
# ingStep = soup.find(id = "")
# print(len(ingStep)) -> 5
for a in ingStep:
    print(stripBlank(a.select_one(".instruction").select_one(".step_text").text))


# HTML全体を表示する
# print(soup)
