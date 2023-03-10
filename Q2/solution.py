class Record():
    def __init__(self, isValid, error = None):
        self.isValid = isValid
        self.error = error


def main():
    num_of_recs = int(input())
    errorCodes = []
    allValid = True

    for i in range(num_of_recs):
        args = input().split()
        # records.append(Record(*args[1:]))
        allValid = allValid and (args[1] == 'true')
        # cover corner case of err code having space as well
        if args[1] == 'false':
            errorCodes.append((' ').join(args[2:]))
    
    if(allValid):
        print("Yes")
    else:
        print('No')
        print(' '.join(errorCodes))
    return

if __name__ == "__main__":
    main()
