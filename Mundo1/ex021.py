# This program plays an MP3 file. It assumes you have the file in the same directory.
# Note: This example uses the `pygame` module, but you need to install it before running the program.

from pygame import mixer

mixer.init()
mixer.music.load("musica.mp3")
mixer.music.play()
input("Pressione Enter para parar a música...")
mixer.music.stop()
