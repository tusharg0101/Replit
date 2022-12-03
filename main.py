import json
import argparse
  
def insert(current_version, characters, current_position):
    current_version = current_version[ : current_position] + characters + current_version[current_position : ]
    current_position = current_position + len(characters)
    return current_version, current_position

def delete(current_version, count, current_position):
    if current_position + count > len(current_version): 
        return False, "delete past end"
    
    current_version = current_version[ : current_position] + current_version[current_position + count : ]
    return current_version, current_position

def skip(current_version, count, current_position):
    if current_position + count > len(current_version):
        return False, "skip past end"

    current_position = current_position + count
    return current_version, current_position

def isValid(stale, latest, operations):
    current_version = stale[:]
    current_position = 0
    
    for op in operations:
        instruction = op["op"]

        if instruction == "insert":
            current_version, current_position = insert(current_version, op["chars"], current_position)

        elif instruction == "delete":
            current_version, current_position = delete(current_version, op["count"], current_position)
            if not current_version:
                return "delete past end"
        
        elif instruction == "skip":
            current_version, current_position = skip(current_version, op["count"], current_position)
            if not current_version: 
                return "skip past end"
    return current_version == latest

def main():
    parser = argparse.ArgumentParser(description="OT Validation")
    parser.add_argument('stale', type = str, metavar="",
                        help ='relative path to stale file')

    parser.add_argument('latest', type = str, metavar="",
                        help ='relative path to latest file')  
    
    parser.add_argument('operations', type = str, metavar="",
                        help ='relative path to operations JSON file')
    
    args = parser.parse_args()

    operations_file = open(args.operations)
    operations = json.load(operations_file)

    stale_file = open(args.stale)
    stale = stale_file.read()

    latest_file = open(args.latest)
    latest = latest_file.read()
    
    result = isValid(stale, latest, operations)
    
    operations_file.close()
    stale_file.close()
    latest_file.close()

    if result != True and result != False: 
        print(f"False, {result}")
    else: 
        print(result)
    
# Main function calling
if __name__ == "__main__":
    main()
