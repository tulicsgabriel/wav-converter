# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:07:48 2021

@author: MIKLOS
"""

import os
import glob
import librosa
import soundfile
from pydub import AudioSegment, effects

import parselmouth

# import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns


NEW_FS = 16000
INPUT_DIR = './Input/'
OUTPUT_DIR = './Output/'


def loop_to_convert():
    """ Loops through the Input directory, reads wav file with 16 kHz with
    librosa, prints filename and new sample rate (fs) and calls the function
    to save the new wav file.

    Returns
    -------
    None.

    """
    for filen_path in glob.glob(os.path.join(INPUT_DIR, '*.wav')):
        data, fs_ = librosa.load(filen_path, NEW_FS)
        base = os.path.basename(filen_path)
        print("Wav filename: {}, fs: {}".format(base, fs_))
        save_as_mono_16khz(data, base)


def save_as_mono_16khz(data, wav_filename):
    """ Save wav with soundfile in Output dir as mono, 16 kHz and 16 bit
    linear quantization.

    Parameters
    ----------
    data : array
        wav file.
    wav_filename : string
        name of the wav file.

    Returns
    -------
    None.

    """
    new_wav_filename = OUTPUT_DIR + wav_filename
    soundfile.write(new_wav_filename, data, NEW_FS, subtype='PCM_16')


def normalize_output_wavs():
    """ Normalize wav file to peak amplitude with pydub.

    """
    for file_path in glob.glob(os.path.join(OUTPUT_DIR, '*.wav')):
        # plot_wav(filen_path)
        raw_wav = AudioSegment.from_file(file_path, "wav")
        print("Normalizing: {}".format(file_path))
        normalized_wav = effects.normalize(raw_wav)
        normalized_wav.export(file_path, format="wav")
        # plot_wav(filen_path)


def plot_wav(file_path):
    """ Plot wav to check effect of normalization with Parselmouth.
    Parselmouth is doing Praat in Python, the Pythonic way.
    """
    snd = parselmouth.Sound(file_path)
    plt.figure()
    plt.plot(snd.xs(), snd.values.T)
    plt.xlim([snd.xmin, snd.xmax])
    plt.xlabel("--> time [s]")
    plt.ylabel("--> amplitude")
    plt.show()


def main():
    """ Main loop
    """
    loop_to_convert()
    normalize_output_wavs()


if __name__ == '__main__':
    main()
