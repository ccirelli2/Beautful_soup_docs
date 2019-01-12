'''

findAll()      tag:         single or list of tag names inside a {} to retreive. 
               attributes
               recursive:   if set to True, the function looks into every lvl of the tree
               text
               limit:       limit the number of return values.  find() is limited to 1. 
               keywords:    Key word to search for in the attribute of the tag. 

Tree Navigation
               Ex:          bsObj.tag.subTag.anotherSubtag
                            Allows you to drill down to the location in the tree. 

               Children     Attribute can be called on a bsObj to only return the children
                            of a current tag.
                            Ex:  bsObj.find('table').children
    
               Descendants  Will return anything that descends from the requested tag, so not only
                            direct children, but the childrens descendants. 

                            Think about Children as the first level tag below are requested tag
                            and descendants as the tags within each one of those children. 

Scraping Tables:
               


'''

# Import Libraries

from bs4 import BeautifulSoup 
from urllib.request import urlopen
from urllib.request import Request
import os


url = 'https://seekingalpha.com/article/4232488-kb-homes-kbh-ceo-jeff-mezger-q4-2018-results-earnings-call-transcript'


# Standard Get BS4 Object Request

def get_bsObj(url):
    # Create bs4 Object
    request = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    html    = urlopen(request)
    bsObj   = BeautifulSoup(html.read(), 'lxml')
    return bsObj


# Find All() Key word
def test_keyword_method(bsObj):
    key_word = bsObj.findAll('div', text = 'http')
    return key_word


# Generate bsObj-------------------------------------------------------------
bsObj = get_bsObj(url)


key_word = test_keyword_method(bsObj)
print(key_word)







