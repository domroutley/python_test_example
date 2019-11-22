def main(arg1, arg2, arg3):
    names = arg2.split("_")
    print("foo")
    if arg3 == True:
        dict = {
            arg2: [
                {
                    "name": names[0],
                    "id": arg1
                },
                {
                    "name": names[1],
                    "id": str(arg1)
                }
            ]
        }
    else:
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
    myRequest(data=dict)

def myRequest(data=dict):
    print("bar")

if __name__ == "__main__":
    main(1, "hi_hi", True)
