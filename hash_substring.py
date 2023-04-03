# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().rstrip().lower()
    
    if input_type == "i":
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == "f":
        file_name = input().rstrip()
        with open("tests/06") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        raise ValueError("Invalid input type. choose I or F")
        
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p_len, t_len = len(pattern), len(text)
    p_hash, t_hash = hash(pattern), hash(text[:p_len])
    result = []
    for i in range (t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+p_len]:
                result.append(i)
        if i < t_len - p_len:
            t_hash = hash(text[i+1:i+p_len+1])
    return result
        
# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
