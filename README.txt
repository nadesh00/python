i designed this macchanger specifically to work with unix shell .



# python
contains python ETH tools 

two modules are used 
 optparser                 https://docs.python.org/3/library/optparse.html
 subprocess                https://docs.python.org/3/library/subprocess.html
 
 using the self made function macchanger()
  we are parsing two parameters "interface" and "new mac" address to the function

--help displays 

Usage: macchanger.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        set interface using this flag
  -m MAC_ADDRESS, --mac=MAC_ADDRESS
                        set the new mac address

// the optparse is deprecated after python3.2 

now it uses "argparse" module  https://docs.python.org/3/library/argparse.html
   
