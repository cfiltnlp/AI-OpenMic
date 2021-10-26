# -*- coding: utf-8 -*-
"""ExtractAudioEmbeddings

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sE2UL7oaAY_I_c8GTmUszlK-o4Piqkss
"""

!pip install librosa

import librosa
import numpy as np
import glob, os

from google.colab import drive
drive.mount('/content/drive')

# convert wav to mp3  
!pip install pydub
from os import path
from pydub import AudioSegment
    
# files                                                                         
path = "/content/drive/Shareddrives/NLP_group/Project/Datasetv3/Ted-Audio" #path to folder containing mp3 files of audio
dst = "/content/drive/Shareddrives/NLP_group/Project/Datasetv3/Ted-Audio/wav/" #path to destination folder

filenames = glob.glob(os.path.join(path, '*.mp3'))
filenames = sorted(filenames)
for filename in filenames:
  print(filename)
  sound = AudioSegment.from_mp3(filename)
  name = filename.split('/')[-1]
  name = name.split('.')[0]
  name = dst + name + '.wav'
  print(name)
  sound.export(name, format="wav")

import os, glob
path = '/content/drive/Shareddrives/NLP_group/Project/Datasetv3/MutedAudio' #path to file containing laughter muted wav files
# path = '/content/drive/Shareddrives/NLP_group/Project/Datasetv3/Ted-Audio/wav'#path to file containing non funny wav files
path2 = '/content/drive/Shareddrives/NLP_group/Project/Datasetv3/audioembed/' #path to destination folder for audioembeddings
# path2 = '/content/drive/Shareddrives/NLP_group/Project/Datasetv3/GloveEmbed' 
counter = 0
max = 8000

filenames = glob.glob(os.path.join(path, '*.pkl'))
filenames = sorted(filenames)
for filename in filenames:
  print(filename)
  audio_data = filename
  x, sr  = librosa.load(audio_data)   #extract audio
  rms =  librosa.feature.rms(x)       #rms energy 1 feature
  mfccs = librosa.feature.mfcc(x, sr=sr)   #extracting MFCCs 20 features
  chromagram = librosa.feature.chroma_stft(x, sr=sr) #extracting Chromagram 12 features
  audiofeatures = np.concatenate((rms, mfccs, chromagram),axis =0) #concatenating all features 33 features
  # if np.shape(audiofeatures)[1] > 8000: #code to check if length of clip exceeds 8000
  #   print(filename)
  a = np.zeros((33, 8000 - np.shape(audiofeatures)[1])) #zero padding to lenght 8000
  audioembeddings = np.concatenate((audiofeatures, a), axis=1 )
  name = filename.split('/')[-1]
  name = name.split('.')[0]
  a_file = open(path2 + name + 'audioembed.txt', 'w') #save as a text file
  np.savetxt(a_file, audioembeddings) #write the feature embedding into file
  a_file.close()
  # if np.shape(audiofeatures)[1] > 8000: #code to check if length of clip exceeds 8000
  #   print(filename)
  counter += 1

print(counter) 
  # counter += 1
print(len(filenames))

#checking the shape of one file
t = np.loadtxt('/content/drive/Shareddrives/NLP_group/Project/Datasetv3/audioembed/AJ_TP_audio_01_mutedaudioembed.txt') 
print(np.shape(t))