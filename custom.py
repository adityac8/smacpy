import os 
import subprocess
import pydub
dir_path = os.path.dirname(os.path.realpath(__file__))
print dir_path

##Create empty folder if not available
path='wavs'
if os.path.exists(path):
    print 'Folder bana hai'
    x=os.listdir(path)
    if x == []:
        print 'Folder khali h'
    else:
        print 'Folder mein {} subfolders h'.format(len(x))
#        print x
        for folder in x:
            new_path=path+'/'+folder
            print folder
            if os.path.isdir(new_path):
                y=os.listdir(new_path)
                if y == []:
                    print 'Empty subfolder:',folder
                else:
                    print '{} files in {} folder'.format(len(y),folder)
#                    print y
                    for file_ in y:
                        filex=file_.replace("_","x")
                        print file_
                        os.rename(new_path+'/'+file_,path+'/'+folder+'_'+filex)
                        if not os.listdir(new_path):
                            os.rmdir(new_path)
            else:
                print 'File mili'
#        x=os.listdir(path)
        i=1
        for files in x:
            if(files[-4:]==".mp3"):
                sound = pydub.AudioSegment.from_mp3(path+'/'+files)
                sound.export(path+'/'+files[:-4]+'.wav', format="wav")
#                os.rmdir(files)
#            subprocess.call(['sox', files, '-e', 'mu-law','-r', '16k', files[:-4]+'.wav', 'remix', '1,2'])
#            print "Old {} New {}".format(files,files[:-4]+'.wav')
#            subprocess.call(['ffmpeg', '-i', files,files[:-4]+'.wav'])
#            i+=1
#            if i==4:
#                break
                

            
    
else:
    os.makedirs('wavs')
    print 'Empty folder named wavs created'
    print 'Data dalo chacha in wavs folder'