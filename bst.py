from tabnanny import check


def check_palindrome(S):
    n = len(S)
    count = 0
    for i in range(n//2):

        if(x[i] == x[n - i - 1]):
            count = count + 1
        else:
            return False
    if (count == n//2):
        return True
    else:
        return False


if __name__ == '__main__':
    x = input('Enter a string')
    if(check_palindrome(x)):
        print('The string is a palindrome')
    else:
        print('The string is not a palindrome')
