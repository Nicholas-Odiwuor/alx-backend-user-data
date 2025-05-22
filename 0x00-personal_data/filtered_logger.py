#!/usr/bin/env python3
"""
Module for filtering log messages to redact personal data.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message with specified fields obfuscated using regex.
    """
    return re.sub(f"({'|'.join(fields)})=.+?{separator}", lambda m: f"{m.group(1)}={redaction}{separator}", message)

