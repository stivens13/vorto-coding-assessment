# Vorto Algorithmic Challenge

## Solution - Greedy Insertion Algorithm
Greedy Insertion provides fast solution with relatively optimal results being a great feat for real-time or time-limited application.

Mean cost results are persistent, however, mean time is strongly dependent on environment - I was receiving best results in PyCharm Terminal in clean conda env while Warp Terminal and cluttered Python interpreters yielded slower results.  

![img.png](data/greedy_results.png)

## How to run

1. (Optional) Create new lean conda environment to ensure consistency of results and reduce the risk of cluttered Python interpreter slowing down the solution execution. 
    ```
    conda env create -f vorto-nikita-env.yml
    conda activate vorto-nikita
    ```

2. Run the evaluator for Greedy Insertion Algorithm
    ```
    python3 evaluateShared.py --cmd "python3 greedy.py" --problemDir "problemset" 
    ```

## Other approaches attempted
### Savings Algorithm
   Clarke-Wright infamous and VRP-defining algorithm. I wanted to try this approach but found a few almost exact implementations to the assessment problem and felt like it wouldn't be fare to use it. However, this algorithm's cost optimization efficiency is incredible and outperforms Greedy Algorithm  

### Genetic Algorithm
   Promising direction that would provide better cost efficiency with longer run time. Faced difficulties implementing a more cost-efficient solution - my results for a quick and dirty solution were worse than Greedy Insertion Algorithm
   
### Neo4j
   Rather unorthodox but theoretically workable approach. In the materials I've read, neo4j or similar graph databases weren't mentioned, but using graph databases might be an efficient and effective approach. This approach took too long in short time-frame I had, but worth exploring 

Resource used:
1. https://en.wikipedia.org/wiki/Vehicle_routing_problem
2. https://ieeexplore.ieee.org/document/9194245
3. https://web.mit.edu/urban_or_book/www/book/chapter6/6.4.12.html
4. https://link.springer.com/article/10.1007/s10479-017-2722-x
5. https://neo.lcc.uma.es/vrp/solution-methods/heuristics/multi-route-improvement-algorithm/
6. https://www.displayr.com/what-is-a-distance-matrix/