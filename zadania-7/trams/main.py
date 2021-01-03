import json, time, random


def makeGraph(tramJson):
    graph = dict()
    dist = 1

    for i in range(len(tramJson["tramwaje"])):
        tprzystanki = tramJson["tramwaje"][i]["tprzystanki"]
        stopsList = list()

        for przystanek in tprzystanki:
            if not przystanek["name"] in graph.keys():
                graph[przystanek["name"]] = list()
            stopsList.append(przystanek["name"])

        for k in range(len(stopsList)):
            if k == 0:
                if not (stopsList[1], dist) in graph[stopsList[k]]:
                    graph[stopsList[k]].append((stopsList[1], dist))

            elif k == len(stopsList) - 1:
                if not (stopsList[k - 1], dist) in graph[stopsList[k]]:
                    graph[stopsList[k]].append((stopsList[k - 1], dist))

            else:
                if not (stopsList[k - 1], dist) in graph[stopsList[k]]:
                    graph[stopsList[k]].append((stopsList[k - 1], dist))
                if not (stopsList[k + 1], dist) in graph[stopsList[k]]:
                    graph[stopsList[k]].append((stopsList[k + 1], dist))

    return graph


def printPath(start, end):
    print(start + ' -> ' + end, end=' ,ilość przystanków: ')


def dijkstra(graph, start, end):

    printPath(start, end)

    timeStart = time.time()

    nodes = choseNodes(graph, start)

    nodesToCheck = set(graph.keys())
    minimum = nodes[start][0]
    min = start

    while nodesToCheck.__len__() > 0:
        for currNode in nodesToCheck:
            if minimum > nodes[currNode][0] > 0:
                minimum = nodes[currNode][0]
                min = currNode

        nodesToCheck.remove(min)

        for k in graph[min]:
            neighbour = k[0]

            if nodes[neighbour][0] > nodes[min][0] + 1:
                nodes[neighbour][0] = nodes[min][0] + 1
                nodes[neighbour][1] = min

        if nodesToCheck.__len__() > 0:
            minimum = nodes[list(nodesToCheck)[0]][0]
            min = list(nodesToCheck)[0]

    timeStop = time.time() - timeStart
    return nodes[end][0], timeStop

def choseNodes(graph, start):
    nodes = dict()
    for node in graph.keys():
        nodes[node] = []

        if node != start:
            nodes[node].append(888)
        else:
            nodes[node].append(0)
        nodes[node].append("")

    return nodes


def bellmanFord(graph, start, end):
    printPath(start, end)

    timeStart = time.time()

    nodes = choseNodes(graph, start)
    nodesToCheck = set(graph.keys())
    neighbourToCheck = [start]

    while nodesToCheck.__len__() > 0:
        temp = neighbourToCheck[0]
        del neighbourToCheck[0]
        nodesToCheck.remove(temp)

        for node in graph[temp]:
            neighbour = node[0]

            if (neighbour in nodesToCheck) and not (neighbour in neighbourToCheck):
                neighbourToCheck.append(neighbour)

            if nodes[neighbour][0] > nodes[temp][0] + 1:
                nodes[neighbour][0] = nodes[temp][0] + 1
                nodes[neighbour][1] = temp

    timeStop = time.time() - timeStart

    return nodes[end][0], timeStop

def average(list):
    return sum(list)/len(list)

def result(graph, iters):
    resultDijkstra = list()
    resultBellman = list()
    for i in range(iters):
        start, end = randomStops(graph)

        dijkstraStops , dijkstraTime = dijkstra(graph, start, end)
        print(dijkstraStops)
        resultDijkstra.append(dijkstraTime)

        bellmanStops , bellmanTime = bellmanFord(graph, start, end)
        print(bellmanStops)
        resultBellman.append(bellmanTime)


    print('\n\nDla ', iters ,'przypadków algorytm Dijkstyry ma średnią: ', average(resultDijkstra))
    print('Dla ', iters,'przypadków algorytm Bellmana Forda ma średnią: ', average(resultBellman))


def randomStops(graph):
    stopsList = list(graph.keys())
    start = random.choice(stopsList)
    end = random.choice(stopsList)
    if start == end:
        randomStops(graph)
    else:
        return start, end


def open_json(fileName):
    with open(fileName, "r", encoding='utf-8') as read_file:
        json_data = json.load(read_file)
    return json_data


if __name__ == '__main__':

    tram_json = open_json('tramwaje.json')

    graph = makeGraph(tram_json)

    result(graph, 30)

