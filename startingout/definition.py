def function(str, n):
    if n > 0:
        print(str, 'called func with n=', n)
        function(str, n-1)

def main():
    function("main", 7)

main()