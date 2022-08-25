# Emy Kay's original off-the-cuff example to explain __name__, Python imports, try/except

class MyObject():
    pass
def my_func():
    pass

print(f"what is the name when importing name_example.py?? {__name__}")


if __name__ == '__main__':

    print("we are inside __main__ ")

    for i in range(1000):
        i
        if i % 100 == 0:
            print(f"we are now at iteration {i}")
        # if i % 899 == 0:
            # try:
                # raise Exception(f"we hit an error at {i}")
            # except Exception as e:
                # print(e)
                # print("skipping")
