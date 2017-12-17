import queue

def main():
    q = queue.Queue()
    q.set(10)
    print(q.sortMax())
    print(q.sortMin())
    print(q.outputQueue())
    print(q.deleteFromQueue())
    print(q.deleteFromQueue())
    print(q.deleteFromQueue())

    print(q.outputQueue())

if __name__ == '__main__':
    main()
