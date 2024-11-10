import os
import sys
from pathlib import Path

def touch(path):
    """
    Create a file if it doesn't exist, or update its timestamp if it does.
    Creates parent directories if they don't exist.
    """
    try:
        # Convert to Path object for better path handling
        filepath = Path(path)
        
        # Create parent directories if they don't exist
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        # Open the file in append mode, creating it if it does not exist
        filepath.touch(exist_ok=True)
        return True
        
    except PermissionError:
        print(f"touch: cannot touch '{path}': Permission denied", file=sys.stderr)
    except OSError as e:
        print(f"touch: cannot touch '{path}': {e.strerror}", file=sys.stderr)
    return False

def main():
    if len(sys.argv) < 2:
        print("Usage: touch FILE...", file=sys.stderr)
        print("Update the access and modification times of each FILE to the current time.", file=sys.stderr)
        sys.exit(1)
    
    success = True
    for file_path in sys.argv[1:]:
        if not touch(file_path):
            success = False
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()