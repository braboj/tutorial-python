import logging

hello = 'Hello world!'

logging.basicConfig(format='%(asctime)s - %(name)s - %(threadName)s - %(message)s')
logging.warning(f'Logger message {hello}')

