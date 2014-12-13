# Automatically created by: scrapy deploy

from setuptools import setup, find_packages

setup(
    name='fun_crawler',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = fun.settings']}, requires=['requests', 'scrapy']
)