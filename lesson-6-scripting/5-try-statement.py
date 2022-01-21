while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError:
        print('A valid number, please! Enter again: ')
    except KeyboardInterrupt:
        print('No input taken')
        break
    finally:
        print('Attempted input.')
