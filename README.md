test text!

# Requirements:
For Telegram logging: pip install pyTelegramBotAPI==0.3.0 . But you don't need to install it unless you wish to log something to Telegram.

# Description:
download easylog.py to your project's directory; then write:
from easylog import *

## log() – acts as print() but also adds everything to the file specified here or to argument file as string like print('Content', file='stream.txt').
optional arguments except file:
- date (True or False) – allows to add date to stream output and toi file at the beginning of a record.
- mode – any mode of the file to write. Appending by default. Recommended against changing, but who knows what your edge cases are.

## clean_log_file() – removes everything from the log file. Can accept file path as argument. But uses the default one.
## delete_log_file() – deletes logging file completely withot a trace.  Can accept file path as argument. But uses the default one.

## unlog(n) – removes any number of lastly added log lines from the log file. Can accept file path as argument. But uses the default one. Without number specified it removes only 1 last line.

## tg_log() – adds logging to your Telegram bot. Acts as log. Accepts same arguments as log(). file – may be False.

You can send Traceback errors to Telegram.
You can add any amount of line breaks to improve readability!
Files are always flushed after each log() and tg_log() (meaning they're updated).

**Developer: telegram: @kopyl** . U're welcome to propose suggestions and both subjectively and objectively critisize me in the DM.
Spend around 5 hours to develop this solution.
Мам, я покушал.

# Known issues I don't know yet how to solve:
- Setting custom file doesn't work as expected as from example here: tg_log('New text', date=True, file='filex.txt') . Text is logging to custom files but errors are ignored.

# Yes, this also works:
list = [1,2,3,4]
log(list)
log(range(13))






# Added in v1.1:
- log(*range(13))
- log("hey","dear","world")
- log(1,2,4, sep="_", end='        ') # Same optional arguments as in print().
- Turned out files are always flushed after each log() and tg_log(). Feature, not a bug.
- You can add any amount of line breaks to improve readability!
- Mentioned about "send errors to Telegram" feature in the easylog.py file.

# Added in v1.2:
**Improvements:**
- Switched to better namings
- Docstrings are insterted the right way accordingly to PEP 257.
- Removed redundant function in the logic and made it much more correct
- Added more white space and made it more consistent to improve readibility.
- Added more flexibility and scalibiliy to the code.
**New features:**
- Option to easily specify errors file and.
- Option to choose whether to delete errors file on creation.

# Added in v1.3:
- Put all settings to a separate config file.
- Put all documentation to README.md file.
- Date format as an optional argument or config setting. Same as strfitime. May be set in settings or as argument.
- I realized that date for is redundant since there is always timestampt of the received message in Telegram. So i disabled it by default. But there may be cases where you may need seconds to be logged to your telegram, so i left it as an option: telegram_date = False .
- Added autoformat feature to settings. To make your print output look clear: (examples: https://imgur.com/a/pyDUHKK): it basically checks if it has date in arguments or settings and if it does, then it adds another blank line in terminal prints between lines to improve readibility. If date wasn't required to print, it will print (log) content as usualy print() function does. Spent around 6 hours on this feature. It was the most complex probablt.
- Forgot to set date to True and specified date format? No problema, date will be set as True for ya!

