import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

print("取得元のurlを入力")
url = input()

print(url)

html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

title = soup.find(
    id="recipe-title").select_one(".recipe-title.fn.clearfix").text
print("recipe title:" + title)

ing = soup.find(id="ingredients")
serv = ing.select_one(".servings_for.yield").text
print("servings_for yield:" + serv)

ingRow = soup.find(id="ingredients_list").select(".ingredient_row")

print("材料:")
for a in ingRow:

    try:
        ingC = a.select_one(".ingredient_category").text
    except AttributeError as e:
        # print("Attributeerror occurs (in category)")
        pass
    except:
        print("some error occurs(in category)")
        pass
    else:
        print(ingC)

    try:
        name = a.select_one(".name").text
    except AttributeError as e:
        print("Attributeerror occurs (in name)")
        # pass
        continue
    except:
        print("some error occurs(in name)")
        continue
    else:
        print(name)

    try:
        qAmount = a.select_one(".ingredient_quantity.amount").text
    except AttributeError as e:
        print("Attributeerror occurs (in quantity)")
        # pass
        continue
    except:
        print("some error occurs(in quantity)")
        continue
    else:
        print(qAmount)


print("step:")
ingStep = soup.find(id="steps").select(".step")
# ingStep = soup.find(id = "")
# print(len(ingStep)) -> 5
for a in ingStep:
    print(a.select_one(".instruction").select_one(".step_text").text)


# HTML全体を表示する
# print(soup)
