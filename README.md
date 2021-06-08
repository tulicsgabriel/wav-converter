# wav-converter
# Resample wav files easaly with just a few lines of code 


<div id="container"> <img src='plot.png' alt="banner"></img>
</div>

#container {
    height:100px;
    line-height:100px;
}

#container img {
    vertical-align:middle;
    max-height:100%;
}

The script loops through an Input directory, reads wav file with 16 kHz with **librosa**, prints filename and new sample rate (fs) and save wav file with **soundfile** in the Output dir as mono wav file with 16 kHz and 16 bit linear quantization.

Extra step: Normalize wav file to peak amplitude with **pydub**.
You can also do a simple plot reading the wav file with **Parselmouth**, which is a Praat library in Python.
