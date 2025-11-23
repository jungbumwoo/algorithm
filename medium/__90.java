// 내 풀이 아님
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        Deque<Integer> path = new ArrayDeque<>();
        dfs(nums, 0, path, res);
        return res;
    }

    private void dfs(int[] nums, int start, Deque<Integer> path, List<List<Integer>> res) {
        res.add(new ArrayList<>(path));              // 현재까지 선택한 부분집합 추가
        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i - 1]) // 같은 레벨에서의 중복 건너뛰기
                continue;
            path.addLast(nums[i]);
            dfs(nums, i + 1, path, res);
            path.removeLast();
        }
    }

    public List<List<Integer>> subsetsWithDup2(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<>());

        int i = 0;
        while (i < nums.length) {
            int val = nums[i];
            int cnt = 0;
            while (i < nums.length && nums[i] == val) { i++; cnt++; }

            int size = res.size();
            for (int s = 0; s < size; s++) {
                List<Integer> base = res.get(s);
                // base에 val을 1..cnt개 붙인 버전들을 추가
                List<Integer> cur = new ArrayList<>(base);
                for (int c = 1; c <= cnt; c++) {
                    cur.add(val);
                    res.add(new ArrayList<>(cur));
                }
            }
        }
        return res;
    }
}