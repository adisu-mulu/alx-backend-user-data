# 0x00-personal_data

## Introduction

The `0x00-personal_data` directory contains scripts and tools for managing personal user data in the Alx Backend application. These scripts help with tasks related to collecting, storing, and retrieving personal information securely.

## Program Descriptions

- **filtered_logger.py:** This Python script is responsible for logging sensitive information while filtering out specific types of data, such as passwords and credit card numbers, before writing to the log file. It ensures that sensitive data is not stored in logs, helping maintain security and compliance.

## Compiling and Executing

To use the `filtered_logger.py` script, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/iakev/alx-backend-user-data.git
   ```

2. Navigate to the 0x00-personal_data directory:

  ```bash
  cd 0x00-personal_data
  ```

3. Execute the script the Python command:

    ```bash
    python filtered_logger.py
    ```
4. The script will run and demonstrate how sensitive data is filtered out before logging.

## Resources

For additional learning and reference on personal data, logging, and security, explore these resources:

- [What Is PII, non-PII, and Personal Data?](https://digitalguardian.com/blog/what-personally-identifiable-information-pii): This article explains the concepts of Personally Identifiable Information (PII), non-PII, and personal data, helping you understand the different types of data you might handle.

- [Logging Documentation](https://docs.python.org/3/library/logging.html): The official Python documentation for the logging module. It provides in-depth information on how to use Python's built-in logging system effectively.

- [bcrypt Package](https://pypi.org/project/bcrypt/): The PyPI page for the bcrypt package, a widely-used library for securely hashing passwords. You can find documentation and usage examples here.

- [Logging to Files, Setting Levels, and Formatting](https://realpython.com/python-logging/): A comprehensive guide on Python logging, covering topics like logging to files, setting log levels, and formatting log messages.


   
