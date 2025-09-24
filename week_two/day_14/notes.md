##### logging
    - Logging is a means of tracking events that happen when some software runs. Logging is important for software developing, 
    debugging, and running. If you don't have any logging record and your program crashes, there are very few chances that you 
    detect the cause of the problem. And if you detect the cause, it will consume a lot of time. With logging, you can leave a 
    trail of breadcrumbs so that if something goes wrong, we can determine the cause of the problem. 

    * Python Logging Levels

    Debug: These are used to give Detailed information, typically of interest only when diagnosing problems.

    Info: These are used to confirm that things are working as expected

    Warning: These are used as an indication that something unexpected happened, or is indicative of some problem in the near future

    Error: This tells that due to a more serious problem, the software has not been able to perform some function

    Critical: This tells serious error, indicating that the program itself may be unable to continue running

    import logging

    # Set up basic configuration
    logging.basicConfig(level=logging.DEBUG)  # default level is WARNING

    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning")
    logging.error("This is an error")
    logging.critical("This is critical")

    ** Only messages with level WARNING and above will show by default unless you set **
    
    Handlers: Decide where logs go (file, console, HTTP, syslog, etc.).

    Formatters: Decide how logs look (timestamp, module, line number, etc.).

    Loggers: Different loggers for different modules (instead of one global logger).

##### regex
    - A regex is a special sequence of characters that defines a pattern for complex string-matching functionality.

    * Characters and their meanings

    . -> Matches any single character except newline
    
    ^ -> Anchors a match at the start of a string

    $ -> Anchors a match at the end of a string

    * -> Matches zero or more repetitions
    
    + -> Matches one or more repetitions

    {} -> Matches an explicitly specified number of repetitions

    \ -> Escapes a metacharacter of its special meaning

    [] -> Specifies a character class

    | -> Designates alternation

    () -> Creates a group

    :,#,=,! -> Designate a specialized group

    <> -> Creates a named group

    \w -> [a-zA-Z0-9_]

    \W -> Match based on whether a character is a word character.,[^a-zA-Z0-9_] negate \w (everythings except \w)

    \d -> Match based on whether a character is a decimal digit.

    \D ->  It matches any character that isn’t a decimal digit, [^0-9]

    \s -> Match based on whether a character represents whitespace.

    \S -> [^a-zA-Z]

    ##### re.search(pattern, text) -> re.search('^[0-9][0-9]$', 'abc12')
        - The re.search() method in Python's re module is used to find the first occurrence of a regular expression pattern within a given string. It scans through the entire string and returns a match object if a match is found, or None if no match is found. 

    ##### re.matches(pattern, text) -> re.match("Hello", 'Hello World)
        - re.match method in Python is used to check if a given pattern matches the beginning of a string. It’s like searching for a word or pattern at the start of a sentence.

    ##### re.findall()
        - re.findall(pattern, string) scans the entire string and returns all non-overlapping matches as a list of strings.

        When I said “non-overlapping”, it means:

        * re.findall() scans the string from left to right.

        * Once it consumes a portion of the string as a match, it does not try to match inside that same portion again.

        * But yes — the function returns the actual matched strings, not the positions.
    
    #### re.sub()
        - re.sub() method in Python parts of a string that match a given regular expression pattern with a new substring. This method provides a powerful way to modify strings by replacing specific patterns, which is useful in many real-life tasks like text processing or data cleaning.

    #### re.split()
        - re.split() method in Python is generally used to split a string by a specified pattern. Its working is similar to the standard split() function but adds more functionality.
    