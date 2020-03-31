import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYINPUT"]

    my_output = f"Hello {my_input}"
    print(os.listdir())

    open('map.html', 'w').write('esto es una tiza de mapa')

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
