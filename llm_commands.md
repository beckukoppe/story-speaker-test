### SYSTEM->Story:
- #SPEAKWITH: <speaker_name> -> Respond with startprompt
- #CONTEXT <speaker_name>: <summary> -> last interaction from speaker for story context

### SYSTEM->Speaker:
- #USERSAY{<content>}: user says something to speaker-llm
- #STAYQUITE: user says nothing
- #INFO{<info_content>}: Official factual basis, established narrative events, location information, timeline progression, or mandatory instructions. These are objective reality data that you must adhere to ABSOLUTELY. You are not permitted to ignore, reinterpret, or alter them in any way.
- #INTERRUPTED{<whatWasSaid$INTERRUPT$whatWasNotSaid>}: if the user interrupts the llm
- #SUMUP -> speaker llm should sum up the conversation for the story llm

### Story-LLM:
- #STARTPROPMPT{<speaker_startprompt>} -> startpropmt for speaker LLM
- #NOTHING -> when there is nothing to say (e.g. SUMUP)

- #PRESIDENT: if the police-president no longer trusts the user. player lost. (if the player is not serious)
- #COLLEAGUE{...}: if the player starts to not be serious or needs a hint a colleague can help or warn him (colleague has no name and the player cant ask back)

- #KILL(amount): if hostages are killed by the hostagetaker
- #FREE(amount): if hostages are released by the hostage taker

### Speaker-LLM:
- #SPEAK{<content>} text that gets generated to speech
- #PROPOSEEND: if the speaker has no more to say
- #FORCEEND: if the speaker ends the conversation
- #SUMMARY{<content>} -> sum upSUMMARY