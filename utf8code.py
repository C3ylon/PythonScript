import os,sys  

Original_Encoding = "gbk"
Output_Encoding = "utf-8"

def convert( filename):   
    try:
        with open(filename, "r", encoding = Original_Encoding) as fp:
            data = ""
            for line in fp:
                data += line
        data = data.encode(Output_Encoding)
        with open(filename, "wb") as fp:
            fp.write(data)
        print("[+]" + filename, "done") 
    except:
        print("[!]can't open",filename)
  
def explore(dir):  
    for root, dirs, files in os.walk(dir):  
        for file in files:  
            path = os.path.join(root, file)  
            convert(path)  
  
def main():  
    for path in sys.argv[1:]:  
        if os.path.isfile(path):  
            convert(path)  
        elif os.path.isdir(path):  
            explore(path)  
  
if __name__ == "__main__":  
    main() 
