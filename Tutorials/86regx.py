import re
# findall, search, split, sub, finditer

# print(r"\n")
# print("\\n")

str = '''Tata Limited
Dr. David Land34sman, executive director
18, Groverson Plaaaace
London SW1X 7HSc
Phone: +44 (20) 7235 8282
Fax: +44 (20) 7235 8172
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions : View fass map fass
bahut badhia hain
'''


'''
USE this -----
regx = re.finditer(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.([a-zA-Z0-9-.]){2,253}', str)
for i in regx:
    print(i)
    start = i.start()
    end = i.end()
    print(f"{s[start:end]}")
'''


# BOTH are SAME -- 
# regx = re.compile(r"[.]")
# regx = re.compile(r"\.")

# regx = re.compile(r'fass')
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'.iew')
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'^Ta')
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'in$')
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'so+')  # or * for 0 also
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'l+a{4}') 
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'(82){2}') 
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'(82){3}|81') 
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'\ATata') 
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'\bFax') 
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'or\b') 
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'\Bover') 
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'd\d\d') 
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'd\D') 
# g = regx.finditer(str)
# for i in g:
#     print(i)

# regx = re.compile(r'w\sfa') 
# g = regx.finditer(str)
# for i in g:
#     print(i)



