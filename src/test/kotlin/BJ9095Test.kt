import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ9095Test {
    val solution = BJ9095::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 9095 테스트`(n: Int, expected: Int) {
        assertEquals(expected, solution(n))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(4, 7),
                Arguments.of(7, 44),
                Arguments.of(10, 274),
            )
        }
    }
}
