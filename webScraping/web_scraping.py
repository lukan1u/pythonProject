from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/global/uk-en/gigabyte-radeon-rx-6700-xt-gv-r67xtgaming-oc-12gd/p/N82E16814932416?Description=gpu&cm_re=gpu-_-14-932-416-_-Product&quicklink=true"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# gives you an html file:
# print(doc.prettify())

# looks for the sing £
prices = doc.find_all(text = '£')
# looks for the parent of the sing £
parent = prices[0].parent
# looks for the branch where price is stored
strong = parent.find("strong")
# prints the price for the thing we were looking for
print(strong.string)
