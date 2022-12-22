# Day 12: Hill Climbing Algorithm

## Part 1

You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where _a_ is the lowest elevation, _b_ is the next-lowest, and so on up to the highest elevation, _z_.

Also included on the heightmap are marks for your current position (_S_) and the location that should get the best signal (E). Your current position (_S_) has elevation a, and the location that should get the best signal (_E_) has elevation z.

You'd like to reach _E_, but to save energy, you should do it in **as few steps as possible**. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be **at most one higher** than the elevation of your current square; that is, if your current elevation is _m_, you could step to elevation _n_, but not to elevation _o_. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:
```
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
```

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the _e_ at the bottom. From there, you can spiral around to the goal:
```
v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
```

In the above diagram, the symbols indicate whether the path exits each square moving up (_^_), down (_v_), left (_<_), or right (_>_). The location that should get the best signal is still _E_, and _._ marks unvisited squares.

This path reaches the goal in _**31**_ steps, the fewest possible.

**What is the fewest steps required to move from your current position to the location that should get the best signal?**

```
python solve01.py -i input.txt
```


## Part 2


```
python solve02.py -i input.txt
```
