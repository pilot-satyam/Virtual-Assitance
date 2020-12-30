#!/usr/bin/env python
# coding: utf-8

# In[1]:
from __future__ import print_function

import speech_recognition as sr

 
# In[ ]:


import os


# In[ ]:


from gtts import gTTS


# In[ ]:

import datetime


# In[ ]:


import warnings


# In[ ]:


import calendra


# In[ ]:


import random


# In[ ]:


import wikipedia  


# In[ ]:


warnings.filterwarnings('ignore')


# In[2]:

#record audio and return it as a string
def recordAudio():
    #record the audio
    r=sr.Recognizer() #creating a recognizer object
    #open the microphone and start recording
    with sr.Microphone() as source:
        print('say something')
        audio= r.listen(source)
    data=''
    try:
        data=r.recognize_google(audio)
        print('You said:'+data)
    except sr.UnknownValueError:
        print('Google speech recognition could not understand audio,unknown error')
    except sr.RequestError as e:
        print('Request results from Google speech Recognition service error'+e)
    return data   


# In[4]:

#function to get viortual assistance response
def assistResponse(text):
    print(text)
    #convert text to speech
    myobj=gTTS(text=text,lang='en',slow=True)
    myobj.save('assistant_response.mp3')
    #play the converted file
    os.system('start assistant_response.mp3')
    


# In[ ]:


def wakeword(text):
    ww=['hey assist','okay assist','good morning assist','good evening assist','listen assist']
    text=text.lower()
    #check to see if user command contains a wake word
    for phrase in ww:
        if phrase in text:
            return True
            #if the wake word isn't found in text from the loop 
    return False




# In[ ]:
import calendar
# a function to get the current date
def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday= calendar.day_name[my_date.weekday()]
    monthNum=now.month
    dayNum=now.day
    mn=['January','February','March','April','May','June','July','August','September','October','November','December']
    on=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']
    return 'Today is'+weekday+' '+mn[monthNum-1]+' the '+on[dayNum-1]+'. '


# In[ ]:

# afunction to return a random response
def greeting(text):
    #greeting inputs
    gi=['hi','hey','hello','hey there','wassup','hola']
    #greeting returns
    gr=['howdy doc','whats gooddoc','hello doc','hey there doc']
    for word in text.split():
        if word.lower() in gi:
            return random.choice(gr)+'.'
    return ''   
    #a function to get a persons first and last names from the text
def getPerson(text):
    wl=text.split()
    for i in range(0,len(wl)):
        if i + 3 <=len(wl)-1 and wl[i].lower()=='who' and wl[i+1].lower()=='is':
            return wl[i+2]+' '+wl[i+3]     
while True:
    #record the audio
    text=recordAudio()
    response=''
    #check for wake phrase

    if(wakeword(text) == True): 
        response=response+greeting(text)
        if ('date' in text):
            get_date=getDate()
            response=response+ ''+get_date
            #check to see user says who is
        import wikipedia
        if ('who is' in text):
            person=getPerson(text)
            wiki = wikipedia.summary(person)
            response = response+' '+wiki
            
 #have the assistant respond back using audio and text from response
assistResponse(response)

import pyzbar.pyzbar as pyzbar
import numpy as np
from cv2 import cv2

def decode(im) : 
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)

  # Print results
  for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')
    
  return decodedObjects


# Display barcode and QR code location  
def display(im, decodedObjects):

  # Loop over all decoded objects
  for decodedObject in decodedObjects: 
    points = decodedObject.polygon

    # If the points do not form a quad, find convex hull
    if len(points) > 4 : 
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else : 
      hull = points
    
    # Number of points in the convex hull
    n = len(hull)

    # Draw the convext hull
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)

  # Display results 
  cv2.imshow("Results", im)
  cv2.waitKey(0)

  
# Main 
if __name__ == '__main__':

  # Read image
  im = cv2.imread('be.png')

  decodedObjects = decode(im)
  display(im, decodedObjects)


            
    
    

