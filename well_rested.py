import json

class Wrapper:
    def __init__(self, json_path: str) -> None:
        '''
        init opens the specified json file, checks its validity according to the format,
        and parses it, setting all api endpoints to class methods
        '''
        with open(json_path, "r") as json_file:
            self.api = json.load(json_file)

            if not isinstance(self.api, list):
                raise Exception("Invalid description file format.")
            
            for func_entry in self.api:
                if "function_name" not in func_entry:
                    raise Exception("No function_name field")

                setattr(self, func_entry["function_name"], self.return_zero)

    def return_zero(self, *args, **kwargs) -> int:
        return 0

def main() -> None:
    w = Wrapper("./references.json")
    print(w.mul(x=5, y=10))

if __name__ == "__main__":
    main()