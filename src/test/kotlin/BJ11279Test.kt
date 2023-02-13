import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ11279Test {
    val solution = BJ11279::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 11279 테스트`(arr: List<Long>, expected: List<Long>) {
        assertEquals(expected, solution(arr))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    arrayListOf<Long>(0, 1, 2, 0, 0, 3, 2, 1, 0, 0, 0, 0, 0),
                    arrayListOf<Long>(0, 2, 1, 3, 2, 1, 0, 0)
                )
            )
        }
    }
}
