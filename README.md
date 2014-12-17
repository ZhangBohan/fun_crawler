# 美图爬虫

By [Bohan](https://github.com/ZhangBohan).

## Description

这个项目仅用于学习

目标是爬取各上的美图，目前实现的爬取[妹子图](http://www.meizitu.com/)，
还有两个cosplay图片爬取的爬虫

## Installation

    > git clone https://github.com/ZhangBohan/fun_crawler.git
    > cd fun_crawler
    > sudo easy_install virtualenv
    > virtualenv venv
    > source venv/bin/activate
    > python setup.py --requires | xargs pip install
    
## Usage

 * 妹子图：`python run.py crawl meizitu`
 * coser `scrapy crawl coser -o items.csv -t csv`