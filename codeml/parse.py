import os
import sys
import re
#parse_root = sys.argv[1]
parse_root = "C:/Users/wassfila/Projects/openthread"

print(f"parse_root = {parse_root}")
print(f"parse_root (absolute) = {os.path.abspath(parse_root)}")

max_test = 200

for root, subdirs, files in os.walk(parse_root):
    for filename in files:
        file_base, file_extension = os.path.splitext(filename)
        if(file_extension == '.c'):
            file_path = os.path.join(root, filename)
            print(f"c : {file_path}")
            
            #pattern = re.compile("(?![a-z])[^\:,>,\.]([a-z,A-Z]+[_]*[a-z,A-Z]*)+[(]")
            pattern = re.compile("\w+\(")
            for i, line in enumerate(open(file_path)):
                for match in re.finditer(pattern, line):
                    f_name = match.group(0)[:-1]
                    print(f"Found on line {i+1}: {f_name}")
                    max_test = max_test - 1
                    if(max_test == 0):
                        print("max test")
                        exit(0)

