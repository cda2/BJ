import java.util.stream.Stream
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.api.*
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.params.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import BJ1012.Pos

class BJ1012Test {
    val solution = BJ1012::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 1012 테스트`(m: Int, n: Int, cabbages: List<Pos>, expected: Int) {
        assertEquals(expected, solution(m, n, cabbages))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    10,
                    8,
                    arrayListOf(
                        Pos(0, 0),
                        Pos(1, 0),
                        Pos(1, 1),
                        Pos(4, 2),
                        Pos(4, 3),
                        Pos(4, 5),
                        Pos(2, 4),
                        Pos(3, 4),
                        Pos(7, 4),
                        Pos(8, 4),
                        Pos(9, 4),
                        Pos(7, 5),
                        Pos(8, 5),
                        Pos(9, 5),
                        Pos(7, 6),
                        Pos(8, 6),
                        Pos(9, 6)
                    ),
                    5
                ),
                Arguments.of(10, 10, arrayListOf(Pos(0, 0)), 1)
            )
        }
    }
}
