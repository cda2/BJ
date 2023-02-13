import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ11724Test {
    val solution = BJ11724::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 11724 테스트`(nodeCount: Int, arr: List<Pair<Int, Int>>, expected: Int) {
        assertEquals(expected, solution(nodeCount, arr))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    6,
                    listOf(
                        1 to 2,
                        2 to 5,
                        5 to 1,
                        3 to 4,
                        4 to 6
                    ),
                    2
                ),
                Arguments.of(
                    6,
                    listOf(
                        1 to 2,
                        2 to 5,
                        5 to 1,
                        3 to 4,
                        4 to 6,
                        5 to 4,
                        2 to 4,
                        2 to 3,
                    ),
                    1
                ),
                Arguments.of(
                    6,
                    listOf<Pair<Int, Int>>(),
                    6
                ),
            )
        }
    }
}
