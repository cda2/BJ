import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ1083Test {
    val solution = BJ1083::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 1083 테스트`(arr: MutableList<Int>, s: Int, expected: List<Int>) {
        assertThat(solution(arr, s)).isEqualTo(expected)
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    arrayListOf(10, 20, 30, 40, 50, 60, 70),
                    1,
                    arrayListOf(20, 10, 30, 40, 50, 60, 70)
                ),
                Arguments.of(
                    arrayListOf(3, 5, 1, 2, 4),
                    2,
                    arrayListOf(5, 3, 2, 1, 4)
                ),
                Arguments.of(
                    arrayListOf(19, 20, 17, 18, 15, 16, 13, 14, 11, 12),
                    5,
                    arrayListOf(20, 19, 18, 17, 16, 15, 14, 13, 12, 11)
                ),
                Arguments.of(
                    arrayListOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                    17,
                    arrayListOf(10, 9, 1, 2, 3, 4, 5, 6, 7, 8)
                )
            )
        }
    }
}
