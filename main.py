import os
import requests  # noqa We are just importing this to prove the dependency installed correctly
import json

def main():

    os.makedirs('data/mini',exist_ok=True)
    data = json.load(open('data/covid19-cuba.json'))
    json.dump(data, open('data/mini/covid19-cuba.json', 'w'))

if __name__ == "__main__":
    main()
