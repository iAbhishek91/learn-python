# Logging

Main purpose of logging instead of print statement.

- globally control when it fires
- automatically add additional metadata - timestamp, label of level, color coding etc
- output to different places

## Logging module and code to implement

**logging** inbuilt module

```python
import logging

# create a logger
logger = logging.getLogger("debug_logger")

# create a log stream handler
# this is not required for simple logging, however its required for different stuff like different logging level or formatting
# scenario like (error and critical should be email-id, and other should be in standard output)
handler = logging.StreamHandler()

## Format log message
my_format = loggingFormatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s")

handler.setFormatter(my_format)

# set formatter to logger
logger.setFormatter(myFormat)

logger.setLevel(logging.DEBUG)

logger.debug("something")


```

## Python logging levels

DEBUG (all)
INFO (all below)
WARNING (all below)
ERROR (error and critical)
CRITICAL (only critical)
