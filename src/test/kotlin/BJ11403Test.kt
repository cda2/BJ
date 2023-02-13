import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ11403Test {
    val solution = BJ11403::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 11403 테스트`(arr: List<List<Int>>, expected: List<List<Int>>) {
        assertEquals(expected, solution(arr))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    listOf(
                        listOf(0, 1, 0),
                        listOf(0, 0, 1),
                        listOf(1, 0, 0)
                    ),
                    listOf(
                        listOf(1, 1, 1),
                        listOf(1, 1, 1),
                        listOf(1, 1, 1)
                    )
                ),
                Arguments.of(
                    listOf(
                        listOf(0, 0, 0),
                        listOf(0, 0, 0),
                        listOf(0, 0, 0)
                    ),
                    listOf(
                        listOf(0, 0, 0),
                        listOf(0, 0, 0),
                        listOf(0, 0, 0)
                    )
                ),
                Arguments.of(
                    listOf(
                        listOf(0, 0, 0, 1, 0, 0, 0),
                        listOf(0, 0, 0, 0, 0, 0, 1),
                        listOf(0, 0, 0, 0, 0, 0, 0),
                        listOf(0, 0, 0, 0, 1, 1, 0),
                        listOf(1, 0, 0, 0, 0, 0, 0),
                        listOf(0, 0, 0, 0, 0, 0, 1),
                        listOf(0, 0, 1, 0, 0, 0, 0)
                    ),
                    listOf(
                        listOf(1, 0, 1, 1, 1, 1, 1),
                        listOf(0, 0, 1, 0, 0, 0, 1),
                        listOf(0, 0, 0, 0, 0, 0, 0),
                        listOf(1, 0, 1, 1, 1, 1, 1),
                        listOf(1, 0, 1, 1, 1, 1, 1),
                        listOf(0, 0, 1, 0, 0, 0, 1),
                        listOf(0, 0, 1, 0, 0, 0, 0)
                    ),
                )
            )
        }
    }
}
