"""Console script for taobao_web_auto."""

import fire

def help():
    print("taobao_web_auto")
    print("=" * len("taobao_web_auto"))
    print("taobao selenium sauto web")

def main():
    fire.Fire({
        "help": help
    })


if __name__ == "__main__":
    main() # pragma: no cover
