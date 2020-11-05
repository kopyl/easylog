
from config import *
from telegram_auth import BOT_TOKEN, YOUR_TELEGRAM_ID

import sys
logfile_open_append = open(errors_file, "w")
sys.stderr = logfile_open_append

log_history = [] # Storage of updates of what was previously and currently printed.
count_print_lines = 0 # To format print text properly – don't print empty line on start and to understand where to put the first empty line (probably).
lines_between_prints = lines_between_prints*'\n'

def timestamp(time_format='%d.%m.%y – %H:%M:%S'):
	"""
	Required to get time 
	"""
	import time
	return time.strftime(time_format)










def log(*content, date=date, mode='a', file=file, sep=' ', end='\n', date_format=date_format, lines_between_prints=lines_between_prints):
	"""
	Print any text you need and add it to file.
	"""
	global log_history
	global count_print_lines

	if date_format != '%d.%m.%y – %H:%M:%S':
		date = True
	
	if autoformat_prints_to_terminal == True:
		if date == True:
			log_history.append('log_date')
			timestamp_variable = timestamp(date_format)

			if count_print_lines == 0:
				before_line = ''
			elif log_history[-1] == 'log_date':
				before_line = '\n'
			elif log_history[-1] == 'log_no_date':
				before_line = ''
			elif log_history == []:
				before_line = ''
			count_print_lines+=1

			print(before_line+timestamp_variable+'\n'+sep.join(str(each) for each in content), end=end)

			with open(file, mode) as log_file:
				log_file.write(timestamp_variable+'\n') # need to wrap in str() since in input there may be ints. And it's impossible to concatenate ints with strings.
				log_file.write(sep.join(str(each) for each in content)+"\n\n")
		else:
			log_history.append('log_no_date')
			with open(file, mode) as log_file:
				log_file.write(sep.join(str(each) for each in content)+"\n\n")

			if count_print_lines == 0:
				after_line = '\n'
			if log_history[-1] == 'log_date':
				after_line = '\n'
			elif log_history[-1] == 'log_no_date':
				after_line = ''
			else:
				after_line = ''

			if len(log_history) > 1:
				if log_history[-2] == 'log_no_date':
					before_line = ''
				else:
					before_line = '\n'
			else:
				before_line = ''
			count_print_lines+=1
			
			print(before_line+sep.join(str(each) for each in content)+after_line, end=end)

	if autoformat_prints_to_terminal == False:
		if date == True:
			timestamp_variable = timestamp(date_format)
			print(timestamp_variable+'\n'+sep.join(str(each) for each in content)+lines_between_prints, end=end)

			with open(file, mode) as log_file:
				log_file.write(timestamp_variable+'\n') # need to wrap in str() since in input there may be ints. And it's impossible to concatenate ints with strings.
				log_file.write(sep.join(str(each) for each in content)+"\n\n")
		else:
			with open(file, mode) as log_file:
				log_file.write(sep.join(str(each) for each in content)+"\n\n")

			print(sep.join(str(each) for each in content)+lines_between_prints, end=end)





def clean_log_file(file=file):
	"""
	Clean log file completely. Leaves file empty without deleting it.
	"""
	with open(file, 'w') as log_file:
		log_file.write("")





def unlog(lines_to_clean=1, file=file):
	"""
	Remove any records from the log file. unlog() to remove just last record. Record = each line in the log file.
	"""
	with open(file, 'r') as log_file_to_clean:
		lines = "".join(file_to_clean.readlines()[0:-lines_to_clean])
		with open(file, 'w') as log_file_to_clean:
			file_to_clean.write(lines)





def tg_log(*content, date=date, mode='a', file=file, sep=' ', end='\n', date_format=date_format, errors_file=errors_file, telegram_date=telegram_date):
	
	"""
	Send text to telegram and save it to file. 
	"""
	if date_format != '%d.%m.%y – %H:%M:%S':
		date = True

	import telebot
	timestamp_variable = timestamp(date_format)
	if len(log_history) > 0:
		if log_history[-1] == 'log_date' or log_history[-1] == 'log_date':
			before_line = lines_between_prints
		else:
			before_line = lines_between_prints
	else:
		before_line = ''
	if date == True:
		if file != False:
			with open(file, mode) as log_file:
				log_file.write(timestamp_variable+'\n'+str(sep.join(str(each) for each in content))+f'\nSending "{sep.join(str(each) for each in content)}" to your Telegram')
		if telegram_date == True:
			telebot.TeleBot(BOT_TOKEN).send_message(YOUR_TELEGRAM_ID, timestamp_variable+'\n'+str(sep.join(str(each) for each in content)))
		else:
			telebot.TeleBot(BOT_TOKEN).send_message(YOUR_TELEGRAM_ID, str(sep.join(str(each) for each in content)))
		print(before_line+timestamp_variable+'\n'+str(sep.join(str(each) for each in content))+f'\nSending "{sep.join(str(each) for each in content)}" to your Telegram')
	else:
		if file != False:
			with open(file, mode) as log_file:
				log_file.write(sep.join(str(each) for each in content)+f'\nSending "{sep.join(str(each) for each in content)}" to your Telegram')
		telebot.TeleBot(BOT_TOKEN).send_message(YOUR_TELEGRAM_ID, sep.join(str(each) for each in content))
		print(before_line+str(sep.join(str(each) for each in content))+f'\nSending "{sep.join(str(each) for each in content)}" to your Telegram')
	with open(errors_file, 'r') as errors_file:
		errors_file_content = "".join(errors_file.readlines())
		if errors_file_content == "":
			if file != False:
				with open(file, mode) as log_file:
					log_file.write("\nSent successully"+"\n\n")
			print("Sent successully"+lines_between_prints, end=end)






import os






def delete_log_file(file=file):
	"""
	Deletes log file completely.
	"""
	try:
		os.remove(file)
	except FileNotFoundError:
		log("No file to remove, dude")





def print_stderr_and_attach_to_log_file(file=file, mode='a'):
	"""
	Necessary function for printing stderr bot to file & stream. Always initialized before program ends.
	"""
	with open(errors_file, 'r') as errors_file_to_read:
		errors_file_content = "".join(errors_file_to_read.readlines())
		print(errors_file_content)
		print('\n')	
		if errors_file_content != "": # If error file contains something, do following. If it contains something except nothing it means it has content. Content in the error log file always has nothing but errors.
			if errors_to_telegram == True:
				try:
					tg_log('\n'+errors_file_content, mode=mode)
				except:
					log('\n'+errors_file_content, mode=mode)
			else:
				if file != False:
					with open(file, mode) as log_file:
						log_file.write('\n'+str(errors_file_content)+'\n', mode=mode)
		if remove_errors_file_after_creation == True:
			os.remove(errors_file) # remove errors file after the error was raised










l = log
import atexit
atexit.register(print_stderr_and_attach_to_log_file) # when program ends even with erros, perform stderr file reading and printing + saving + deleting the file.
