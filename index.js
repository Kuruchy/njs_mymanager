var firebase = require('firebase-admin')


var serviceAccount = require('credentials/')

admin.initializeApp({
	credential: admin.credential.cert(serviceAccount),
	databaseURL: "https://"
})

admin.database().ref('').on('value', (snapshot)=>{
	console.log(snapshot.val())
})
