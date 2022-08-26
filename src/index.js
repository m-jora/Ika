require('dotenv').config();
const { Client, GatewayIntentBits } = require('discord.js');

const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.once('ready', () => {
  console.log('Yeehaw');
})

//console.log(process.env.TOKEN);
client.login(process.env.TOKEN);