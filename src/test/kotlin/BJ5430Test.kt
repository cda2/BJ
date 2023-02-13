import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ5430Test {
    val solution = BJ5430::solution

    @ParameterizedTest
    @MethodSource("testCases")
    fun `백준 5430 테스트`(command: String, array: List<Int>, result: Any) {
        assertThat(solution(command, array)).isEqualTo(result)
    }

    companion object {
        @JvmStatic
        fun testCases(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    "RDD", listOf(1, 2, 3, 4), listOf(2, 1)
                ),
                Arguments.of(
                    "DD", listOf(42), "error"
                ),
                Arguments.of(
                    "RRD", listOf(1, 1, 2, 3, 5, 8), listOf(1, 2, 3, 5, 8)
                ),
                Arguments.of(
                    "D", List(0) { 0 }, "error"
                ),
                Arguments.of(
                    "DRD", listOf(1), "error"
                ),
                Arguments.of(
                    "RDR", listOf(1, 2, 3, 4), listOf(1, 2, 3)
                ),
                Arguments.of(
                    "RR", listOf(1, 2), listOf(1, 2)
                ),
                Arguments.of(
                    "DRR", listOf(1, 2, 3), listOf(2, 3)
                )
            )
        }
    }
}
