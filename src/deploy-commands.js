const { SlashCommandBuilder, Routes } = require('discord.js');
const { REST } = require('@discordjs/rest');
require('dotenv').config();

const clientId = '979077308860215397'
const guildId = '721110814706368563'

const commands = [
  new SlashCommandBuilder().setName('ping').setDescription('Replies with a pong'),
  new SlashCommandBuilder().setName('server').setDescription('server info'),
  new SlashCommandBuilder().setName('user').setDescription('user info'),
]
    .map(command => command.toJSON());

const rest = new REST({ version: '10' }).setToken(process.env.TOKEN);

rest.put(Routes.applicationGuildCommands(clientId, guildId), {body: commands })
  .then(() => console.log('succesfully registered commands'))
  .catch(console.error);


