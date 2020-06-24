def function(str, n):
    if n > 0:
        function(str, n-1)
        print(str, 'called the func with value n=', n)

def main():
    function("main", 7)

main()