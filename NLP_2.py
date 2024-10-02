# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:40:22 2024

@author: Admin
"""



##Extract Information From the Text like age,moblie no., ect

import re
chat1 = 'my numner is : 123654897 '

def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]
    
get_pattern_match('order[^\d]*(\d*)', chat1)

#######################


chat1 = 'you ask lost of qurstions 1234678912, abc@xyz.com'
chat2 = 'here is :(123)0123654897, abc@xyz.com'
chat3 = 'your phone : 1234678912, abc@xyz.com'

get_pattern_match('[a-zA-Z0-9]*@[a-z]*\.[a-zA-Z0-9]*]', chat1)
get_pattern_match('[a-zA-Z0-9]*@[a-z]*\.[a-zA-Z0-9]*]', chat2)
get_pattern_match('[a-zA-Z0-9]*@[a-z]*\.[a-zA-Z0-9]*]', chat3)


#############################

get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat1)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat2)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat3)

################################

text = '''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partners	
Grimes (2018–2021)[1]
Children	11[a][3]
Parents	
Errol Musk
Maye Musk
Relatives	
Kimbal Musk (brother)
Tosca Musk (sister)
Lyndon Rive (cousin)
'''

get_pattern_match(r'age (\d+)', text)
get_pattern_match(r'Born(.*)\n', text).strip()
get_pattern_match(r'Born.*\n(.*)\(age', text).strip()
get_pattern_match(r'\(age.*\n(.*)', text)

################################################


import re

text = '''Born	Elon Reeve Musk 
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
'''



###################################################

text1 = '''Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 67)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''

def extract_personal_information(text1):
    age = get_pattern_match('age (\d+)', text1)
    full_name = get_pattern_match('Born(.*)\n', text1)
    birth_date = get_pattern_match('Born.*\n(.*)\(age', text1)
    birth_place = get_pattern_match('\(age.*\n(.*)', text1)
    return{
        'age': int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }

extract_personal_information(text1)

​################################################

fron PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader

reader = PdfReader('here give path of pdf') 
##printing No.Of pages in a pdf
print(len(reader.pages))

##getting specific page from the pdf

page = reade.pages[2]

##extracting text from page

print(text)

#####################






















