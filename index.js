var admin = require('firebase-admin')

var cheerio = require('cheerio')
var request = require('request')




var serviceAccount = require('./credentials/mymanager-d47ac-firebase-adminsdk-nij3l-141a31a2f0.json')

// URLs from scrapped webpages
// initialize firebase
admin.initializeApp({
	credential: admin.credential.cert(serviceAccount),
	databaseURL: "https://mymanager-d47ac.firebaseio.com"
})
// to keep track of changes in the firebase database
admin.database().ref('players').on('value', (snapshot)=>{
	player_database = snapshot.val();
})

/*
* scrape configuration and function to get player names
*/
const SCRAPE_CONFIG = (base_url, league_url, team_selector, player_selector)=>{
	return{
		base_url,
		league_url,
		team_selector,
		player_selector
	}
}
const scrape_player_names = {
	standard: (config)=>{
		return (
			request(config.base_url + config.league_url, (error, response, html)=>{
				if(!error && response.statusCode == 200){
					var $ = cheerio.load(html)
					$(config.team_selector).each((index,team)=>{
						request(config.base_url + $(team).attr('href'),(error,response,html)=>{
							if(!error && response.statusCode == 200){
								var $p = cheerio.load(html)
								$p(config.player_selector).each((index,player)=>{
									// Player names
									console.log($p(player).text())
								})
							}
						})
					})
				}
			})
		)
	},
	protected: (config)=>{
		return (
			null
		)
	}
}



/*
*
*  WHOSCORED
*
*/
const WHOSCORED = SCRAPE_CONFIG('https://www.whoscored.com',
					'/Regions/206/Tournaments/4/Spain-La-Liga',
					'tbody.standings > tr > td > a.team-link',
					'tbody#player-table-statistics-body > tr > td.pn > a.player-link')

//scrape_player_names.protected(WHOSCORED)


/*
* TRANSFERMARKT
*/
const TRANSFERMARKT = SCRAPE_CONFIG(
	'https://www.transfermarkt.com',
	'/laliga/startseite/wettbewerb/ES1',
	'div#yw1 > table > tbody > tr > td.hauptlink.hide-for-small > a.vereinprofil_tooltip',
	'span.hide-for-small > a.spielprofil_tooltip'
)
scrape_player_names.standard(TRANSFERMARKT)
