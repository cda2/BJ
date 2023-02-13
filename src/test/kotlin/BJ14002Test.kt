import io.kotest.core.spec.style.FunSpec
import io.kotest.matchers.shouldBe

class BJ14002Test :
    FunSpec({
        val solution = BJ14002()::solution

        test("테스트 케이스 1") { solution(intArrayOf(1)) shouldBe listOf(1) }

        test("테스트 케이스 2") { solution(intArrayOf(3, 3, 2, 3)) shouldBe listOf(2, 3) }

        test("테스트 케이스 3") {
            solution(intArrayOf(10, 20, 10, 30, 20, 50)) shouldBe listOf(10, 20, 30, 50)
        }

        test("테스트 케이스 4") {
            solution(intArrayOf(2, 8, 4, 9, 5, 1, 7, 6, 3)) shouldBe listOf(2, 4, 5, 6)
        }

        test("테스트 케이스 5") {
            solution(intArrayOf(1, 6, 2, 4, 5, 3, 7)) shouldBe listOf(1, 2, 4, 5, 7)
        }

        test("테스트 케이스 6") { solution(intArrayOf(1, 5, 6, 2, 3, 4)) shouldBe listOf(1, 2, 3, 4) }

        test("테스트 케이스 7") {
            solution(intArrayOf(1, 7, 3, 2, 5, 10, 3)) shouldBe listOf(1, 2, 5, 10)
        }
    })
