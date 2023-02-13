import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ2630Test {
    val solution = BJ2630::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 2630 테스트`(arr: Array<IntArray>, expected: Pair<Int, Int>) {
        assertEquals(expected, solution(arr))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    arrayOf(
                        intArrayOf(1, 1, 0, 0, 0, 0, 1, 1),
                        intArrayOf(1, 1, 0, 0, 0, 0, 1, 1),
                        intArrayOf(0, 0, 0, 0, 1, 1, 0, 0),
                        intArrayOf(0, 0, 0, 0, 1, 1, 0, 0),
                        intArrayOf(1, 0, 0, 0, 1, 1, 1, 1),
                        intArrayOf(0, 1, 0, 0, 1, 1, 1, 1),
                        intArrayOf(0, 0, 1, 1, 1, 1, 1, 1),
                        intArrayOf(0, 0, 1, 1, 1, 1, 1, 1)
                    ),
                    Pair(9, 7)
                )
            )
        }
    }
}
