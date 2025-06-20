# Secret Management
# ------------------------------------------------------------------------------
# Retrieve secrets like API keys from environment variables instead of
# hardcoding them in the source code.

import os

api_key = os.getenv('API_KEY')
if api_key is None:
    raise RuntimeError('API_KEY environment variable is not set')

print('Loaded API key of length', len(api_key))
