# pynse
Library to extract realtime and historical data from NSE website

## Using the API

### Logging
The whole library is equipped with python's `logging` moduele for debugging. If more debug information is needed, enable logging using the following code.
  
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

```python
from pynse import *
nse=Nse()
nse.info('SBIN')
```
