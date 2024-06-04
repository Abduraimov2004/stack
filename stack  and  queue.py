import random


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)


stack = Stack()
queue = Queue()


def run1():
    tanla = input("""
    1.> Queue
    2.> Stack
            >>> : """)
    if tanla == "1":
        tanla1 = input("""
        1.> Malumotlarni qolda kiritish
        2.> Tayyor malumotdan foydalanish
                >>> : """)
        if tanla1 == "1":
            push = int(input("Nechta malumot qoshmoqchisiz : "))
            for i in range(1, push + 1):
                print(i)
                malumot = input(">>> :")
                try:
                    queue.enqueue(int(malumot))
                except ValueError:
                    queue.enqueue(malumot)
            print("Malumotlar qoshildi")
            tanla3: str = '1'
            while tanla3 == '1':

                tanlang: str = input("""
                1.> Yana malumot qoshish
                2.> Biror bir malumotni ochirib tashlash
                3.> Biror bir malumotni ko'rish
                        >>> : """)
                if tanlang == "1":
                    push = int(input("Nechta malumot qoshmoqchisiz : "))
                    for i in range(1, push + 1):
                        print(i)
                        malumot = input(">>> :")
                        try:
                            queue.enqueue(int(malumot))
                        except ValueError:
                            queue.enqueue(malumot)
                    print("Malumotlar qoshildi")



                elif tanlang == "2":
                    print(queue.items)
                    net = input("""
                    1.> ohiridan 1 ta elementni ochirish
                    2.> Ixtiyoriy elementni ochirish
                                >>> : """)
                    if net == "1":
                        queue.dequeue()
                        print(queue.items)
                    elif net == "2":
                        kiriting = input(">>> : ")
                        try:
                            for i in queue.items:
                                ixtiyoriy1 = int(kiriting)
                                if i == ixtiyoriy1:
                                    queue.items.remove(ixtiyoriy1)
                                    print(queue.items)
                                    break
                            else:
                                print("Topilmadi")

                        except ValueError:
                            for i in queue.items:
                                if i == kiriting:
                                    queue.items.remove(kiriting)
                                    print(queue.items)
                                    break
                            else:
                                print("Topilmadi")
                elif tanlang == "3":
                    print(queue.items)
                    kirit = input("""
                    1.> Ohiridagi elementni ko'rish
                    2.> Ixtiyoriy elementni ko'rish
                                >>> : """)
                    if kirit == "1":
                        queue.peek()
                        print(queue.items)
                    elif kirit == "2":
                        ixtiyoriy = input(">>> :")
                        try:
                            for i in queue.items:
                                ixtiyoriy1 = int(ixtiyoriy)
                                if i == ixtiyoriy1:
                                    print(i)
                                    print(queue.items)
                                    break
                            else:
                                print("Topilmadi")

                        except ValueError:
                            for i in queue.items:
                                if i == ixtiyoriy:
                                    print(i)
                                    print(queue.items)
                                    break
                            else:

                                print("Topilmadi")
                tanla3 = input("""Davom etirmoqchimisiz
                1.> Ha
                2.> Yoq
                        >>> : """)
            return



        if tanla1 == "2":
            queue.items.extend(["assalom", "hello", 20, 66, True])
            print(queue.items)
            tanla3 = "1"
            while tanla3 == "1":
                tanlang = input("""
                1.> Yana malumot qoshish
                2.> Biror bir malumotni ochirib tashlash
                3.> Biror bir malumotni ko'rish
                        >>> : """)
                if tanlang == "1":
                    push = int(input("Nechta malumot qoshmoqchisiz : "))
                    for i in range(1, push + 1):
                        print(i)
                        malumot = input(">>> :")
                        try:
                            queue.enqueue(int(malumot))
                        except ValueError:
                            queue.enqueue(malumot)
                    print("Malumotlar qoshildi")
                elif tanlang == "2":
                    print(queue.items)
                    net = input("""
                    1.> ohiridan 1 ta elementni ochirish
                    2.> Ixtiyoriy elementni ochirish
                                >>> : """)
                    if net == "1":
                        queue.dequeue()
                        print(queue.items)
                    elif net == "2":
                        kiriting = input(">>> : ")
                        try:
                            for i in queue.items:
                                ixtiyoriy1 = int(kiriting)
                                if i == ixtiyoriy1:
                                    queue.items.remove(ixtiyoriy1)
                                    print(queue.items)
                                    break
                            else:
                                print("Topilmadi")

                        except ValueError:
                            for i in queue.items:
                                if i == kiriting:
                                    queue.items.remove(kiriting)
                                    print(queue.items)
                                    break
                            else:
                                print("Topilmadi")
                elif tanlang == "3":
                    print(queue.items)
                    kirit = input("""
                    1.> Ohiridagi elementni ko'rish
                    2.> Ixtiyoriy elementni ko'rish
                                >>> : """)
                    if kirit == "1":
                        queue.peek()
                        print(queue.items)
                    elif kirit == "2":
                        ixtiyoriy = input(">>> :")
                        try:
                            for i in queue.items:
                                ixtiyoriy1 = int(ixtiyoriy)
                                if i == ixtiyoriy1:
                                    print(i)
                                    print(queue.items)
                                    break
                            else:
                                print("Topilmadi")

                        except ValueError:
                            for i in queue.items:
                                if i == ixtiyoriy:
                                    print(i)
                                    print(queue.items)
                                    break
                            else:
                                print("Topilmadi")
                tanla3 = input("""Davom etirmoqchimisiz
                1.> Ha
                2.> Yoq
                        >>> : """)
            return
    elif tanla == "2":
        tanla2 = input("""
        1.> Malumotlarni qolda kiritish
        2.> Tayyor malumotdan foydalanish
                >>> : """)
        if tanla2 == "1":
            push = int(input("Nechta malumot qoshmoqchisiz : "))
            for i in range(1, push + 1):
                print(i)
                malumot = input(">>> :")
                try:
                    stack.push(int(malumot))
                except ValueError:
                    stack.push(malumot)
            print("Malumotlar qoshildi")
            tanla3 = "1"
            while tanla3 == "1":
                tanlang = input("""
                1.> Yana malumot qoshish
                2.> Biror bir malumotni ochirib tashlash
                3.> Biror bir malumotni ko'rish
                        >>> : """)
                if tanlang == "1":
                    push = int(input("Nechta malumot qoshmoqchisiz : "))
                    for i in range(1, push + 1):
                        print(i)
                        malumot = input(">>> :")
                        try:
                            stack.push(int(malumot))
                        except ValueError:
                            stack.push(malumot)
                    print("Malumotlar qoshildi")
                elif tanlang == "2":
                    print(stack.items)
                    net = input("""
                    1.> ohiridan 1 ta elementni ochirish
                    2.> Ixtiyoriy elementni ochirish
                                >>> : """)
                    if net == "1":
                        stack.pop()
                        print(stack.items)
                    elif net == "2":
                        kiriting = input(">>> : ")
                        try:
                            for i in stack.items:
                                ixtiyoriy1 = int(kiriting)
                                if i == ixtiyoriy1:
                                    stack.items.remove(ixtiyoriy1)
                                    print(stack.items)
                                    break
                            else:
                                print("Topilmadi")

                        except ValueError:
                            for i in stack.items:
                                if i == kiriting:
                                    stack.items.remove(kiriting)
                                    print(stack.items)
                                    break
                            else:
                                print("Topilmadi")
                elif tanlang == "3":
                    print(stack.items)
                    kirit = input("""
                    1.> Ohiridagi elementni ko'rish
                    2.> Ixtiyoriy elementni ko'rish
                                >>> : """)
                    if kirit == "1":
                        stack.peek()
                        print(stack.items)
                    elif kirit == "2":
                        ixtiyoriy = input(">>> :")
                        try:
                            for i in stack.items:
                                ixtiyoriy1 = int(ixtiyoriy)
                                if i == ixtiyoriy1:
                                    print(i)
                                    print(stack.items)
                                    break
                            else:
                                print("Topilmadi")

                        except ValueError:
                            for i in stack.items:
                                if i == ixtiyoriy:
                                    print(i)
                                    print(stack.items)
                                    break
                            else:
                                print("Topilmadi")
                tanla3 = input("""Davom etirmoqchimisiz
                1.> Ha
                2.> Yoq
                        >>> : """)
            return

        elif tanla2 == "2":
            stack.items.extend([4, "ali", 20, "salom", 88, 19])
            print(stack.items)
            tanla3 = "1"

            while tanla3 == "1":
                tanlang = input("""
                1.> Yana malumot qoshish
                2.> Biror bir malumotni ochirib tashlash
                3.> Biror bir malumotni ko'rish
                        >>> : """)
                if tanlang == "1":
                    push = int(input("Nechta malumot qoshmoqchisiz : "))
                    for i in range(1, push + 1):
                        print(i)
                        malumot = input(">>> :")
                        try:
                            stack.push(int(malumot))
                        except ValueError:
                            stack.push(malumot)
                    print("Malumotlar qoshildi")
                elif tanlang == "2":
                    print(stack.items)
                    net = input("""
                    1.> ohiridan 1 ta elementni ochirish
                    2.> Ixtiyoriy elementni ochirish
                                >>> : """)
                    if net == "1":
                        stack.pop()
                        print(stack.items)
                    elif net == "2":
                        kiriting = input(">>> : ")
                        try:
                            for i in stack.items:
                                ixtiyoriy1 = int(kiriting)
                                if i == ixtiyoriy1:
                                    stack.items.remove(ixtiyoriy1)
                                    print(stack.items)
                                    break
                            else:
                                print("Topilmadi")

                        except ValueError:
                            for i in stack.items:
                                if i == kiriting:
                                    stack.items.remove(kiriting)
                                    print(stack.items)
                                    break
                            else:
                                print("Topilmadi")
                elif tanlang == "3":
                    print(stack.items)
                    kirit = input("""
                    1.> Ohiridagi elementni ko'rish
                    2.> Ixtiyoriy elementni ko'rish
                                >>> : """)
                    if kirit == "1":
                        stack.peek()
                        print(stack.items)
                    elif kirit == "2":
                        ixtiyoriy = input(">>> :")
                        try:
                            for i in stack.items:
                                ixtiyoriy1 = int(ixtiyoriy)
                                if i == ixtiyoriy1:
                                    print(i)
                                    print(stack.items)
                                    break
                            else:
                                print("Topilmadi")

                        except ValueError:
                            for i in stack.items:
                                if i == ixtiyoriy:
                                    print(i)
                                    print(stack.items)
                                    break
                            else:
                                print("Topilmadi")
                tanla3 = input("""Davom etirmoqchimisiz
                1.> Ha
                2.> Yoq
                        >>> : """)
            return



def binar_search() -> None:
    numbers = random.sample(range(1, 100), 30)
    numbers.sort()
    print(numbers)
    target: int = int(input("Qidiriladigan sonni kiriting: "))
    low: int = 0
    lenght = len(numbers) - 1
    count: int = 0
    while low <= lenght:
        mid: int = (low + lenght) // 2
        a: int = numbers[mid]
        print(a)
        count += 1
        if a == target:
            print(f"Siz kiritgan sonni {count} urinishda topdingiz")
            break
        elif a < target:
            low = mid + 1
        else:
            lenght = mid - 1
    else:
        print("Kiritilgan son topilmadi")


def linear_search() -> None:
    print("[1 ___ 30]")
    target = int(input(" son =>"))
    n = 0
    while n < 31:
        n += 1
        if n == target:
            print(f"""Misol qiymati {target} 
        {n}-urinishda topdingiz""")
            break

    else:
        print("Qiymat topilmadi")





def run() -> None:
    next: str = input("""
    1.> Binary search
    2.> Linear search
            >>>> """)

    if next == '1':
        return binar_search()
    elif next == '2':
        return linear_search()



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("Error")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def check(self, data):
        if self.head is None:
            return None
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def deleted(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None


list_qolda = []


def tayyor() -> None:
    l_list = LinkedList()
    list_qolda = []
    for i in range(1, 11):
        list_qolda.append(i)
    l_list.head = Node(list_qolda[0])
    for j in list_qolda[1:]:
        l_list.append(j)
    l_list.printList()




def qolda():
    l_list = LinkedList()
    tugun: int = int(input("Nechta tugun yaratmoqchisiz: "))
    if tugun > 0:
        tugun_boshi: int = int(input("Tugundi boshi >>> : "))
        list_qolda.insert(0, tugun_boshi)
        while tugun > 1:
            davomi = int(input("Tugundi davomi > :"))
            list_qolda.append(davomi)
            tugun -= 1
    l_list.head = Node(list_qolda[0])
    for j in list_qolda[1:]:
        l_list.append(j)
    l_list.printList()



def q_amallar():
    l_list = LinkedList()
    if len(list_qolda) > 0:
        tanlang = input("""
        1.> Push
        2.> Insert
        3.> Append
                >>> : """)
        if tanlang == "1":
            tugun1 = int(input("Tugundi boshini ozgartrish  >>> : "))
            list_qolda.insert(0, tugun1)

            for j in list_qolda:
                l_list.append(j)
            l_list.printList()
            tanla = input("""Davom etirmoqchimisiz
            1.> Ha
            2.> Yoq
                    >>> : """)
            if tanla == "1":
                return q_amallar()
            else:
                return
        elif tanlang == "2":
            data = int(input("Tugunni kiriting: "))
            l_list.printList()
            prev_data = int(input("Qaysi tugundan kegin qoshmoqchisiz: "))
            list_qolda.insert(prev_data, data)
            for j in list_qolda:
                l_list.append(j)
            prev_node = l_list.check(prev_data)
            if prev_node is None:
                print("Oldingi tugun mavjud emas")
            else:
                l_list.insert(prev_node, data)
            l_list.printList()
            tanla = input("""Davom etirmoqchimisiz
            1.> Ha
            2.> Yoq
                    >>> : """)
            if tanla == "1":
                return q_amallar()
            else:
                return
        elif tanlang == "3":
            data = int(input("Tugunni kiriting: "))
            list_qolda.append(data)
            for j in list_qolda:
                l_list.append(j)
            l_list.printList()
            tanla = input("""Davom etirmoqchimisiz
            1.> Ha
            2.> Yoq
                    >>> : """)
            if tanla == "1":
                return q_amallar()
            else:
                return
        else:
            print("Noto'g'ri tanlov")
    else:
        print("Hozirda Data bo'sh uni toldiring")
        tanla = input("""
        1.> Qolda qoshish 
        2.> Tayyor data 
         3.> Back
                >>>> : """)

        if tanla == "1":
            return qolda(), q_amallar()
        elif tanla == "2":
            l_list = LinkedList()
            for i in range(1, 11):
                list_qolda.append(i)
            l_list.head = Node(list_qolda[0])
            for j in list_qolda[1:]:
                l_list.append(j)
            l_list.printList()
            return q_amallar()
        else:
            return


def run2():
    tugadi = input("""
    1.> Search
    2.> Linked list
    3.> Stack/Queue
                >>> : """)
    if tugadi == "1":
        return run()
    elif tugadi == "2":
        return q_amallar()
    elif tugadi == "3":
        return run1()


run2()

