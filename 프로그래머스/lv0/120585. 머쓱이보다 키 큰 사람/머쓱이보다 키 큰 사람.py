def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return len(array[:array.index(height)])