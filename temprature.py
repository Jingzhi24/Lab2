


def dispaly_main_manu():
    print("Enter some numbers seperate by commas e.g.(5,67,32)")

def get_user_input():
    print("Please Enter your number")
    x = input()
    print(x)
    string_list= x.split(",")
    float_list = [float(item.strip()) for item in string_list]
    return float_list
    


def calc_average_temperature(data_list):
    if not data_list:
        return 0.0
    return sum(data_list) / len(data_list)

def find_min_max(data_list):
    if not data_list:
        return [0.0, 0.0]
    return [min(data_list), max(data_list)]


if __name__ == "__main__":
    dispaly_main_manu()
    get_user_input()
    
    find_min_max()
    calc_average_temperature()