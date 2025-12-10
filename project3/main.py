from project3 import lcs_algorithm

def main():
    print("Welcome to the LCS (Longest Common Substring) Finder")
    string1 = input("Enter first string")
    string2 = input("Enter second string")
    lcs_algorithm(string1, string2)



if __name__ == '__main__':
    main()