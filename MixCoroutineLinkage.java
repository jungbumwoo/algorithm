public class MixCoroutineLinkage {

    // ── 레이블(프로그램 카운터 대용) ──────────────────────────────
    static final int A1 = 1, A2 = 2, A3 = 3, A_DONE = 9;
    static final int B1 = 11, B2 = 12, B3 = 13, B_DONE = 19;

    public static void main(String[] args) throws InterruptedException {
        // AX, BX = "JMP 슬롯" (최초엔 각 코루틴의 시작점)
        int AX = A1;  // AX: JMP A1 과 같은 효과
        int BX = B1;  // BX: JMP B1

        // 각 코루틴의 현재 PC(어느 레이블에 있는지)
        int aPC = A1;
        int bPC = B1;

        // 누가 현재 실행 중인지
        char cur = 'A';

        int steps = 0;
        final int MAX_STEPS = 16;

        // 두 코루틴이 모두 끝날 때까지 실행
        while ((aPC != A_DONE || bPC != B_DONE) && steps++ < MAX_STEPS) {
            Thread.sleep(500);
            if (cur == 'A') {
                switch (aPC) {
                    case A1:
                        System.out.println("A1: A 시작");
                        // 다음으로
                        aPC = A2;
                        break;

                    case A2:
                        System.out.println("A2: B에게 넘긴다 (JMP B)");
                        // MIX 관점: JMP B
                        // 1) rJ = A2 다음(A3)
                        int rJ_A_to_B = A3;
                        // 2) STJ AX  → AX := rJ (A로 돌아올 때 A3로)
                        AX = rJ_A_to_B;
                        // 3) JMP BX
                        // BX로 점프
                        bPC = BX;
                        cur = 'B';
                        break;

                    case A3:
                        System.out.println("A3: B에서 돌아와 A 계속 실행");
                        // A 종료
                        aPC = A_DONE;
                        System.out.println("A_DONE");
                        // A가 끝났어도 B가 안 끝났으면 B를 계속 실행
                        if (bPC != B_DONE) {
                            bPC = BX;
                            cur = 'B';
                        }
                        break;

                    case A_DONE:
                        // 이미 끝났으면 B 쪽으로 넘김
                        if (bPC != B_DONE) cur = 'B';
                        break;
                }

            } else { // cur == 'B'
                switch (bPC) {
                    case B1:
                        System.out.println("B1: B 시작");
                        bPC = B2;
                        break;

                    case B2:
                        System.out.println("B2: A에게 넘긴다 (JMP A)");
                        // MIX 관점: JMP A
                        // 1) rJ = B2 다음(B3)
                        int rJ_B_to_A = B3;
                        // 2) STJ BX  → BX := rJ (B로 돌아올 때 B3로)
                        BX = rJ_B_to_A;
                        // 3) JMP AX: AX로 점프
                        aPC = AX;
                        cur = 'A';
                        break;

                    case B3:
                        System.out.println("B3: A에서 돌아와 B 계속 실행");
                        bPC = B_DONE;
                        System.out.println("B_DONE");
                        if (aPC != A_DONE) {
                            aPC = AX;
                            cur = 'A';
                        };
                        break;

                    case B_DONE:
                        if (aPC != A_DONE) cur = 'A';
                        break;
                }
            }

            if (steps >= MAX_STEPS) {
            System.err.println("Guard triggered: too many steps (possible infinite loop).");
            } else {
                System.out.println("둘 다 종료.");
            }
        }
        System.out.println("둘 다 종료.");
    }
}
