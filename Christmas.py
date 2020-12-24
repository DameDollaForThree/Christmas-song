# Example: Sound

from wave import open
from struct import Struct
from math import floor

frame_rate = 11025

def encode(x):
    """Encode float x between -1 and 1 as two bytes.
    (See https://docs.python.org/3/library/struct.html)
    """
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name='Christmas.wav', seconds=13):
    """Write the output of a sampler function as a wav file.
    (See https://docs.python.org/3/library/wave.html)
    """
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()

def tri(frequency, amplitude=0.3):
    """A continuous triangle wave."""
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler

def note(f, start, end, fade=.01):
    """Play f for a fixed duration."""
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler


def both(f, g):
    """a helper function that enables us to create a song"""
    return lambda t: f(t) + g(t)


"""Let's create some notes"""
c_freq, e_freq, g_freq = 261.63, 329.63, 392.00
c = tri(c_freq)
e = tri(e_freq)
g = tri(g_freq)

d_freq, f_freq, a_freq, b_freq = 293.66, 349.23, 440, 466.16
d = tri(d_freq)
f = tri(f_freq)
a = tri(a_freq)
b = tri(b_freq)

low_g_freq, low_b_freq, sharp_f_freq = 196, 246.94, 369.99
low_g = tri(low_g_freq)
low_b = tri(low_b_freq)
sharp_f = tri(sharp_f_freq)

sharp_c_freq, flat_e_freq, flat_b_freq = 277.18, 311.13, 466.16
sharp_c = tri(sharp_c_freq)
flat_e = tri(flat_e_freq)
flat_b = tri(flat_b_freq)

  # Merry Christmas!!!
  #             *
  #           * * *
  #         * * * * *
  #       * * * * * * *
  #     * * * * * * * * *
  #   * * * * * * * * * * *
  # * * * * * * * * * * * * *
  #             *
  #           * * *
  #         * * * * *
  #       * * * * * * *
  #     * * * * * * * * *
  #   * * * * * * * * * * *
  # * * * * * * * * * * * * *
  #           * * *
  #           * * *
  #           * * *
  #           * * *
  #           * * *
  #           * * *
  #           * * *

def Xmas(c, d, e, f, g, a, b, low_g, low_b, sharp_f, sharp_c, flat_e, flat_b):
    z = 0
    song = note(low_g, z, z + 1/4)
    z += 2/5
    song = both(song, note(low_b, z, z + 1/5))
    z += 1/4
    song = both(song, note(d, z, z + 1/4))
    z += 2/5
    song = both(song, note(sharp_f, z, z + 1/4))
    z += 2/5
    song = both(song, note(g, z, z + 1/4))
    z += 2/5
    song = both(song, note(sharp_f, z, z + 1/4))
    z += 2/5
    song = both(song, note(e, z, z + 1/4))
    z += 2/5
    song = both(song, note(d, z, z + 1/4))

    z += 3/5
    song = both(song, note(a, z, z + 1/4))
    z += 2/5
    song = both(song, note(g, z, z + 1/5))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 2/5
    song = both(song, note(sharp_f, z, z + 1/4))
    z += 2/5
    song = both(song, note(g, z, z + 1/4))
    z += 2/5
    song = both(song, note(sharp_f, z, z + 1/4))
    z += 2/5
    song = both(song, note(e, z, z + 1/4))
    z += 2/5
    song = both(song, note(d, z, z + 1/4))

    z += 3/5
    song = both(song, note(sharp_c, z, z + 1/4))
    z += 2/5
    song = both(song, note(e, z, z + 1/5))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 2/5
    song = both(song, note(a, z, z + 1/4))
    z += 2/5
    song = both(song, note(b, z, z + 1/4))
    z += 2/5
    song = both(song, note(a, z, z + 1/4))
    z += 2/5
    song = both(song, note(g, z, z + 1/4))
    z += 2/5
    song = both(song, note(e, z, z + 1/4))

    z += 3/5
    song = both(song, note(c, z, z + 1/4))
    z += 2/5
    song = both(song, note(flat_e, z, z + 1/5))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 2/5
    song = both(song, note(a, z, z + 1/4))
    z += 2/5
    song = both(song, note(flat_b, z, z + 1/4))
    z += 2/5
    song = both(song, note(a, z, z + 1/4))
    z += 2/5
    song = both(song, note(f, z, z + 1/4))
    z += 2/5
    song = both(song, note(flat_e, z, z + 1/4))

    return song

def Xmas_at(octave):
    c = tri(octave * c_freq)
    d = tri(octave * d_freq)
    e = tri(octave * e_freq)
    f = tri(octave * f_freq)
    g = tri(octave * g_freq)
    a = tri(octave * a_freq)
    b = tri(octave * b_freq)
    low_g = tri(octave * low_g_freq)
    low_b = tri(octave * low_b_freq)
    sharp_f = tri(octave * sharp_f_freq)
    sharp_c = tri(octave * sharp_c_freq)
    flat_e = tri(octave * flat_e_freq)
    flat_b = tri(octave * flat_b_freq)
    return Xmas(c, d, e, f, g, a, b, low_g, low_b, sharp_f, sharp_c, flat_e, flat_b)

play(both(Xmas_at(1), Xmas_at(1/2)))
