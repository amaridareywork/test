from pygame import mixer

mixer.init()
mixer.music.load('./sound/space.ogg')
mixer.music.set_volume(0.20)
mixer.music.play()
fire_sound = mixer.Sound('./sound/fire.ogg')
fire_sound.set_volume(0.20)