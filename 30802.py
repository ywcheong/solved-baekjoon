n = int(input())
size_list = list(map(int, input().split()))
shirt_unit, pencil_unit = list(map(int, input().split()))

def convert_shirt_unit(count):
    if count % shirt_unit == 0:
        return count // shirt_unit
    return count // shirt_unit + 1

print(sum(map(convert_shirt_unit, size_list)))
print(n // pencil_unit, n % pencil_unit)