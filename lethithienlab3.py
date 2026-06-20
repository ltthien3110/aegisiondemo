def show_menu():
    print('----MENU----')
    print('1. Add value.')
    print('2. Search value.')
    print('3. Remove the first occurrence of a value.')
    print('4. Remove all the occurrences of a value.')
    print('5. Print out the array.')
    print('6. Sort the array in ascending orders.')
    print('7. Sort the array in descending orders.')
    print('Others: Exit the program.')
    yourchoice = input('Choose an option: ')
    return yourchoice
def bubble_sort(arr, ascending = True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                if arr[j] > arr[j +1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
def main():
    array = []
    max = 100
    while True:
        choice = show_menu()
        if choice == '1':
            if len(array) >= max:
                print('The array is full (max 100 elements) cannot add more.')
            else:
                try:
                    val = int(input('Input an integer to add: '))
                    array.append(val)
                    print('Successfully added ', val, ' to the array,')
                except ValueError:
                    print('Invalid! Please enter a valid integer.')
        elif choice == '2':
            try:
                val = int(input('Input an integer to search: '))
                if val in array:
                    index = array.index(val)
                    print('The index of ', val, ' in the array is: ',index)
                else:
                    print('Value ', val, ' not found in the array.')
            except ValueError:
                    print('Invalid! Please enter a valid integer.')
        elif choice == '3':
            try:
                val = int(input('Input an integer to remove (first occurence): '))
                if val in array:
                    array.remove(val)
                    print('Successfully removed the first occurence of ', val)
                else:
                    print('Value ', val, ' not found in the array.')
            except ValueError:
                print('Invalid! Please enter a valid integer.')
        elif choice == '4':
            try:
                val = int(input('Input an integer to remove (all occurences): '))
                if val in array:
                    array[:] = [item for item in array if item != val]
                    print('Successfully removed all occurrences of ', val)
                else:
                    print('Value ', val, ' not found in the array.')
            except ValueError:
                print("Invalid! Please enter a valid integer.")
        elif choice == '5':
            if len(array) == 0:
                print("The array is currently empty.")
            else:
                print("Array elements:", array)
        elif choice == '6':
            if len(array) == 0:
                print("The array is empty. Nothing to sort.")
            else:
                bubble_sort(array, ascending = True)
                print("The array has been sorted in ascending order.")
        elif choice == '7':
            if len(array) == 0:
                print("The array is empty. Nothing to sort.")
            else:
                bubble_sort(array, ascending = False)
                print("The array has been sorted in descending order.")
        else:
            print("Goodbye!")
            break
main()