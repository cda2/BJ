import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ1927Test {
    val solution = BJ1927::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 1927 테스트`(arr: List<Long>, expected: List<Long>) {
        assertEquals(expected, solution(arr))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    arrayListOf<Long>(0, 12345678, 1, 2, 0, 0, 0, 0, 32),
                    arrayListOf<Long>(0, 1, 2, 12345678, 0)
                )
            )
        }
    }
}
