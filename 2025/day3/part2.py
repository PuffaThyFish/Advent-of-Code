
def getHighestJoltage(file_path):
    with open(file_path, 'r') as battery_banks:
        totalJoltage = 0
        for battery_bank in battery_banks:
            battery_bank = battery_bank.strip()
            totalJoltage += findHighestJoltage(battery_bank)
    return totalJoltage

def findHighestJoltage(battery_bank):
    highest = [None] * 12
    bank_size = len(battery_bank)

    for i in range(bank_size):
        battery = battery_bank[i]

        # loop through each spot
        for j in range(len(highest)):
            if highest[j] == None:
                highest[j] = battery
                break
            elif battery > highest[j] and 12-j-1 > 0:
                highest = highest[:j] + [battery] + [None]*(12-j)
                break
    
    joltage = ''
    for num in highest:
        joltage += str(num)
    return int(joltage)



print(findHighestJoltage('987654321111111')) # 987654321111 987654321111
print(findHighestJoltage('811111111111119')) # 811111111119 811111111111
print(findHighestJoltage('234234234234278')) # 434234234278 234234234234
print(findHighestJoltage('818181911112111')) # 888911112111 818181911112
print(getHighestJoltage("2025\day3\input.txt"))