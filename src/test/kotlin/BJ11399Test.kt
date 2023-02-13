import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ11399Test {
    val solution = BJ11399::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 11399 테스트`(arr: List<Int>, expected: Int) {
        assertThat(solution(arr)).isEqualTo(expected)
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    listOf(3, 1, 4, 3, 2),
                    32
                ),
            )
        }
    }
}
