#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Handy Random Functions""" 


# In[2]:


#Classes


# In[3]:


class color:
    """
    For Color
    Works Same as colorama
    """
    RED = '\x1b[31m'
    LIGHTRED_EX = '\x1b[91m'
    BLUE = '\x1b[34m'
    LIGHTBLUE_EX = '\x1b[94m'
    BLACK = '\x1b[30m'
    LIGHTBLACK_EX = '\x1b[90m'
    CYAN = '\x1b[36m'
    LIGHTCYAN_EX = '\x1b[96m'
    GREEN = '\x1b[32m'
    LIGHTGREEN_EX = '\x1b[92m'
    MAGENTA = '\x1b[35m'
    LIGHTMAGENTA_EX = '\x1b[95m'
    YELLOW = '\x1b[33m'
    LIGHTYELLOW_EX = '\x1b[93m'
    WHITE = '\x1b[37m'
    LIGHTWHITE_EX = '\x1b[97m'
    RESET = '\x1b[39m'


# In[4]:


class Card_make:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
                'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# In[5]:


#Dictionarys


# In[6]:


#For Color
Fore = color()
alpha_color_dict = {'red':Fore.RED ,
             'light_red':Fore.LIGHTRED_EX ,
             'blue':Fore.BLUE ,
             'light_blue':Fore.LIGHTBLUE_EX ,
             'black':Fore.BLACK ,
             'light_black':Fore.LIGHTBLACK_EX ,
             'cyan':Fore.CYAN ,
             'light_cyan':Fore.LIGHTCYAN_EX ,
             'green':Fore.GREEN ,
             'light_green':Fore.LIGHTGREEN_EX ,
             'magenta':Fore.MAGENTA ,
             'light_magenta':Fore.LIGHTMAGENTA_EX ,
             'yellow':Fore.YELLOW ,
             'light_yellow':Fore.LIGHTYELLOW_EX ,
             'white':Fore.WHITE ,
             'light_white':Fore.LIGHTWHITE_EX ,
             'reset':Fore.RESET
             
             }


# In[7]:


#For alpha to num
alpha_num_dict = {
                  " ":0 ,
                  "a":1 ,
                  "b":2 ,
                  "c":3 ,
                  "d":4 ,
                  "e":5 ,
                  "f":6 ,
                  "g":7 ,
                  "h":8 ,
                  "i":9 ,
                  "j":10 ,
                  "k":11 ,
                  "l":12 ,
                  "m":13 ,
                  "n":14 ,
                  "o":15 ,
                  'p':16,
                  'q':17,
                  'r':18,
                  's':19,
                  't':20,
                  'u':21,
                  'v':22,
                  'w':23,
                  'x':24,
                  'y':25,
                  'z':26}


# In[8]:


numdict = {'Zero':0,'One':1,'Two':2,'Three':3,'Four':4,'Five':5,
           'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Eleven':11,
           'Twelve':12,'Thirteen':13,'Fourteen':14,'Fifteen':15,'Sixteen':16,
           'Seventeen':17,'Eighteen':18,'Nineteen':19,'Twenty':20,'Thirty':30,
           'Fourty':40,'Fifty':50,'Sixty':60,'Seventy':70,'Eighty':80,'Ninety':90,
           'Hundred':100,'Thousand':1000,'Million':1000000,'Billion':1000000000,'Trillion':100000000000}


# In[9]:


#Functions


# In[10]:


def strnum(num):
    """
    num --> int/str
    
    reverse is automatic
    
    convert num to number name
    up to 100
    """
    
    #Making reverse 
    if type(num) == type(int()):
        num = int(num)
        reverse = False
    elif type(num) == type(str()):
        reverse = True
    else: #In case of error
        print("Num can only be int/str")
        return False
    
    #Atcual code
    if not reverse:
        #No need for extra step
        if num in numdict.values():
            return list(numdict.keys()) [list(numdict.values()).index(num)]
        #If need for calculation
        else:
            t = round(num - 5,-1)
            o = num - t 
            ts = list(numdict.keys()) [list(numdict.values()).index(t)]
            os = list(numdict.keys()) [list(numdict.values()).index(o)]
            return ts + '-' + os
    
    else:
        #No need for extra step
        if num in numdict:
            return numdict[num]

        #If need for calculation
        else: 
            t,o = num.split('-')
            tn = numdict[t]
            on = numdict[o]
            return tn + on


# In[11]:


def convert_color(name,reverse = False):
    """
    Converts Color names to Colorama Fore Colors 
    and vice versa
    """
    
    #If want color name to ascii escape 
    if not reverse:
        return alpha_color_dict[name.lower()]
    
    #Vice versa
    else: 
        return list(alpha_color_dict.keys()) [list(alpha_color_dict.values()).index(name)]


# In[12]:


def Convert_Bool(x,z = None):
    """
    convert/numertical str to bool
    """
    if x.upper() == 'TRUE' or x == True or x == 1 or 'T' in x.upper() or x == z:
        return True
    else:
        return False


# In[13]:


def Convert_AlphaNum(x,reverse = False):
    """
    convert alphabet to number
    """
    if not reverse:
        return alpha_num_dict[x.lower()]
    else:
        return list(alpha_num_dict.keys()) [list(alpha_num_dict.values()).index(x)]


# In[14]:


def encode(x,reverse = False, seed = 31):
    """
    Encodes String and digits
    """
    seed = seed + 0.5
    #For digit
    if type(x) == type(9) or type(x)==type(9.0) :
        if not reverse:
            return float (str( x + seed)[::-1])
        else:
            return float(str(x)[::-1]) - seed
    
    #For String
    elif type(x) == type(' '):
        if not reverse:
            y = [Convert_AlphaNum(i) for i in x]
            z = str([str(i + 2)[::-1] for i in y])
            z = z.strip('[]').replace(',','').replace("'",'')
            return z
        else:
            print(x)
            x = x.split()
            y = [ (int(str(i)[::-1])) - 2 for i in x ]
            z = str([Convert_AlphaNum(i,True) for i in y])
            z = z.strip('[]').replace(', ','').replace("'",'')
            return z
    
    #If It is not that
    else:
        print('Str or Digit')


# In[15]:


def match_input(target,msg ,infi = True,og_inp = None, details = True):
    """
    target --> list
    msg --> str
    infi --> bool
    details --> bool
    
    target is the target input
    msg is the msg u want to put
    inp is input
    infi is while continue
    details returns a dict of details
    """

    def match_input_tru():
        
        if og_inp == None:
            inp = input(msg)
        else: pass
        
        if inp in target:
            return {'result':True,'inp':inp,'msg':msg,'target':target}
        else:
            return {'result':False,'inp':inp,'msg':msg,'target':target}

    if infi:
        result = False
        while not result:
            otp = match_input_tru() 
            result = otp['result']
    else:
        otp = match_input_tru()
        
    if details:
        return otp
    else:
        return otp['result']


# In[16]:


def strlist(lis,nl = False,sp = False):
    """
    converts list to pure str
    lis --> list
    nl --> bool
        nl adds new line after each elem
    sp --> bool
        sp adds space after each elem 
    """
    
    ns = ''
    for i in lis:
        i = str(i)
        if sp:
            ns += ' '
        else:
            pass
        if nl:
            ns+=f'\n{i}'
        else:
            ns += i
        
    return ns.strip()


# In[17]:


def trycall(y,*args,**kwargs):
    """
    return called value if y, 
    if not callable returns y
    """

    if callable(y):
        return y(*args,**kwargs)
    else:
        return y



# In[18]:


def ifret(retx,condition,false_ret = '',*args,**kwargs):
    """
    returns retx if condition is True
    else returns empty string 
    
    inp = input for condition if lambda or func
    false_ret = what to return if false
    
    args and kwargs are for condition
    """
   
    def cond(y):
        """
        to check if y is calllable
        """
        
        if callable(y):
            return y(*args,**kwargs)
        else:
            return y
        
    if cond(condition):
        return cond(retx)
    else:
        return cond(false_ret)

