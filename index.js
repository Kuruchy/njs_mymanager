var admin = require('firebase-admin')
var Xray = require('x-ray')
var xray = new Xray();

var serviceAccount = require('./credentials/mymanager-d47ac-firebase-adminsdk-nij3l-141a31a2f0.json')

admin.initializeApp({
	credential: admin.credential.cert(serviceAccount),
	databaseURL: "https://mymanager-d47ac.firebaseio.com"
})


// scraping transfermarkt
xray('https://www.transfermarkt.com/laliga/startseite/wettbewerb/ES1',
	'div#yw1 > table > tbody > tr > td.hauptlink.hide-for-small > a.vereinprofil_tooltip',
	[{ href:'@href'}])
	((err,teams)=>{
		if(err){
			console.error('ERROR', err)
		}else{
			teams.forEach((team)=>{
				xray(team.href,['a.spielprofil_tooltip'])
				((err,players)=>{
					if(err){
						console.error("ERROR",err)
					}else{
						players.forEach((player)=>{
							admin.database().ref('players').push(
								{
									name: player,
									team: team.href
								}
							)
						})
					}
				})
			})
		}
	})

// to keep track of changes in the database
admin.database().ref('players').on('value', (snapshot)=>{
	player_database = snapshot.val();
})
