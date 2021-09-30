from pydub import AudioSegment 
from pydub.playback import play 
#import tempfile

wav_file = AudioSegment.from_file(file = "E:/Recording/2021/4-April/FNV-AmongUs/MONO-002.wav", 
                                  format = "wav") 
  
# Play the audio file
#play(wav_file)
'''
def _play_with_ffplay(wav_file):
    with NamedTemporaryFile("w+b", suffix=".wav") as f:
        fileName = f.name

    #seg.export(fileName, "wav")
    #subprocess.call([PLAYER, "-nodisp", "-autoexit", "-hide_banner", fileName])
    #os.remove(fileName)
'''

#silent_wav_file = wav_file - 5
play(wav_file)