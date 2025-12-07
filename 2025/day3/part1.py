
def getHighestJoltage(file_path):
    with open(file_path, 'r') as battery_banks:
        totalJoltage = 0
        for battery_bank in battery_banks:
            battery_bank = battery_bank.strip()
            totalJoltage += findHighestJoltage(battery_bank)
    return totalJoltage

def findHighestJoltage(battery_bank):
    highest = None
    second = None

    for i in range(len(battery_bank)):
        battery = battery_bank[i]
        if highest == None: highest = battery
        elif battery > highest and i+1 < len(battery_bank): 
            highest = battery
            second = None
        elif second == None: second = battery
        elif battery > second:
            second = battery
    
    joltage = int(highest + second)
    return joltage

print(findHighestJoltage('987654321111111')) # 98
print(findHighestJoltage('811111111111119')) # 89
print(findHighestJoltage('234234234234278')) # 78
print(findHighestJoltage('818181911112111')) # 92
print(getHighestJoltage("2025\day3\input.txt"))