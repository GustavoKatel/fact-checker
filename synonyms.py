#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import chardet
import re

def get_synonyms(word):
    try:
        response = urllib2.urlopen('http://www.dicionarioinformal.com.br/sinonimos/'+word.replace(' ', '+'))
        # response_2 = urllib2.urlopen('http://www.dicionarioinformal.com.br/sinonimos/'+word.replace(' ', '+')+'/2')
        # response_sinonimos = urllib2.urlopen('http://www.sinonimos.com.br/'+word.replace(' ', '+'))

        html = response.read()
        # html += response_2.read()

        encoding = chardet.detect(html)
        html = html.decode('iso-8859-1')

        # regex = re.compile(r'<a href="\/[a-zA-Z\-]+\/" class="sinonimo">([a-zA-Z\-\s]+)', re.MULTILINE)
        # matches = [m.group(1) for m in regex.finditer(html)]

        regex = re.compile(r'<h3 class="di-blue">.*[0-9]+\. (.*)<\/a><\/h3>', re.MULTILINE)
        matches = [m.group(1) for m in regex.finditer(html)]

        return matches
    except Exception as e:
        print e
        return 'nada'
