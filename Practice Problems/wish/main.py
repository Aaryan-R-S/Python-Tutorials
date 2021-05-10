# Refer Code With Harry Auto. Birthday Wisher !
import pandas
from datetime import datetime
import smtplib
import os
os.mkdir('testing')

gmailId = 'your-gmail-id'
gmailPwd = 'your-gmail-pwd'

def sendEmail(to, sub, msg, name):
    print(f"\nEmail to {name} sent ! \nSubject: {sub} \nMessage: {msg} \nGmail: {to}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(gmailId, gmailPwd)
    s.sendmail(gmailId, to, f"Subject: {sub}\n\n{msg} ")
    s.quit()

if __name__ == "__main__":
    dataExcel = pandas.read_excel("data.xlsx")
    # print(dataExcel)
    yearNow = datetime.now().strftime("%Y")
    today = datetime.now().strftime("%d-%m")
    # print(today)

    for index, item in dataExcel.iterrows():
        # print(index, item['Birthday'])

        bday = item['Birthday'].strftime('%d-%m')
        # print(bday)
        
        writInd = []
        if today == bday and yearNow not in str(item['Year']):
            sendEmail(item['Gmail'], f"Happy Birthday! {item['Name']}!", f"Dear {item['Name']}... \n{item['Dialogue']}", item['Name'])
            writInd.append(index)

        for i in writInd:
            y = dataExcel.loc[index, 'Year']
            dataExcel.loc[index, 'Year'] = str(y) + ',' + str(yearNow)
 
    dataExcel.to_excel('data.xlsx', index=False)
    # print(dataExcel)

