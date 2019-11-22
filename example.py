def main(arg1, arg2):
    names = arg2.split("_")
    dict = {
        arg2: [
            {
                "name": names[0],
                "id": str(arg1)
            },
            {
                "name": names[1],
                "id": arg1
            }
        ]
    }
    print("hello world")
    myRequest(data=dict)

def myRequest(data=dict):
    pass
