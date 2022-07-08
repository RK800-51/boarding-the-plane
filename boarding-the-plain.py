
def right_replace(string, old, new, n):
    return string[::-1].replace(old[::-1], new[::-1], n)[::-1]


def seat_manager(row, n, side, position):
    if side == 'left':
        if position == 'aisle':
            selected_seats = row[-5:-5-n:-1]
            if selected_seats.count('.') == n:
                tickets = row[-5-n::-1][::-1] + right_replace(row[-5:-5-n:-1], '.', 'X', n) + row[3::]
                return tickets
        else:
            selected_seats = row[0:0+n]
            if selected_seats.count('.') == n:
                tickets = row[0:0+n].replace('.', 'X', n) + row[n::]
                return tickets
    else:
        if position == 'aisle':
            selected_seats = row[4:4+n]
            if selected_seats.count('.') == n:
                tickets = row[0:4] + row[4:4+n].replace('.', 'X', n) + row[4+n::]
                return tickets
        else:
            selected_seats = row[-1:-1 - n:-1]
            if selected_seats.count('.') == n:
                tickets = row[0:4] + row[-1-n:-4:-1][::-1] + right_replace(row[-1:-1 - n:-1], '.', 'X', n)
                return tickets


def info_about_tickets(n, number, answer):
    names_for_seats = {0: 'A', 1: 'B', 2: 'C', 4: 'D', 5: 'E', 6: 'F'}
    seat_X = answer.index('X')
    string = 'Passengers can take seats:'
    for i in range(n):
        string = string + ' ' + str(number+1) + names_for_seats[seat_X + i]
    return string


num_of_rows = int(input())
rows = [input() for i in range(num_of_rows)]
num_of_passengers = int(input())
requests = tuple(input() for j in range(num_of_passengers))
for request in requests:
    seats_found = False
    request = request.split()
    n = int(request[0])
    side = request[1]
    position = request[2]
    for row in rows:
        answer = (seat_manager(row, n, side, position))
        if answer is not None:
            number = rows.index(row)
            rows[number] = answer
            seats_found = True
            break
    if seats_found:
        print(info_about_tickets(n, number, answer))
        print(*rows, sep='\n')
        rows[number] = rows[number].replace('X', '#')
    else:
        print('Cannot fulfill passengers requirements')
