import re 

def extract_username(email): 
    match = re.match(r"(\w+)@(\w+\.\w+)", email) 
    return match.group(1) 

# Example usage 
print(extract_username("alice@company.com"))