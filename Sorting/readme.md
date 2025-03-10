# Partition-and-Merge Sorting Algorithm

## Overview

This repository contains a **Partition-and-Merge Sorting Algorithm**, a unique approach to sorting a list of integers. The algorithm splits the sorting process into two phases:

1. **Partitioning**: Identifies and removes "problem elements" from the list.
2. **Merging**: Inserts the removed elements back into the list in sorted order.

This algorithm was created as a fun project to explore sorting from a fresh perspective. It is **not optimized** for performance but serves as a valuable exercise for understanding list manipulation and basic sorting concepts.

## How It Works

### Phase 1: Partitioning
- The algorithm traverses the list, comparing each element to the next.
- If an element is greater than the next, it’s removed from the main list and stored in a separate list (`y`).
  
### Phase 2: Merging
- The elements stored in `y` are inserted back into the main list, one by one, in the correct position to maintain order.

## Features

- **Easy to understand**: A beginner-friendly way to explore sorting.
- **Two-phase approach**: Partitioning and merging—breaking the task into smaller parts.
- **Hands-on learning**: Great for beginners who want to create their own sorting algorithm.

## Requirements

- Python 3.x

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/<username>/partition-and-merge-sort.git
#   S p l i t - S o r t  
 #   S p l i t - S o r t  
 