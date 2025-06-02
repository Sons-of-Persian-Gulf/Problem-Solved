for _ in range(int(input())):
    phone_number = input()
    if phone_number.startswith("09") and len(phone_number) == 11 and "+" not in phone_number:
        print(f"+98{phone_number[1:]}")
    elif phone_number.startswith("98") and len(phone_number) == 12 and "+" not in phone_number:
        print(f"+{phone_number}")
    elif phone_number.startswith("+98") and len(phone_number) == 13 and "+" not in phone_number[1:]:
        print(phone_number)
    else:
        print("invalid")
