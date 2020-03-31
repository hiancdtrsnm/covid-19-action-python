import os
import requests  # noqa We are just importing this to prove the dependency installed correctly
import json

def main():

    os.makedirs('data/mini')
    data = json.load(open('data/covid19-cuba.json'))
    json.dump(data, open('data/mini/covide-cuba.json' 'w'))

if __name__ == "__main__":
    main()
