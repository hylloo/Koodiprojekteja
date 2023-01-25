import discord

async def antimoi(message):
    msg_content = message.content.lower()
    curseWord = ['moi', 'moro', 'moikka'] #kielletyt sanat
      #  # delete curse word if match with the list
    if any(word in msg_content for word in curseWord):
        await message.delete()
     # #################################
antimoi()