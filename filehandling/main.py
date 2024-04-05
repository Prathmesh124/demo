asr=open("C:\\New folder\\v1.mp4","rb")
newimg=open("C:\\transfer\\v1new.mp4","wb")
data=asr.readlines()
newimg.writelines(data)
print(data)
newimg.close
asr.close