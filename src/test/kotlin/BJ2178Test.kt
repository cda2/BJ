import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ2178Test {
    val solution = BJ2178::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 2178 테스트`(n: Int, m: Int, arr: Array<IntArray>, expected: Int) {
        assertEquals(expected, solution(n, m, arr))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    4,
                    6,
                    arrayOf(
                        intArrayOf(1, 0, 1, 1, 1, 1),
                        intArrayOf(1, 0, 1, 0, 1, 0),
                        intArrayOf(1, 0, 1, 0, 1, 1),
                        intArrayOf(1, 1, 1, 0, 1, 1)
                    ),
                    15
                ),
                Arguments.of(
                    4,
                    6,
                    arrayOf(
                        intArrayOf(1, 1, 0, 1, 1, 1),
                        intArrayOf(1, 1, 0, 1, 1, 1),
                        intArrayOf(1, 1, 1, 1, 1, 1),
                        intArrayOf(1, 1, 1, 1, 0, 1)
                    ),
                    9
                ),
                Arguments.of(
                    2,
                    25,
                    arrayOf(
                        intArrayOf(
                            1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
                            1
                        ),
                        intArrayOf(
                            1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0,
                            1
                        )
                    ),
                    38
                ),
                Arguments.of(
                    7,
                    7,
                    arrayOf(
                        intArrayOf(1, 1, 1, 1, 1, 1, 1),
                        intArrayOf(1, 0, 0, 0, 0, 0, 1),
                        intArrayOf(1, 0, 1, 1, 1, 0, 1),
                        intArrayOf(1, 0, 1, 0, 1, 0, 1),
                        intArrayOf(1, 0, 1, 0, 1, 0, 1),
                        intArrayOf(1, 0, 1, 0, 1, 0, 1),
                        intArrayOf(1, 1, 1, 1, 1, 1, 1)
                    ),
                    13
                ),
                Arguments.of(
                    4,
                    4,
                    arrayOf(
                        intArrayOf(1, 1, 1, 1),
                        intArrayOf(1, 0, 0, 1),
                        intArrayOf(1, 0, 0, 1),
                        intArrayOf(1, 1, 1, 1)
                    ),
                    7
                )
            )
        }
    }


}
