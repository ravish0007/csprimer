import urllib.request


cache = {}

def caching_func(f):
    def wrapper(arg):
        if arg in cache:
            print('fetching from cache', arg)
            return cache[arg]
        result = f(arg)
        cache[arg] = result
        return result

    return wrapper

@caching_func
def fetch(url):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        return content

@caching_func
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fetch('http://google.com')[:80])
    print('=======================')
    print(fetch('http://google.com')[:80])
