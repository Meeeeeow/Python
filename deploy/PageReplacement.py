# FIFo


def fifo_method():
    my_processes = list(map(int, input().split()));
    count = page_fault = page_hit = frame_number = 0;
    frames = int(input());
    memory = [];
    for item in my_processes:
        if memory.count(item) == 0 and count < frames:  # frame not filled
            memory.append(item);
            page_fault += 1;
            count += 1;
        elif memory.count(item) == 0 and count == frames:  # frame filled
            print(f'Full Size of memory is {memory} ')
            item_popped = memory.pop(frame_number);
            print(f'{item_popped} popped from frame {frame_number}');
            memory.insert(frame_number, item);
            print(f'Modified Size of memory is {memory} ')
            frame_number += 1;
            page_fault += 1;
            if frame_number == frames:
                frame_number = 0;
        elif memory.count(item) > 0:  # item is already in frame
            page_hit += 1;
    percentage_page_fault = (page_fault / len(my_processes)) * 100;
    percentage_page_hit = (page_hit / len(my_processes)) * 100;
    print(
        f'Page fault is {page_fault} and Page hit is {page_hit} and page fault percentage is {round(percentage_page_fault, 4)} and page hit percentage is {round(percentage_page_hit, 4)}');

    # Optimal


def optimal_method():
    my_processes = list(map(int, input().split()));
    frames = int(input());
    count = page_fault = page_hit = index = 0;
    max_index = - 1;
    memory = []
    for item in my_processes:
        if memory.count(item) == 0 and count < frames:  # frame not filled
            memory.append(item);
            page_fault += 1;
            count += 1;
        elif memory.count(item) == 0 and count == frames:  # frame filled
            test_index = my_processes[index:].index(item);
            # print(test_index+index , item);
            index += test_index;
            # print(f'index of the extra item  is {index}');
            for value in memory:
                if value in my_processes[index:]:
                    value_index = my_processes[index:].index(value);
                    # print(f'index in secondary page  is {value_index} and values is {value}');
                    if value_index > max_index:
                        max_index = value_index;
                        swapped_value = value;
                elif value not in my_processes[index:]:
                    swapped_value = value;
                    break;
            print(f'Before {memory}');
            index_swapped_value = memory.index(swapped_value);
            item_popped = memory.pop(index_swapped_value);
            print(f'Item popped {item_popped}');
            memory.insert(index_swapped_value, item);
            print(f'modified memory {memory}');
            max_index = -1;
            page_fault += 1;
        elif memory.count(item) > 0:
            page_hit += 1;

    percentage_page_fault = (page_fault / len(my_processes)) * 100;
    percentage_page_hit = (page_hit / len(my_processes)) * 100;
    print(
        f'Page fault is {page_fault} and Page hit is {page_hit} and page fault percentage is {round(percentage_page_fault, 4)} and page hit percentage is {round(percentage_page_hit, 4)}');

    # LRU
def lru_method():
    my_processes = list(map(int, input().split()));
    frames = int(input());
    count = page_fault = page_hit = index = 0;
    max_index = - 1;
    memory = []
    for item in my_processes:
        if memory.count(item) == 0 and count < frames:
            memory.append(item);
            page_fault += 1;
            count += 1;

        elif memory.count(item) == 0 and count == frames:
            test_index = my_processes[index:].index(item);
            print(test_index + index, item);
            index += test_index;
            for value in memory:
                if value in my_processes[index::-1]:
                    value_index = my_processes[index::-1].index(value);
                    print(f'index is {value_index} and values is {value}');
                    if value_index > max_index:
                        max_index = value_index;
                        swapped_value = value;
                elif value not in my_processes[index:]:
                    swapped_value = value;
                    break;
            print(f'before {memory}');
            index_swapped_value = memory.index(swapped_value);
            item_popped = memory.pop(index_swapped_value);
            print(f'Item popped {item_popped}');
            memory.insert(index_swapped_value, item);
            print(f'modified memory {memory}');
            max_index = -1;
            page_fault += 1;
        elif memory.count(item) > 0:
            page_hit += 1;
    percentage_page_fault = (page_fault / len(my_processes)) * 100;
    percentage_page_hit = (page_hit / len(my_processes)) * 100;
    print(
        f'Page fault is {page_fault} and Page hit is {page_hit} and page fault percentage is {round(percentage_page_fault, 4)} and page hit percentage is {round(percentage_page_hit, 4)}');

    # main


if __name__ == '__main__':
    print(f'\t\t\t\t Page Replacement Algorithms')
    print('Options');
    print('1. FIFO \n2. optimal \n3. LRU');
    choice = int(input('Please enter your choice below(1 to 3):\n'));
    while choice >= 1 and choice <= 3:
        if choice == 1:
            fifo_method();
        elif choice == 2:
            optimal_method();
        elif choice == 3:
            lru_method();
        choice = int(input('Please enter your choice again(1 to 3):\n'));
    print('Thank you for playing!');

