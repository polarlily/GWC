from random import *
five_sy = ("Get on the dance floor","Do you even care","Back it up right now","I am a savage","Never say never","You make me jiggle","I don't give no hecks","Pay me a little","I'm a love sick fool","Let's break it down","Look me in the eye","Hoping to save me","Lookin' so crazy","Right in front of me","Who let the dogs out","Look at that face","I'll give you my love","I secretly love")
seven_sy = ("I'm addicted to the pain","Buy me some pharmacy drugs","You can't have me at my best","Promise me no promises","Wake me up on the inside","I'm desperate for love and sax","Blow my brains outta my head","Never will I let you down","First things first, I'm a realist","I'm the life of the party","You got me straight in the chest","Don't worry about my dog","Shawty's life is spiraling")

a = randint(0, len(five_sy)-1)
c = randint(0, len(seven_sy)-1)
b = randint(0,len(five_sy)-1)

print(five_sy[a])
print(seven_sy[b])
print(five_sy[c])
