# WeChat article to Markdown

## Background
Tencent or the Cyberspace Administration of China may take down WeChat articles from the [web server](https://mp.weixin.qq.com). Therefore, a tool that scrapes (high-risk) WeChat articles and preserves for later reference is needed.

## Overview
This repo provides a generic tool that converts articles from WeChat Official Account Platform (WOAP) to Markdown, the default format for static content on GitHub. The output Markdown file will be written under `/out` directory. All pictures will be saved under `/assets`, if download of images is enabled. CSS styles (bold, italic, WOAP-specific formatting, etc.), embedded videos, and podcasts are not saved.

## Usage
Download the repo:

```git clone https://github.com/yuangu002/wechat2md.git```

Install required packages:

```pip install -r requirements.txt```

Run the script:

```python3 wechat2md.py mp.weixin.qq.com/s/foobar foobar```. By default, pictures are not downloaded. To enable this feature, set the `DOWNLOAD_PIC` flag [here](wechat2md.py#L13) to `True` and re-run the command.

Replace `mp.weixin.qq.com/s/foobar` with a Wechat article's link. Once you see the success message, `foobar.markdown` can be found under `/out`.

## Note
The CLI accepts exactly two arguments. The first is the WeChat article's URL. HTTP prefix (https:// or http://) is optional. The second is filename for the output Markdown file. Markdown suffix (.md or .markdown) is optional.

The article must be a valid URL on the web server of WOAP (`mp.weixin.qq.com`).

The tool is designed to scrape texts; therefore, the `DOWNLOAD_PIC` flag should be used with care, especially dealing with articles with a lot of pictures or gifs, which could significantly lower the performance or explode your local storage. GitHub only supports storage of a single item within 100 MiB. Anything item larger than 100 MiB should be handled by [GitHub Large File Storage](https://git-lfs.github.com/).

## Generate a Jekyll-style blog
This Python script is a generic converter, which does not assume a specific format of Markdown. If you would like to organize all articles into a Jekyll-style blog, you can see my example [here](https://github.com/yuangu002/yuangu002.github.io).

## Disclaimer
I do **NOT** have an opinion on Chinese censorship/GFW. I am a steadfast supporter of CPC's leadership in China and its [Four Cardinal Principles](https://en.wikipedia.org/wiki/Four_Cardinal_Principles).