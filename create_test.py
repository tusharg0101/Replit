def make_test(test_number, test_case):
    if test_number == None or test_case == None: 
        return False

    stale_address = f"stale_{test_number}.txt"
    latest_address = f"latest_{test_number}.txt"
    operations_address = f"operations_{test_number}.json"

    with open(stale_address, 'w') as f:
        f.write(test_case[0])

    with open(latest_address, 'w') as f:
        f.write(test_case[1])

    with open(operations_address, 'w') as f:
        f.write(test_case[2])

make_test(None, None)