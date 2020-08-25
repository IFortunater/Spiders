if __name__ == '__main__':
    l2 = [2, 3, 4]
    l = [1, [1, 2], {1:2, 3:4}, l2]
    l2.append(5)
    print(l.__str__())
