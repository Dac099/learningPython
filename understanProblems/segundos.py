def calculate(hours, minutes):
    seconds = 0
    seconds += minutes * 60
    seconds += hours * 3600
    return seconds

def getData(): 
    hours = int(input('Hours: '))
    minutes = int(input('Minutes: '))
    return calculate(hours, minutes)

if __name__ == '__main__':
    time = getData()
    print(f"Time in seconds: {time}")