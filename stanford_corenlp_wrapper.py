from selenium import webdriver
import requests
import re

sentence_pattern = r'<span style="color:.+?<\/span>'

code_pattern = r'background:(.+)?>(\w.+)?<\/span>'



driver=webdriver.PhantomJS()

driver.set_window_size(1120, 550)

def stanford_nlp_wrapper(text):


    url='http://nlp.stanford.edu:8080/ner/process'
    driver.get(url)
    data=driver.find_element_by_xpath('//*[@id="ContentBody"]/form/table/tbody/tr[4]/td/textarea').send_keys(text)
    submit=driver.find_element_by_xpath('//*[@id="ContentBody"]/form/table/tbody/tr[5]/td/input[1]').click()
    page_source =re.findall(sentence_pattern,driver.page_source)
    entities = {}
    for i in page_source:
        code_color = re.findall(code_pattern,i)
        for entity in code_color:
            if entity[0] not in entities:
                entities[entity[0]]=[entity[1]]
        else:
            entities[entity[0]].append(entity[1])

    return list(entities.values())




print(stanford_nlp_wrapper('Apple is looking at buying U.K. startup for $1 billion'))



#output

#[['Apple', 'ORGANIZATION'], ['PERSON'], ['U.K.', 'LOCATION']]
