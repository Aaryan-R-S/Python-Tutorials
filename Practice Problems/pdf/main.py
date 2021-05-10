import PyPDF2

a = PyPDF2.PdfFileReader('sample.pdf')

print(a.documentInfo)

s = ''
for i in range(a.getNumPages()):
    s += a.getPage(i).extractText()

with open("text.txt", "w", encoding='utf-8') as f:
    f.write(s)

print(a.getPage(0).getContents())