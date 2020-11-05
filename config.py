
"""
Seetings you should configure to your liking before using this library.
"""
file = 'logs.log' # Set file to log to.
errors_file = 'errors.log' # Set the file to send errors to.
date = False # Ddd date by default to all log messages.
telegram_date = True # dd date to your telegram messages.
date_format='%d.%m.%y – %H:%M:%S'
errors_to_telegram = True


autoformat_prints_to_terminal = True
lines_between_prints = 1 # adds 1 line of free space for better readibiliy

remove_errors_file_after_creation = True # errors will go to general log file anyways, but you can opt-out of deleting the initial log file.
