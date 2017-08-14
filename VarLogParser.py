#/usr/bin/python
import os
from optparse import OptionParser

DEFAULT_FILENAME = 'messages'
DEFAULT_FREQUENCY = 'm'
DEFAULT_WINDOW = 't'

class ParseCommand:

    def __init__(self, options):
        self.filename = options.filename if options.filename else DEFAULT_FILENAME
        self.frequency = options.frequency if options.frequency else DEFAULT_FREQUENCY
        self.window = options.window if options.window else DEFAULT_WINDOW

    def run(self):
        pass



def main():
    usage = "usage: %prog [FREQUENCY]... [WINDOW]... [FILE]..."
    parser = OptionParser(usage=usage)
    parser.add_option("-q", dest="frequency", action="store_true", help="Frequency of grouping "
                                                                        "(eg. 'm' for minute or 'h' for hour) "
                                                                        "Default: m")
    parser.add_option("-w", dest="window", action="store_true", help="Window of time to analyze (eg. 'all' for entire"
                                                                     " log file, 'y' for yesterday, 't' for today,"
                                                                     " or an integer for number of days "
                                                                     " in the past (including today)) "
                                                                     "Default: t")
    parser.add_option("-f", dest="filename", action="store_true", help="The filename of the /var/log file. "
                                                                       "Default: messages (Linux) syslog (MAC OS)")

    options, args = parser.parse_args()
    print options
    print args

    p = ParseCommand(options)
    p.run()



if __name__ == '__main__':
    main()