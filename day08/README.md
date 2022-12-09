# Day 8: Treetop Tree House

## Part 1

The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a [tree house](https://en.wikipedia.org/wiki/Tree_house).

First, determine whether there is enough tree cover here to keep a tree house **hidden**. To do this, you need to count the number of trees that are **visible from outside the grid** when looking directly along a row or column.

The Elves have already launched a [quadcopter](https://en.wikipedia.org/wiki/Quadcopter) to generate a map with the height of each tree (your puzzle input). For example:

```
30373
25512
65332
33549
35390
```

Each tree is represented as a single digit whose value is its height, where _0_ is the shortest and _9_ is the tallest.

A tree is **visible** if all of the other trees between it and an edge of the grid are **shorter** than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are **visible** - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the **interior nine trees** to consider:

 - The top-left _5_ is **visible** from the left and top. (It isn't visible from the right or bottom since other trees of height _5_ are in the way.)
 - The top-middle _5_ is **visible** from the top and right.
 - The top-right _1_ is not visible from any direction; for it to be visible, there would need to only be trees of height **0** between it and an edge.
 - The left-middle _5_ is **visible**, but only from the right.
 - The center _3_ is not visible from any direction; for it to be visible, there would need to be only trees of at most height _2_ between it and an edge.
 - The right-middle _3_ is **visible** from the right.
 - In the bottom row, the middle _5_ is **visible**, but the _3_ and _4_ are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of _**21**_ trees are visible in this arrangement.

Consider your map; **how many trees are visible from outside the grid?**

```
python solve01.py -i input.txt
```


## Part 2

Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of **trees**.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large [eaves](https://en.wikipedia.org/wiki/Eaves) to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle _5_ in the second row:

```
30373
25512
65332
33549
35390
```

 - Looking up, its view is not blocked; it can see _**1**_ tree (of height 3).
 - Looking left, its view is blocked immediately; it can see only _**1**_ tree (of height _5_, right next to it).
 - Looking right, its view is not blocked; it can see _**2**_ trees.
 - Looking down, its view is blocked eventually; it can see _**2**_ trees (one of height _3_, then the tree of height _5_ that blocks its view).

A tree's **scenic score** is found by **multiplying together** its viewing distance in each of the four directions. For this tree, this is _**4**_ (found by multiplying _1 * 1 * 2 * 2_).

However, you can do even better: consider the tree of height _5_ in the middle of the fourth row:

```
30373
25512
65332
33549
35390
```

 - Looking up, its view is blocked at _**2**_ trees (by another tree with a height of _5_).
 - Looking left, its view is not blocked; it can see _**2**_ trees.
 - Looking down, its view is also not blocked; it can see _**1**_ tree.
 - Looking right, its view is blocked at _**2**_ trees (by a massive tree of height _9_).

This tree's scenic score is _**8**_ (_2 * 2 * 1 * 2_); this is the ideal spot for the tree house.

Consider each tree on your map. **What is the highest scenic score possible for any tree?**

```
python solve02.py -i input.txt
```
