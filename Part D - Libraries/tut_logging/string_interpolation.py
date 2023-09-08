import logging

hello = 'Hello world!'

logging.basicConfig(format='%(asctime)s - %(name)s - %(threadName)s - %(message)s')
root = logging.getLogger()
root.warning(f'Logger message {hello}')

