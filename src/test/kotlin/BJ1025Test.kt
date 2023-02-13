import java.util.stream.Stream
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

// 미작동. https://github.com/kotest/kotest/issues/3351 이슈인 듯?
// class BJ1025Test :
//    StringSpec({
//        val realSolution = BJ1025::solution
//
//        fun solution(table: List<String>): Long {
//            return realSolution(table.map { line -> line.split("").map { it.toShort() } })
//        }
//
//        "테스트 케이스." {
//            withData(
//                listOf("123", "234") to 64,
//                listOf("00000", "00000", "00200", "00000", "00000") to 81,
//                listOf("3791178", "1283252", "4103617", "8233494", "8725572", "2937261") to
// 320356) { (input, expected) ->
//                    val answer = solution(input)
//                    answer shouldBe expected
//                }
//        }
//    })

class BJ1025Test {
    private val realSolution = BJ1025::solution

    private fun solution(table: List<String>): Int {
        return realSolution(table.map { line -> line.toCharArray().map { it.digitToInt() } })
    }

    @ParameterizedTest
    @MethodSource("testCases")
    fun `백준 1025 테스트`(table: List<String>, expected: Int) {
        assertEquals(expected, solution(table))
    }

    companion object {
        @JvmStatic
        fun testCases(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(listOf("123", "456"), 64),
                Arguments.of(listOf("00000", "00000", "00200", "00000", "00000"), 0),
                Arguments.of(
                    listOf("3791178", "1283252", "4103617", "8233494", "8725572", "2937261"),
                    320356),
                Arguments.of(
                    listOf("135791357", "357913579", "579135791", "791357913", "913579135"), 9),
                Arguments.of(
                    listOf(
                        "553333733",
                        "775337775",
                        "777537775",
                        "777357333",
                        "755553557",
                        "355533335",
                        "373773573",
                        "337373777",
                        "775557777"),
                    -1),
                Arguments.of(
                    listOf(
                        "257240281",
                        "197510846",
                        "014345401",
                        "035562575",
                        "974935632",
                        "865865933",
                        "684684987",
                        "768934659",
                        "287493867"),
                    95481),
                Arguments.of(listOf("37", "66", "37", "22", "60", "36", "73", "71", "17"), 361),
                Arguments.of(listOf("9"), 9),
                Arguments.of(
                    listOf(
                        "462743547",
                        "342244373",
                        "494474722",
                        "441223774",
                        "233443934",
                        "125444346",
                        "442233332",
                        "323732443"),
                    44521))
        }
    }
}
