from HelperFunctions import *
from moviepy.editor import VideoFileClip  # Mosy efficient but you need to specify everything from moviepy that you are using

from tkinter import *
from tkinter import scrolledtext
def main ():

    TimeStampDelta = 0
    #TimeStampDelta = (-4)
    TimeExtension = 2
    exttime = 0

    VideoFileName = TextEntry1.get()
    parserDataFilePath = TextEntry2.get()
    subclipFolder =  TextEntry3.get()

    TimeStamps = readFile(parserDataFilePath)
    Segment = VideoFileClip(VideoFileName)
    print("Parsing Timestamp: " + TimeStamps[0]) #Insert the response
    SecondsStart = GetSecondsBasedOnTimeStamp(GetStartTimestampFromIndex(TimeStamps, 0))
    SecondsEnd = GetSecondsBasedOnTimeStamp(GetEndTimestampFromIndex(TimeStamps, 0))
    InitialSegmentToAdd = Segment.subclip(SecondsStart+TimeStampDelta-TimeExtension, SecondsEnd+TimeStampDelta+TimeExtension)
    InitialSegmentToAdd.write_videofile(subclipFolder+"Clip0.mp4", temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")
    
    #FinalClip = InitialSegmentToAdd

    i=1
    while(TimeStamps[i]!=''):
        print("Parsing Timestamp: " + TimeStamps[i]) #Insert the response
        SecondsStart = GetSecondsBasedOnTimeStamp(GetStartTimestampFromIndex(TimeStamps, i))
        SecondsEnd = GetSecondsBasedOnTimeStamp(GetEndTimestampFromIndex(TimeStamps, i))
        SegmentToAdd = Segment.subclip(SecondsStart+TimeStampDelta-TimeExtension, SecondsEnd+TimeStampDelta+TimeExtension+exttime)
        SegmentToAdd.write_videofile(subclipFolder+"Clip"+str(i)+".mp4", temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")
        #FinalClip = concatenate_videoclips([FinalClip, SegmentToAdd])
        i+=1

    #FinalClip.write_videofile(OutputFileName, temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")

VideoFileName = "D:\kurtYoutube\Video9\\2022-08-2212-00-54Trim.mp4"
parserDataFilePath = "D:\kurtYoutube\Video9\Timestamps.txt"
subclipFolder = "D:\kurtYoutube\Video8\Subclips\\"


window= Tk()
window.title("Kurt's Video Parser")

Label (window, text="Video File Path", fg="black", font="none 16 bold") .grid(row=1, column=0)
TextEntry1 = Entry(window, width=150, bg="white",text="DEGREE FAHRENHEIT")
TextEntry1.insert(0, VideoFileName)
TextEntry1.grid(row=1,column=1)
Label (window, text="Timestamp File Path", fg="black", font="none 16 bold") .grid(row=2, column=0)
TextEntry2 = Entry(window, width=150, bg="white")
TextEntry2.insert(0, parserDataFilePath)
TextEntry2.grid(row=2,column=1)
Label (window, text="Subclip Folder Path", fg="black", font="none 16 bold") .grid(row=3, column=0)
TextEntry3 = Entry(window, width=150, bg="white")
TextEntry3.insert(0, subclipFolder)
TextEntry3.grid(row=3,column=1)

outputText = scrolledtext.ScrolledText(window)
outputText.grid(row = 5, column = 0, columnspan = 2)



Button(window, text="Run", width=30, command=main) .grid(row=4,column=0)

window.mainloop()

#VideoFileName = "D:\kurtYoutube\Python\VideoFiles\KurtsSundayMillionRunP1.mp4"
#OutputFileName = "KurtsSundayMillionRunFinalFirstCut1.mp4"



