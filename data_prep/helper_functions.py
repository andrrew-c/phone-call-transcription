import re
import pandas as pd

def parse_filename(fname, fext='m4a'):

    """ Return dictionary object with following aspects from filename
        date - INT in format YYYYMMDD
        time - INT in format HHMMSS
        pnumber - STR phone number of caller/callee

    """
    # Get date and time of call
    date = fname[2:10]
    time = fname[10:16]

    # Regex to extract a phone number from the filename
    pnumber_regex = re.compile(r'(?<=(0|1)d[0-9]{14}p)([+0-9]+|null)(?=.m4a)')

    # Search for phone number in string using regex
    srch = pnumber_regex.search(fname)

    # Return phone number (if matched, including null) else return None
    pnumber = srch.group() if srch != None else None

    return dict(date=date, time=time, pnumber=pnumber)


def get_all_files_info(files):

    # Columns
    #cols = ['filename', 'date', 'time', 'phonenumber']

    outfiles = []

    for file in files:
        outfiles.append(parse_filename(file))

    return pd.DataFrame(outfiles)