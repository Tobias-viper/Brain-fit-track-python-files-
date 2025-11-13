import pyrebase
firebaseConfig={
"apiKey": "AIzaSyDNZbMp6OO1WufBL3idbQFtlAnVfZxTqcE",
"authDomain": "database-a91c0.firebaseapp.com",
"projectId": "database-a91c0",
 "storageBucket": "database-a91c0.appspot.com",
"messagingSenderId": "821958889670",
 "appId": "1:821958889670:web:9013ed25fc46a68e5007c7",
 'databaseURL':'https://database-a91c0-default-rtdb.firebaseio.com'
}
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
auth=firebase.auth()



