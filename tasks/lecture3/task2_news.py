import requests
from lxml import html

main_page = 'https://www.python.org/'

page = requests.get(main_page)
page_tree = html.fromstring(page.content)
preview = page_tree.xpath("//div[contains(@class,'blog-widget')]//ul/li[1]//a/text()")[0]
print(preview)