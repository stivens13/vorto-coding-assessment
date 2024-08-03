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
### Genetic Algorithm
   Promising direction that would provide better cost efficiency with longer run time. Faced difficulties implementing a more cost-efficient solution - my results for a quick and dirty solution were worse than Greedy Insertion Algorithm
   
### Neo4j
   Rather unorthodox but theoretically workable approach. In the materials I've read, neo4j or similar graph databases weren't mentioned, but using graph databases might be an efficient and effective approach 