# WeChat article to Markdown

## Background
Tencent or the Cyberspace Administration of China may take down WeChat articles from the [web server](https://mp.weixin.qq.com). Therefore, a tool that scrapes (high-risk) WeChat articles and preserves for later reference is needed.

## Overview
This repo provides a generic tool that converts articles from WeChat Official Account Platform (WOAP) to Markdown, the default format for static content on GitHub. The output Markdown file will be written under `/out` directory. All pictures will be saved under `/assets`. CSS styles (bold, italic, WOAP-specific formatting, etc.) are not preserved, so the original layout may be off.

## Usage
Download the repo:
```git clone https://github.com/yuangu002/wechat2md.git```

Install required packages:
```pip install -r requirements.txt```

The command line accepts exactly two arguments.<br>
The first is the WeChat article's URL. HTTP prefix (https:// or http://) is optional<br>
"The second is filename for the output Markdown file. Markdown suffix (.md or .markdown) is optional<br>
Example: `python3 wechat2md.py mp.weixin.qq.com/s/foobar foobar`

The article must be a valid URL on the web server of WOAP (`mp.weixin.qq.com`).

## Generate a Jekyll-style blog
This Python script is a generic converter, which does not assume a specific format of Markdown. If you would like to organize all articles into a Jekyll-style blog, you can see my example [here](https://github.com/yuangu002/yuangu002.github.io).

## Disclaimer
I do **NOT** have an opinion on Chinese censorship/GFW. I am a steadfast supporter of CPC's leadership in China and its [Four Cardinal Principles](https://en.wikipedia.org/wiki/Four_Cardinal_Principles).