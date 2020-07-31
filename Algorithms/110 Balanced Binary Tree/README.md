The time complexity of "recursive_top-down" is O(nlogn).

The time complexity of "recursive_bottom-up" is O(n). 

"recursive_bottom-up" runs faster than "recursive_top-down" because in "recursive_top-down", the depth of nodes are calculated more than one time.

While in "recursive_bottom-up", it judges whether the subtrees are balanced trees first and then judges whether the father node is balanced by comparing the depths of the subtrees.