import io.kotest.core.spec.style.FunSpec
import io.kotest.matchers.shouldBe

class BJ1013Test :
    FunSpec({
        val solution = BJ1013()::solution

        test("테스트 케이스 1") { solution("10010111") shouldBe "NO" }
        test("테스트 케이스 2") { solution("011000100110001") shouldBe "NO" }
        test("테스트 케이스 3") { solution("0110001011001") shouldBe "YES" }
    })
