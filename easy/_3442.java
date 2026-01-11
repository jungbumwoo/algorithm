package easy;

import java.util.*;

class Solution {
    class Element implements Comparable<Element> {
        int val, count;
        Element(int val, int count) {
            this.val = val;
            this.count = count;
        }

        @Override
        public int compareTo(Element other) {
            if (this.count != other.count) return Integer.compare(this.count, other.count);
            return Integer.compare(this.val, other.val);
        }
    }

    private PriorityQueue<Element> topX = new PriorityQueue<>(); // Min-Heap
    private PriorityQueue<Element> candidates = new PriorityQueue<>(Collections.reverseOrder()); // Max-Heap
    private Map<Integer, Integer> countMap = new HashMap<>();
    private long currentXSum = 0;
    private int topXSize = 0;

    public long[] findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        long[] answer = new long[n - k + 1];

        for (int i = 0; i < n; i++) {
            // 1. 새로운 원소 추가
            add(nums[i], x);

            // 2. 윈도우를 벗어난 원소 제거
            if (i >= k) {
                remove(nums[i - k], x);
            }

            // 3. 결과 저장 (윈도우 크기가 k가 되었을 때부터)
            if (i >= k - 1) {
                cleanHeaps();
                answer[i - k + 1] = currentXSum;
            }
        }
        return answer;
    }

    private void add(int val, int x) {
        int prevCount = countMap.getOrDefault(val, 0);
        // 기존에 topX에 있었다면 제거 (논리적 제거)
        if (prevCount > 0) {
            // 실제 삭제 대신 빈도수 업데이트로 처리 (cleanHeaps에서 정리)
        }
        
        int newCount = prevCount + 1;
        countMap.put(val, newCount);
        
        // 일단 candidates에 넣고 rebalance
        candidates.offer(new Element(val, newCount));
        rebalance(x);
    }

    private void remove(int val, int x) {
        int prevCount = countMap.get(val);
        // 이 로직은 countMap의 상태를 업데이트하는 것이 중요
        if (prevCount == 1) countMap.remove(val);
        else countMap.put(val, prevCount - 1);
        
        // 제거된 원소가 topX에 영향을 줄 수 있으므로 다시 candidates에 넣고 rebalance
        if (prevCount > 0) {
            candidates.offer(new Element(val, prevCount - 1));
        }
        rebalance(x);
    }

    private void rebalance(int x) {
        // 1. candidates에서 가장 좋은 후보를 topX로 이동
        while (!candidates.isEmpty() && topXSize < x) {
            Element best = candidates.poll();
            if (isValid(best)) {
                topX.offer(best);
                currentXSum += (long) best.val * best.count;
                topXSize++;
            }
        }

        // 2. topX의 최소값과 candidates의 최대값 비교 후 교체
        while (!topX.isEmpty() && !candidates.isEmpty()) {
            cleanHeaps();
            Element minTop = topX.peek();
            Element maxCand = candidates.peek();
            
            if (isValid(maxCand) && maxCand.compareTo(minTop) > 0) {
                topX.poll();
                candidates.poll();
                
                currentXSum -= (long) minTop.val * minTop.count;
                currentXSum += (long) maxCand.val * maxCand.count;
                
                topX.offer(maxCand);
                candidates.offer(minTop);
            } else {
                break;
            }
        }
    }

    private void cleanHeaps() {
        while (!topX.isEmpty() && !isValid(topX.peek())) {
            Element invalid = topX.poll();
            currentXSum -= (long) invalid.val * invalid.count;
            topXSize--;
        }
        while (!candidates.isEmpty() && !isValid(candidates.peek())) {
            candidates.poll();
        }
    }

    private boolean isValid(Element e) {
        return e.count > 0 && countMap.getOrDefault(e.val, 0) == e.count;
    }
}

// tree set 이용한 풀이

// class Solution {
//     class Element implements Comparable<Element> {
//         int val, count;
//         Element(int val, int count) {
//             this.val = val;
//             this.count = count;
//         }

//         @Override
//         public int compareTo(Element other) {
//             if (this.count != other.count) return Integer.compare(this.count, other.count);
//             return Integer.compare(this.val, other.val);
//         }
//     }

//     private PriorityQueue<Element> topX = new PriorityQueue<>(); // Min-Heap
//     private PriorityQueue<Element> candidates = new PriorityQueue<>(Collections.reverseOrder()); // Max-Heap
//     private Map<Integer, Integer> countMap = new HashMap<>();
//     private long currentXSum = 0;
//     private int topXSize = 0;

//     public long[] findXSum(int[] nums, int k, int x) {
//         int n = nums.length;
//         long[] answer = new long[n - k + 1];

//         for (int i = 0; i < n; i++) {
//             // 1. 새로운 원소 추가
//             add(nums[i], x);

//             // 2. 윈도우를 벗어난 원소 제거
//             if (i >= k) {
//                 remove(nums[i - k], x);
//             }

//             // 3. 결과 저장 (윈도우 크기가 k가 되었을 때부터)
//             if (i >= k - 1) {
//                 cleanHeaps();
//                 answer[i - k + 1] = currentXSum;
//             }
//         }
//         return answer;
//     }

//     private void add(int val, int x) {
//         int prevCount = countMap.getOrDefault(val, 0);
//         // 기존에 topX에 있었다면 제거 (논리적 제거)
//         if (prevCount > 0) {
//             // 실제 삭제 대신 빈도수 업데이트로 처리 (cleanHeaps에서 정리)
//         }
        
//         int newCount = prevCount + 1;
//         countMap.put(val, newCount);
        
//         // 일단 candidates에 넣고 rebalance
//         candidates.offer(new Element(val, newCount));
//         rebalance(x);
//     }

//     private void remove(int val, int x) {
//         int prevCount = countMap.get(val);
//         // 이 로직은 countMap의 상태를 업데이트하는 것이 중요
//         if (prevCount == 1) countMap.remove(val);
//         else countMap.put(val, prevCount - 1);
        
//         // 제거된 원소가 topX에 영향을 줄 수 있으므로 다시 candidates에 넣고 rebalance
//         if (prevCount > 0) {
//             candidates.offer(new Element(val, prevCount - 1));
//         }
//         rebalance(x);
//     }

//     private void rebalance(int x) {
//         // 1. candidates에서 가장 좋은 후보를 topX로 이동
//         while (!candidates.isEmpty() && topXSize < x) {
//             Element best = candidates.poll();
//             if (isValid(best)) {
//                 topX.offer(best);
//                 currentXSum += (long) best.val * best.count;
//                 topXSize++;
//             }
//         }

//         // 2. topX의 최소값과 candidates의 최대값 비교 후 교체
//         while (!topX.isEmpty() && !candidates.isEmpty()) {
//             cleanHeaps();
//             Element minTop = topX.peek();
//             Element maxCand = candidates.peek();
            
//             if (isValid(maxCand) && maxCand.compareTo(minTop) > 0) {
//                 topX.poll();
//                 candidates.poll();
                
//                 currentXSum -= (long) minTop.val * minTop.count;
//                 currentXSum += (long) maxCand.val * maxCand.count;
                
//                 topX.offer(maxCand);
//                 candidates.offer(minTop);
//             } else {
//                 break;
//             }
//         }
//     }

//     private void cleanHeaps() {
//         while (!topX.isEmpty() && !isValid(topX.peek())) {
//             Element invalid = topX.poll();
//             currentXSum -= (long) invalid.val * invalid.count;
//             topXSize--;
//         }
//         while (!candidates.isEmpty() && !isValid(candidates.peek())) {
//             candidates.poll();
//         }
//     }

//     private boolean isValid(Element e) {
//         return e.count > 0 && countMap.getOrDefault(e.val, 0) == e.count;
//     }
// }

// // tree set 이용한 풀이
// class Solution {
//     class Element implements Comparable<Element> {
//         int val, count;
//         Element(int val, int count) {
//             this.val = val;
//             this.count = count;
//         }

//         @Override
//         public int compareTo(Element o) {
//             if (this.count != o.count) return Integer.compare(this.count, o.count);
//             return Integer.compare(this.val, o.val);
//         }
//     }

//     private TreeSet<Element> topSet = new TreeSet<>();
//     private TreeSet<Element> bottomSet = new TreeSet<>();
//     private Map<Integer, Integer> counts = new HashMap<>();
//     private long currentXSum = 0;

//     public long[] findXSum(int[] nums, int k, int x) {
//         int n = nums.length;
//         long[] result = new long[n - k + 1];

//         for (int i = 0; i < n; i++) {
//             // 1. 새로운 원소 추가
//             update(nums[i], 1, x);

//             // 2. 윈도우 밖 원소 제거
//             if (i >= k) {
//                 update(nums[i - k], -1, x);
//             }

//             // 3. 결과 기록
//             if (i >= k - 1) {
//                 result[i - k + 1] = currentXSum;
//             }
//         }
//         return result;
//     }

//     private void update(int val, int delta, int x) {
//         int oldCount = counts.getOrDefault(val, 0);
//         Element oldElem = new Element(val, oldCount);

//         // 기존에 존재하던 상태 제거
//         if (topSet.contains(oldElem)) {
//             topSet.remove(oldElem);
//             currentXSum -= (long) val * oldCount;
//         } else {
//             bottomSet.remove(oldElem);
//         }

//         // 새로운 빈도수 계산 및 추가
//         int newCount = oldCount + delta;
//         if (newCount > 0) {
//             counts.put(val, newCount);
//             Element newElem = new Element(val, newCount);
//             // 우선 topSet에 넣고 나중에 rebalance
//             topSet.add(newElem);
//             currentXSum += (long) val * newCount;
//         } else {
//             counts.remove(val);
//         }

//         rebalance(x);
//     }

//     private void rebalance(int x) {
//         // 1. topSet이 x개보다 많으면 bottomSet으로 이동
//         while (topSet.size() > x) {
//             Element smallestTop = topSet.pollFirst();
//             currentXSum -= (long) smallestTop.val * smallestTop.count;
//             bottomSet.add(smallestTop);
//         }

//         // 2. topSet이 부족하고 bottomSet에 여유가 있으면 가져오기
//         while (topSet.size() < x && !bottomSet.isEmpty()) {
//             Element largestBottom = bottomSet.pollLast();
//             topSet.add(largestBottom);
//             currentXSum += (long) largestBottom.val * largestBottom.count;
//         }

//         // 3. topSet의 최소값이 bottomSet의 최대값보다 작으면 서로 교체 (순위 역전 방지)
//         while (!topSet.isEmpty() && !bottomSet.isEmpty()) {
//             Element minTop = topSet.first();
//             Element maxBottom = bottomSet.last();

//             if (minTop.compareTo(maxBottom) < 0) {
//                 topSet.pollFirst();
//                 bottomSet.pollLast();

//                 topSet.add(maxBottom);
//                 bottomSet.add(minTop);

//                 currentXSum = currentXSum - ((long) minTop.val * minTop.count) 
//                                         + ((long) maxBottom.val * maxBottom.count);
//             } else {
//                 break;
//             }
//         }
//     }
// }