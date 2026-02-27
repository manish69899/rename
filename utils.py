import time
import math

def progress_bar(current, total):
    """
    Example output: [■■■■■□□□□□] 50%
    """
    if total == 0: return "[----------] 0%"
    
    percentage = current / total
    finished_length = int(percentage * 10)
    
    bar = "■" * finished_length + "□" * (10 - finished_length)
    return f"[{bar}] {int(percentage * 100)}%"

def human_readable_time(seconds):
    """Seconds ko Minutes/Seconds me convert karta hai"""
    if seconds < 60:
        return f"{int(seconds)}s"
    minutes = int(seconds // 60)
    sec = int(seconds % 60)
    return f"{minutes}m {sec}s"