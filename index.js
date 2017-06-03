var admin = require('firebase-admin')
var Xray = require('x-ray')

var _ = require('lodash')
var fs = require('fs')

var xray = new Xray();

var serviceAccount = require('./credentials/mymanager-d47ac-firebase-adminsdk-nij3l-141a31a2f0.json')

admin.initializeApp({
	credential: admin.credential.cert(serviceAccount),
	databaseURL: "https://mymanager-d47ac.firebaseio.com"
})



	xray('https://www.transfermarkt.com/laliga/startseite/wettbewerb/ES1',
		'div#yw1 > table > tbody > tr > td.hauptlink.hide-for-small > a.vereinprofil_tooltip',
		[{
			href:'@href',
		}])((err,teams)=>{
			if(err){
				console.error('ERROR', err)
			}else{
				teams.forEach((team)=>{
					xray(team.href,['a.spielprofil_tooltip'])((err,players)=>{
						if(err){
							console.error("ERROR",err)
						}else{
							players.forEach((player)=>{
								console.log(player)
								admin.database().ref('players').push(
								{
									name: player,
									team: team.href
								})
							})
						}
						//players.split(',').forEach((player)=>{
							//console.log(player)
						/*	admin.database().ref('players').set(
							{
								name: player,
								team: team.href
							})*/
						//})
					})
				})
			}

		})

			/*
			teams.forEach((team)=>{
			    xray(team.href, 'a.spielprofil_tooltip'
			)((err,players)=>{
					console.log(players)
					if(err){
						console.error("ERROR",err)
					}else{
						players.forEach((player)=>{
							console.log(`player: ${player}`)
						})

					}

				})
			})

		})*/

var player_database;

admin.database().ref('players').on('value', (snapshot)=>{
	player_database = snapshot.val();
	console.log(snapshot.val())
})
/*
var serviceAccount = require('./credentials/mymanager-d47ac-firebase-adminsdk-nij3l-141a31a2f0.json')

admin.initializeApp({
	credential: admin.credential.cert(serviceAccount),
	databaseURL: "https://mymanager-d47ac.firebaseio.com"
})

admin.database().ref('messages').on('value', (snapshot)=>{
	player_database = snapshot.val();
	console.log(snapshot.val())
})
*/
/*
app.listen(process.env.PORT || 3000, ()=>{
	console.log(`app listening to requests in port ${process.env.PORT}`);
})

app.get('/', (req,res)=>{
	res.send('Welcome to players API')
})

app.get('/players', (req,res)=>{
	res.json(player_database)
})
*/
