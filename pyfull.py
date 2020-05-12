import time

def function_timer(orgfunc):
    def wrapper_timer(*args, **kwargs):
        print("Before function {} was run".format(orgfunc.__name__))
        t = time.time()
        orgfunc(*args, **kwargs)
        print("{} took {}s to run".format(orgfunc.__name__, time.time()-t))
    return wrapper_timer


def file_to_list(filename, spliter):
    if type(spliter) != str:
       raise TypeError("spliter is not of type string") 
    try:
        with open(filename,'r') as file:
            content = file.read().split(spliter)
            return content
    except FileNotFoundError:
        raise FileNotFoundError("File Does not exist")


def list_to_file(filename, ls, spliter):
    if type(spliter) != str:
       raise TypeError("spliter is not of type string")
                       
    with open(filename,"w+") as file:
        output_string = ""
        for item in ls:
            output_string+=str(item)+spliter
        file.write(output_string.rstrip(spliter[len(spliter)::-1]))


def str_to_ordlist(sr):
    ls = []
    if type(sr) != str:
        raise TypeError("Function not provided the correct type. Provide a string as an argument")
    i = 0
    while i < len(sr):
        ls.append(ord(sr[i]))
        i+=1
    return ls


#Returns a String from 
def ordlist_to_str(ls):
    i = 0
    prd = ""
    if type(ls) != list:
        raise TypeError('Type Error. Please provide an array as an argument')
    i = 0
    while i < len(ls):
        try:
            prd+=chr(int(ls[i]))
            i+=1
        except:
            raise TypeError('Type Error. Item at index {} is not an integer and/or cannot be converted into a integer'.format(i))
    return prd


    
if __name__ == "__main__":
    print("Pyful Version 1.2")
    #Testing
