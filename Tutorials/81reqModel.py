import requests

# https://financialmodelingprep.com/developer/docs/       -- REFER --


#  GET --
# url = "https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=demo"
url = "https://randomuser.me/api/"
r = requests.get(url=url)
print(r.text)
print(r.status_code)


#  POST --
url = "https://jsonplaceholder.typicode.com/posts"
data ={
    "title": "foo",
    "body": "bar",
    "userId": 1
}
r = requests.post(url=url, data=data)
print(r.text)
print(r.status_code)

'''

//GET REQUESTS--
// URL -- https://randomuser.me/api/

// JSON/PARAMS  -- ANT TEXT



//  POST REQUESTS ---
//  URL --  https://jsonplaceholder.typicode.com/posts

//  JSON--
//   {
//     "title": "foo",
//     "body": "bar",
//     "userId": 1
//   }

// PARAMS -- above text as words in key & value e.g.
//     title     foo
//     body      bar
//     userId    1


'''