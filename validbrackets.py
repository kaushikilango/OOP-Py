def validity(s):
    f = [0] * 100
    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            f[i] = 1
        if s[i] == ')' or s[i] == '}' or s[i] == ']':
            set = 0
            if(s[i] == ')'):
                t = '('
            elif(s[i] == '}'):
                t = '{'
            elif(s[i] == ']'):
                t = '['
            for k in range(i-1, -1, -1):
                print(f[k])
                print
                if(f[k] != 0 and s[k] != t):
                    return False
                elif(f[k] == 1 and s[k] == t):
                    f[k] = 0
                    set = 1
                    break
            if(set == 0):
                return False
    return True


c = input()
print(validity(c))
