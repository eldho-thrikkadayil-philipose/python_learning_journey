import sys

who = sys.argv[1] if len(sys.argv) > 1 else 'World'
print('Hello', who)