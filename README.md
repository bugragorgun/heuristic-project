
## How To Use(Pac-Man Search Project)

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/) installed on your computer. From your command line:

```bash

# Clone this repository
$ git clone https://github.com/bugragorgun/heuristic-project/

# To run DFS
$ python pacman.py -l tinyMaze -p SearchAgent
$ python pacman.py -l mediumMaze -p SearchAgent
$ python pacman.py -l bigMaze -z .5 -p SearchAgent

# To run DFS(Recursive)
$ python pacman.py -l tinyMaze -p SearchAgent -a fn=dfsr
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=dfsr
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfsr

# To run BFS
$ python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=bfs

# To run BFS(Recursive)
$ python pacman.py -l tinyMaze -p SearchAgent -a fn=bfsr
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=bfsr
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=bfsr

# To run UCS
$ python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=ucs

# To run A*(Manhattan)
$ python pacman.py -l tinyMaze -p SearchAgent -a fn=astar
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=astar
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar

```

## How To Use(Genetic Algorithm Three Hump Camel)
```bash
$ python three_hump_camel.py
```
---

