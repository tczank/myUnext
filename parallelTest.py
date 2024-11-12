#!/usr/bin/python

from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def process_item(args):
    i, j = args
    # Your processing here
    print(f"Processing {i}-{j}")
    # No return needed

combinations = [(i, j) for i in range(10) for j in range(5)]

# Option 1: If you don't need to track completion
with ThreadPoolExecutor() as executor:
    list(executor.map(process_item, combinations))

# Option 2: If you want a progress bar
with ThreadPoolExecutor() as executor:
    list(tqdm(
        executor.map(process_item, combinations),
        total=len(combinations)
    ))
