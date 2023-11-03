from pydub import AudioSegment

def flac_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file, format="flac")
    audio.export(output_file, format="wav")

# Example usage
input_file = "/Users/macbookpro/Documents/Samples/Insect Sounds/678349__msx2plus__insects-and-rain-at-night-seamless.flac"
output_file = "/Users/macbookpro/Documents/Samples/Insect Sounds/678349__msx2plus__insects-and-rain-at-night-seamless.wav"

flac_to_wav(input_file, output_file)
