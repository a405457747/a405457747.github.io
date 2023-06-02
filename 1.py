import os;
import  json;

def writeText(path,textContent,mode="w"):
    with open(path,mode,encoding='utf-8') as f:
        f.write(textContent);
def readText(path,mode='r'):
    with open(path,mode,encoding='utf-8') as f:
        return f.read();
def writeJson(path,obj):
    writeText(path,json.dumps(obj,indent=2));
def readJson(path):
    return json.loads(readText(path));











tempDict={
    'a':{
        'aa':{
            'ccc':[]
        }
    }
}

dict={};
dir="文章";
if __name__ == "__main__":
    for (root,dirs,files) in os.walk(dir, topdown=True):
        #print (root)
        pass;

    def traverseDir(filepath,action,exts=['.png','.md']):      

        files =os.listdir(filepath)

        if(filepath not in dict):
            dict[filepath]={};        
            
        for fi in files:
            fi_d =os.path.join(filepath,fi);
            if os.path.isdir(fi_d):
   
                print(fi_d);
                dict[filepath][fi_d]={};
                traverseDir(fi_d,action,exts)
            else:
                ext =os.path.splitext(fi_d)[1];
                if ext in exts and (action !=None):
                    #action(fi_d);
                    pass;
    traverseDir(dir,[],['.png','.md','.txt']);
    print(dict);