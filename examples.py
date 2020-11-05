
from easylog import *

# log('Text to print to terminal and save to file') # Prints text inside parentheses to stream and to file. Same as print('Test to log'); print('Test to log', file=open('errors.log', 'a')).
# log('Text to print to terminal and save to file', file='custom_file.txt') # Same as log(), but prints to selected file. Inline file setting doesn't work with errors yet (if you set a different file, errors won't be logged to file). Use settings in easylog.py.
# log('Text to print to terminal and save to file with date', date=True) # Same as log() but with date of the function's call above the printed text.
# log('Text to print to terminal and save to file with date and custom end characters and separators', date=True, sep='   ', end='\n\n\n\n') # same arguments as in print(). Type help(print) to find out more.
# log('Text to print to terminal and save to file', date_format="%H:%M:%S"

# tg_log('Text to print to terminal, save to file and send to Telegram') # Same as log() but also sends value Telegram bot.
# tg_log('Text to print to terminal, save to file and send to Telegram', date=True) # Same as tg_log() but also adds date above.
# tg_log('Text to print to terminal, save to file and send to Telegram', date=True, file=False) # Same as tg_log() but won't print anything to file.
# tg_log('Text to print to terminal, save to file and send to Telegram', date=True, file=False, sep='   ', end='\n\n\n\n') # same arguments as in print(). Type help(print) to find out more.
# tg_log('Text to print to terminal, save to file and send to Telegram', date_format="%H:%M:%S") # Specified date format



# unlog(2) # Removes any number of lastly added log lines from the log file. Can accept file path as argument. But uses the default one. Without number specified it removes only 1 last line.
# clean_log_file() # Removes everything from the log file. Can accept file path as argument. But uses the default one.
# delete_log_file() # Deletes logging file completely withot a trace.  Can accept file path as argument. But uses the default one.


log(2)