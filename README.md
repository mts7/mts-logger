# mts-logger

This is my first attempt at writing a logger in Python, which happened before I learned the `logging` package already
exists and works beautifully.

When there is a log to write, it outputs in the color corresponding to the log method used. The log level (or mode) can
be one of `error`, `warning`, `info`, or `debug`. A future version might include `critical`. The current outputs
supported are screen/console and file, though a future version might make use of the parent logging class.

## Usage

### .env

```dotenv
log_level='debug'
log_output='out'
log_file=None
log_use_error=True
```

### requirements.txt

```text
git+https://github.com/mts7/mts-logger@v0.2.4
```

### module.py

```python
import mtslogger

logger = mtslogger.get_logger(__name__)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.log('message according to log level')
```

## TODO

1. Add tests
1. Reimplement using parent class options
1. Add options for passing variables (like list and dict)
1. Clean up the config in the beginning of the class
1. Clean up parameter handling and passing
1. Add ability for external connections
