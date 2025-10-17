import time

def format_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def log_message(message):    
    print(f'{format_timestamp()} \t Message from {message.author}: {message.content}')

def log(text):
    print(f'{format_timestamp()} \t {text}')