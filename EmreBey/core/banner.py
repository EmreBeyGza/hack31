#! /usr/bin/env python2.7
# core the Optivaframework  
import os
import sys
import time
import random
from termcolor import colored, cprint

def Banner():

	bn1 = colored(''' \033[91m	
                                            |||
    _                                __     |L|
---' |    _                        <'__`)   |||__________
/  : |  -'               ( (  --    )- \\   |/__________/
/  : |   ---         ((( -  ---     \__;`               |
/  : |  -._         (  --        _-'/:_\                |
---._|     __               \|,-' _// ( \|              |
___\_               ( ---- `{)_--'//  | ||]             |
_____]_[~~-_                '    (.L_/  ||              |
____________]         .        _-' `\_,/'/              |
        |||    ( ---  |\_---''/  ,___,'./               |
        |||      ((-- |_\____/ ,'______|                |
        |||                 / / I==||                   |
        |||       ( - -  __/_/   __||__                 |
---------++-------------`-._/---o--o---o----------------+ 
		''',)

	bn2 = colored('''                         
                 _          __               
          ,-----' |   _   <'__`)              
          | //  : | -'     )o \\          
          | //  : |  ---   \__;`          
          | //  : | -._      |\`\            
          `-----._|     __  // ( \|          
           _/___\_    //)_`//  | ||]           
     _____[_______]_[~~-_ (.L_/  ||
    [____________________]' `\_,/'/
      ||| /          |||  ,___,'./
      ||| \          |||,'______|
      ||| /          /|| I==||
      ||| \       __/_||  __||__
  -----||-/------`-._/||-o--o---o---                     
    ~~~~~'	
			''', 'yellow')

	bn3 = colored('''\033[92m 
  \033[92m  Optiva.py! \033[27m   
   -----------                
      \                
       \   \033[1;31m,__,\033[1;m             
        \  \033[1;31m(\033[1;moo\033[1;31m)____\033[1;m       
           \033[1;31m(__)    )\ \033[1;m    
           \033[1;31m   ||--|| \033[1;m\033[05m*\033[25m\033[1;m [ Optivaframework |                                                                                        
                                                 ''',)   
                                  
	bou = [bn1, bn2, bn3]
	const = bou[random.randint(0, 2)] 
	print const


