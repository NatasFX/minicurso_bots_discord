@client.event
async def on_voice_state_update(member, state_before, state_after):
   if state_before.self_mute != state_after.self_mute:
       # mutou ou desmutou
   elif state_before.self_video != state_after.self_video:
       # abriu ou fechou câmera
   elif not state_before.self_stream and state_after.self_stream:
       # iniciou uma stream
