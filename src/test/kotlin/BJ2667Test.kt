import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ2667Test {
    val solution = BJ2667::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 2667 테스트`(n: Int, arr: Array<IntArray>, expected: List<Int>) {
        assertEquals(expected, solution(n, arr))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    7,
                    arrayOf(
                        intArrayOf(0, 1, 1, 0, 1, 0, 0),
                        intArrayOf(0, 1, 1, 0, 1, 0, 1),
                        intArrayOf(1, 1, 1, 0, 1, 0, 1),
                        intArrayOf(0, 0, 0, 0, 1, 1, 1),
                        intArrayOf(0, 1, 0, 0, 0, 0, 0),
                        intArrayOf(0, 1, 1, 1, 1, 1, 0),
                        intArrayOf(0, 1, 1, 1, 0, 0, 0)
                    ),
                    listOf(7, 8, 9)
                )
            )
        }
    }
}
