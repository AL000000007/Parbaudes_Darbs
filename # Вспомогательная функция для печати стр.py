def print_with_indent(text, indent=4):
    print(" " * indent + text)



def fibonacci_iterative(n):
    if n <= 0:
        raise ValueError("Skaitlim jābūt lielākam par 0.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
   
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
    return b



def fibonacci_recursive(n, C=None):
    if C is None:
        C = {1: 0, 2: 1}  

    if n <= 0:
        raise ValueError("Skaitlim jābūt lielākam par 0.")

    if n not in C:  
        C[n] = fibonacci_recursive(n - 1, C) + fibonacci_recursive(n - 2, C)

    return C[n]

 

def fibonacci_memoization(n, memo=None):
    if memo is None:
        memo = {1: 0, 2: 1}
   
    if n <= 0:
        raise ValueError("Skaitlim jābūt lielākam par 0.")
   
    if n not in memo:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
   
    return memo[n]



def main():
    print("Laipni lūdzam programmā Fibonači skaitļu aprēķināšanai!")
    print("Izvēlieties aprēķināšanas metodi:")
    print("1. Iteratīvā metode")
    print("2. Rekursīvā metode")
    print("3. Memoizācijas metode")
   

    method_choice = input("Ievadiet metodes numuru (1, 2, 3): ")
   
    
    if method_choice not in ['1', '2', '3']:
        print("Nepareiza metodes izvēle. Mēģiniet vēlreiz.")
        return


    n = input("Ievadiet Fibonači skaitļa numuru: ")
   

    try:
        n = int(n)
        if n <= 0:
            print("Skaitlim jābūt lielākam par nulli. Mēģiniet vēlreiz.")
            return
    except ValueError:
        print("Nepareiza ievade! Ievadiet veselu skaitli.")
        return
   
   
    if method_choice == '1':
        print_with_indent(f"Fibonači skaitlis {n}-ajā pozīcijā (iteratīvā metode): {fibonacci_iterative(n)}")
    elif method_choice == '2':
        print_with_indent(f"Fibonači skaitlis {n}-ajā pozīcijā (rekursīvā metode): {fibonacci_recursive(n)}")
    elif method_choice == '3':
        print_with_indent(f"Fibonači skaitlis {n}-ajā pozīcijā (memoizācija): {fibonacci_memoization(n)}")
   
    print("\nVai vēlaties turpināt? (jā/nē)")
    continue_choice = input().strip().lower()
    if continue_choice == 'jā':
        main()
    else:
        print("Paldies, ka izmantojāt programmu! Uz redzēšanos.")
       

if __name__ == "__main__":
    main()


print("Programmas darbs pabeigts.")