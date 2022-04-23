import sys
from turtle import title
from urllib.request import urlopen
from bs4 import BeautifulSoup
from mdutils.mdutils import MdUtils
from mdutils import Html
import validators
from datetime import date
from timeit import default_timer as timer
import os
import requests
import uuid

def print_with_space(s):
    print()
    print(s)
    print()

if __name__ == "__main__":
    start_time = timer()
    argvs = sys.argv

    if len(argvs) != 3:
        print_with_space("Incorrect Usage: The command line accepts exactly two arguments.\n" +
                        "The first is the WeChat article's URL. HTTP prefix (https:// or http://) is optional\n" + 
                        "The second is filename for the output Markdown file. Markdown suffix (.md or .markdown) is optional\n" +
                        "Example: python3 wechat2md.py mp.weixin.qq.com/s/foobar foobar")
        sys.exit()

    article = argvs[1]
    filename = argvs[2]
    if not article.startswith("https://") and not article.startswith("http://"):
        article = "https://" + article

    if not validators.url(article):
        print_with_space("Not a valid URL\n无效URL链接")
        sys.exit()

    if "mp.weixin.qq.com" not in article:
        print_with_space("URL is not on the WeChat Official Accounts Platform!\n文章不在微信公众平台上")
        sys.exit()

    page = urlopen(article)
    html_res = page.read().decode("utf-8")

    print_with_space("Article fetched. Convertion begin...")

    title = None
    author = None
    account_name = None
    date_time = None

    bs = BeautifulSoup(html_res, "html.parser")
    article_div = bs.find("div", {"id": "js_article"})

    # Title
    title_elem = article_div.find("h1", {"class": "rich_media_title", "id": "activity-name"})
    if title_elem is not None:
        title = title_elem.get_text().strip()

    # Metadata
    metadata = article_div.find("div", {"class": "rich_media_meta_list", "id": "meta_content"})

    author_elem = metadata.find("span", {"class": "rich_media_meta rich_media_meta_text"})
    if author_elem is not None:
        author = author_elem.get_text().strip()

    account_name_elem = metadata.find("strong", {"class": "profile_nickname"})
    if account_name_elem is not None:
        account_name = account_name_elem.get_text().strip()

    #TODO: extract datetime from metadata instead
    date_time = str(date.today())
    filename = date_time + '-' + filename + '.markdown'

    # Add header
    md_content = "---\nlayout: post\n"
    md_content = md_content + "title: \""   + title + '"\n'
    md_content = md_content + "author: \"" + author + ' | ' + account_name + '"\n---\n\n'

    # Content: make sure find the one in the body
    wrapper = article_div.find("div", {"class": "rich_media_wrp"})
    content_div = wrapper.find("div",  {"id": "js_content"})

    for div in content_div.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'img']):
        text = div.get_text().strip()
        if div.name == 'p':
            if not text:
                continue
            if div.parent.name == 'blockquote':
                text = '> ' + text
            md_content = md_content + text + '\n\n'
        elif div.name == 'img':
            if not div.has_attr('data-src'):
                continue
            href = div['data-src']
            res = requests.get(href.strip())
            if not os.path.isdir("./assets"):
                os.mkdir('assets')
            pic_name = uuid.uuid4().hex + '.png'
            pic = open('./assets/' + pic_name, "wb")
            pic.write(res.content)
            pic.close()

            path_name = '"/assets/' + pic_name + '"'
            print("Image saved: " + path_name)

            md_content = md_content + '\n<center><img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src=' + path_name + '></center>\n\n'

        else:
            if not text:
                continue
            # default by using h3 for all header tags
            md_content = md_content + '\n### **' + text + '**\n\n'
    
    if not os.path.isdir("./out"):
        os.mkdir("out")
    with open("./out/" + filename, 'w') as f:
        f.write(md_content)

    end_time = timer()
    print_with_space("Article converted: " + title)
    print("Success! Time taken: {0:.2f}s".format(end_time - start_time))
