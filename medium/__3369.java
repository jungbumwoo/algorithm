// Incorrect Answer Note

class Solution {
    public int maxRemoval(int[] nums, int[][] queries) {
        // sort 0 - ascending, 1 ascending
        // nums = [0, 1, 2]
        // [0, 1], [1, 2], [2, 2]
        // priority queue?

        // sort the queries
        // greedily pick the queries with farthest ending point first.

        Arrays.sort(queries, (int[] a, int[] b) -> {
            if (a[0] == b[0]) {
                return Integer.compare(b[1], a[1]);
            }
            return Integer.compare(a[0], b[0]);
        });

        System.out.println(Arrays.deepToString(queries));
        // nums = [0, 1, 2], queries = [[0,1],[1,2],[2,2]]
        // queries를 greedy하게 1차, 왼쪽부터 정렬하고, 긴걸 우선 정렬했더니
        // 여기서 1 index 에 1 value 를 어떻게 처리할지 애매함.
        return 0;
    }
}