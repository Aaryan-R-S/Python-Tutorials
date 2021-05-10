import pickle
# import requests

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# response = requests.get(url)

# irisText = response.text

# items = irisText.split('\n')

# irisList = [items[i].split(',') for i in range(len(items))]   # to get list of list
# irisList.pop()
# irisList.pop()

# print(irisList)

# f = open('85.pkl', 'wb')
# pickle.dump(irisList, f) 
# f.close()


#  -- To view --

f = open('85.pkl', 'rb')
mySecretList = pickle.load(f)  
print(mySecretList)
print(type(mySecretList))

