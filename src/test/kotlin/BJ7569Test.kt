import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ7569Test {
    val solution = BJ7569::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 7569 토마토 테스트`(tomatoes: Array<Array<IntArray>>, answer: Int) {
        assertThat(solution(tomatoes)).isEqualTo(answer)
    }


    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {

            return Stream.of(
                Arguments.of(
                    arrayOf(
                        arrayOf(
                            intArrayOf(0, -1, 0, 0, 0),
                            intArrayOf(-1, -1, 0, 1, 1),
                            intArrayOf(0, 0, 0, 1, 1),
                        )
                    ),
                    -1
                ),
                Arguments.of(
                    arrayOf(
                        arrayOf(
                            intArrayOf(0, 0, 0, 0, 0),
                            intArrayOf(0, 0, 0, 0, 0),
                            intArrayOf(0, 0, 0, 0, 0)
                        ),
                        arrayOf(
                            intArrayOf(0, 0, 0, 0, 0),
                            intArrayOf(0, 0, 1, 0, 0),
                            intArrayOf(0, 0, 0, 0, 0),
                        )
                    ),
                    4
                ),
                Arguments.of(
                    arrayOf(
                        arrayOf(
                            intArrayOf(1, 1, 1, 1),
                            intArrayOf(1, 1, 1, 1),
                            intArrayOf(1, 1, 1, 1)
                        ),
                        arrayOf(
                            intArrayOf(1, 1, 1, 1),
                            intArrayOf(1, -1, -1, -1),
                            intArrayOf(1, 1, 1, -1)
                        ),
                    ),
                    0
                ),
            )
        }
    }


}
