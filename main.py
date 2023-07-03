from funix import funix, run


@funix()
def greetings(name: str) -> str:
    return f"Hello {name}!"

if __name__ == "__main__":
    run("./main.py")
