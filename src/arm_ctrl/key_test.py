
import sys, select, termios, tty

msg = """
base rotation clk_wise--- 'q'
base rotation anti_clk_wise--- 'z'
link one forward --- 'w'
link one backward --- 'x'
link two forward --- 'e'
link two backward --- 'c'
link three forward --- 'r'
link three backward --- 'v'
gripper clk_wise--- 't'
gripper anti_clk_wise--- 'b'
gripper open ---'y'
gripper close ---'n'
all stop ---'s'
"""

moveBindings = { 'q','z','w','x','e','c','r','v','t','b','y','n','s'
    }


def getKey(key_timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


if __name__=="__main__":
    	settings = termios.tcgetattr(sys.stdin)
    	key_timeout = None

        print(msg)

        while(1):
            key = getKey(key_timeout)
            if key in moveBindings:
               if key == 'q':
         
            else:
                
                if key == '' and x == 0 and y == 0 and z == 0 and th == 0:
                    continue
                if (key == '\x03'):
                    break


