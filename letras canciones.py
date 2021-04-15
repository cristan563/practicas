yummy=['''Yeah, you got that yummy-yum
That yummy-yum, that yummy-yummy
Yeah, you got that yummy-yum
That yummy-yum, that yummy-yummy
Say the word, on my way
Yeah, babe, yeah, babe, yeah, babe
Any night, any day
Say the word, on my way
Yeah babe, yeah babe, yeah babe
In the mornin' or the late
Say the word, on my way
Bonafide stallion
It ain't no stable, no, you stay on the run
Ain't on the side, you're number one
Yeah, every time I come around, you get it done (you get it done)''']

love=['''For all the times that you rain on my parade
And all the clubs you get in using my name
You think you broke my heart
Oh, girl, for goodness sake
You think I'm crying on my own, well, I ain't

And I didn't wanna write a song
'Cause I didn't want anyone thinking I still care
I don't, but you still hit my phone up

And, baby, I've been movin' on
And I think you should be somethin'
I don't wanna hold back
Maybe you should know that

My mama don't like you and she likes everyone
And I never like to admit that I was wrong''']

off=['''One touch and you got me stoned
Higher than I've ever known
You call the shots and I follow
Sun rise but the night still young
No words, but we speak in tongues
If you let me, I might say too much

Your touch blurred my vision
It's your world, and I'm just in it
Even sober I'm not thinkin' straight

'Cause I'm off my face, in love with you
I'm out my head, so into you
And I don't know how you do it
But I'm forever ruined by you, ooh, ooh, ooh

Can't sleep 'cause I'm way too buzzed''']

while True:
    print("Letras de Canciones")
    print("Selecciona una cancion  para saber la letra\n")
    print("1.- Yummy yumm - Justin Bieber")
    print("2.- Love Yourself - Justin Bieber")
    print("3.- off my face - Justin Bieber")
    print("4.- salir")
    opc = int(input())

    if opc == 1:
        print(yummy)
        pass
    if opc == 2:
        print(love)
        pass
    elif opc == 3:
        print(off)
        pass
    if opc == 4:
        break


