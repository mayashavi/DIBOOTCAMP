
while True:
    try:
        move = int (input('enter row and column'))
        if move < 1 or move > 3:
            print("Please enter a number between 1-3.")
        print("move accepted")
        break
    except Exception as e:
        print(e)