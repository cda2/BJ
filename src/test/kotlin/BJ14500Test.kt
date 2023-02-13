import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ14500Test {
    val solution = BJ14500::solution

    @ParameterizedTest
    @MethodSource("testCases")
    fun `백준 14500 테스트`(paper: List<List<Int>>, answer: Int) {
        assertThat(solution(paper)).isEqualTo(answer)
    }

    companion object {
        @JvmStatic
        fun testCases(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    listOf(
                        listOf(1, 2, 3, 4, 5),
                        listOf(5, 4, 3, 2, 1),
                        listOf(2, 3, 4, 5, 6),
                        listOf(6, 5, 4, 3, 2),
                        listOf(1, 2, 1, 2, 1),
                    ),
                    19
                ),
                Arguments.of(
                    listOf(
                        listOf(1, 2, 3, 4, 5),
                        listOf(1, 2, 3, 4, 5),
                        listOf(1, 2, 3, 4, 5),
                        listOf(1, 2, 3, 4, 5),
                    ),
                    20
                ),
                Arguments.of(
                    listOf(
                        listOf(1, 2, 1, 2, 1, 2, 1, 2, 1, 2),
                        listOf(2, 1, 2, 1, 2, 1, 2, 1, 2, 1),
                        listOf(1, 2, 1, 2, 1, 2, 1, 2, 1, 2),
                        listOf(2, 1, 2, 1, 2, 1, 2, 1, 2, 1),
                    ),
                    7
                ),
            )
        }
    }
}
