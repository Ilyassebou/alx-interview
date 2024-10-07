#!/usr/bin/python3
"""Solution to the Lockboxes problem."""


def canUnlockAll(box_list):
    """Check if all boxes can be opened."""
    
    if not isinstance(box_list, list) or len(box_list) == 0:
        return False

    for key in range(1, len(box_list) - 1):
        can_unlock = False

        for box_index in range(len(box_list)):
            can_unlock = key in box_list[box_index] and key != box_index
            if can_unlock:
                break
        
        if not can_unlock:
            return False
            
    return True
