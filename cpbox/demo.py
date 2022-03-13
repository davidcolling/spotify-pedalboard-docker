import inspect
import soundfile as sf
from pedalboard import (
    Pedalboard,
    Convolution,
    Compressor,
    Chorus,
    Gain,
    Reverb,
    Limiter,
    LadderFilter,
    Phaser,
)

audio, sample_rate = sf.read('input.wav')

# Make a Pedalboard object, containing multiple plugins:
# found with inspect.signature(Phaser()): <pedalboard.Phaser rate_hz=1 depth=0.5 centre_frequency_hz=1300 feedback=0 mix=0.5 at 0x2cdb970>
board = Pedalboard([
    Phaser(rate_hz=1, mix=1.0, feedback=0.5)
], sample_rate=sample_rate)

# Run the audio through this pedalboard!
effected = board(audio)

# Write the audio back as a wav file:
with sf.SoundFile('./output.wav', 'w', samplerate=sample_rate, channels=len(effected.shape)) as f:
    f.write(effected)

