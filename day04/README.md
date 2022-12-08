# Day 4: Camp Cleanup

## Part 1

Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique **ID number**, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments **overlap**. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a **big list of the section assignments for each pair** (your puzzle input).

For example, consider the following list of section assignment pairs:

```
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
```

For the first few pairs, this list means:

 - Within the first pair of Elves, the first Elf was assigned sections _2-4_ (sections _2_, _3_, and _4_), while the second Elf was assigned sections _6-8_ (sections _6_, _7_, _8_).
 - The Elves in the second pair were each assigned two sections.
 - The Elves in the third pair were each assigned three sections: one got sections _5_, _6_, and _7_, while the other also got _7_, plus _8_ and _9_.

This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

```
.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
```

Some of the pairs have noticed that one of their assignments fully contains the other. For example, _2-8_ fully contains _3-7_, and _6-6_ is fully contained by _4-6_. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are _**2**_ such pairs.

**In how many assignment pairs does one range fully contain the other?**

```
python solve01.py -i input.txt
```


## Part 2

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that **overlap at all**.

In the above example, the first two pairs (_2-4,6-8_ and _2-3,4-5_) don't overlap, while the remaining four pairs (_5-7,7-9_, _2-8,3-7_, _6-6,4-6_, and _2-6,4-8_) do overlap:

 - _5-7,7-9_ overlaps in a single section, _7_.
 - _2-8,3-7_ overlaps all of the sections _3_ through _7_.
 - _6-6,4-6_ overlaps in a single section, _6_.
 - _2-6,4-8_ overlaps in sections _4_, _5_, and _6_.

So, in this example, the number of overlapping assignment pairs is _**4**_.

**In how many assignment pairs do the ranges overlap?**

```
python solve02.py -i input.txt
```
