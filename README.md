# pynse

Library to extract realtime and historical data from NSE website.EOD data like bhavcopy and option chain are also saved to directory. First run will create directories for storing the data and will download the index symbols. 

### Prerequisites

Python 3.x


## Using the API

### Overview
There is only one class in the whole library `Nse`. 

### Logging
The whole library is equipped with python's `logging` moduele for debugging. If more debug information is needed, enable logging using the following code.

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

```python
from pynse import *
nse=Nse()
```

### Get Market Status

```python
nse.market_status()
```

### Get Symbol Information
```python
nse.info('SBIN')
```

### Get Quote
Get realtime quote for EQ, FUT and OPT. If no expiry date is provided for derivatives, returns date for nearest expiry.

for cash
```python
nse.get_quote('RELIANCE')
```

for futures
```python
nse.get_quote('TCS', segment=Segment.FUT, expiry=dt.date( 2020, 6, 30 ))
```

for options
```python
nse.get_quote('HDFC', segment=Segment.OPT, optionType=OptionType.PE)
```
