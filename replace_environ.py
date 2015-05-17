import os
import os.path
def replace_config(file_name):
    f=open(file_name,'r')
    content=f.read()
    for e in os.environ:
        content=content.replace('$'+e,os.environ[e])
    f.close()
    f2=open(file_name.split('.template')[0],'w')
    f2.write(content)
    f2.close()
def replace_folders(parent):
    subdirs=[os.path.join(parent,o) for o in os.listdir(parent) if os.path.isdir(os.path.join(parent,o))]
    print subdirs
    for s in subdirs:
        files=[os.path.join(s,o) for o in os.listdir(s) if not os.path.isdir(os.path.join(s,o)) and o.endswith('.template')]
        for f in files:
            print "replacing file:",f
            replace_config(f)
    
if __name__=='__main__':
    replace_folders('/templates')
