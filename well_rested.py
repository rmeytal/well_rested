import json

class Wrapper:
    def __init__(self, json_path: str) -> None:
        with open(json_path, "r") as json_file:
            api = json.load(json_file)
            for func in list(api["functions"]):
                setattr(self, func, self.return_zero)

    def return_zero(self, *args, **kwargs) -> int:
        return 0

def main() -> None:
    w = Wrapper("./references.json")
    print(w.mul(x=5, y=10))

if __name__ == "__main__":
    main()