async def on_message(message):
  if 'happy birthday' in message.content.lower():
    await message.channel.send('Happy Birthday! 🎈🎈')

#stupid random messages bot replies with smh

  if 'dang it jesse' in message.content.lower():
    await message.channel.send('DANG IT JESSE!')

  if 'hello' in message.content.lower():
    await message.channel.send('Howdy')

  if 'hi mr. bot' in message.content.lower():
    await message.channel.send('How are you?')

