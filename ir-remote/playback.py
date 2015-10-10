import lirc

sock_id = lirc.init("playback")

def print_it(command):
    print "Rceived command %s"%(command)

g_keypress_mappings = {
    "vol_down" : print_it,
    "vol_up"   : print_it,
    "play_pause": print_it,
    "next" : print_it,
    "previous": print_it
    }

def main():
    loop = True
    try:
        while loop:
            code = lirc.nextcode()
            if len(code) == 0:
                continue

            if code[0] in g_keypress_mappings:
                g_keypress_mappings[code[0]](code[0])
            else:
                print "Unknown command %s"%(code[0])
    except KeyboardInterrupt:
        print "Received keyboard interrupt..."
    finally:
        lirc.deinit() # free up resources

if "__main__" == __name__:
    main()
	
