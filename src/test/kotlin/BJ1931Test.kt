import java.util.stream.Stream
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.api.*
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.params.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import BJ1931.Meeting

class BJ1931Test {
    val solution = BJ1931::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 1931 테스트`(arr: List<Meeting>, expected: Int) {
        assertEquals(expected, solution(arr))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    listOf(
                        Meeting(1, 4),
                        Meeting(3, 5),
                        Meeting(0, 6),
                        Meeting(5, 7),
                        Meeting(3, 8),
                        Meeting(5, 9),
                        Meeting(6, 10),
                        Meeting(8, 11),
                        Meeting(8, 12),
                        Meeting(2, 13),
                        Meeting(12, 14)
                    ),
                    4
                ),
                Arguments.of(
                    listOf(
                        Meeting(1, 1),
                        Meeting(1, 2),
                        Meeting(2, 2),
                        Meeting(2, 3),
                    ),
                    4
                ),
                Arguments.of(
                    listOf(
                        Meeting(1, 2),
                        Meeting(2, 3),
                        Meeting(3, 4),
                        Meeting(4, 5),
                        Meeting(5, 6),
                        Meeting(6, 7),
                        Meeting(7, 8),
                        Meeting(8, 9),
                        Meeting(9, 10),
                        Meeting(10, 11),
                        Meeting(11, 12),
                        Meeting(12, 13),
                        Meeting(13, 14),
                        Meeting(14, 15),
                        Meeting(15, 16),
                        Meeting(16, 17),
                        Meeting(17, 18),
                        Meeting(18, 19),
                        Meeting(19, 20),
                        Meeting(20, 21),
                        Meeting(21, 22),
                        Meeting(22, 23),
                        Meeting(23, 24),
                        Meeting(24, 25),
                        Meeting(25, 26),
                        Meeting(26, 27),
                        Meeting(27, 28),
                        Meeting(28, 29),
                        Meeting(29, 30),
                    ),
                    29
                ),
                Arguments.of(
                    listOf(
                        Meeting(4, 4),
                        Meeting(4, 4),
                        Meeting(1, 4),
                    ),
                    3
                ),
                Arguments.of(
                    listOf(
                        Meeting(4, 4),
                        Meeting(1, 4),
                    ),
                    2
                ),
                Arguments.of(
                    listOf(
                        Meeting(1, 1),
                        Meeting(1, 1),
                        Meeting(0, 1)
                    ),
                    3
                ),
                Arguments.of(
                    listOf(
                        Meeting(1, 6),
                        Meeting(5, 8),
                        Meeting(7, 12)
                    ),
                    2
                ),
                Arguments.of(
                    listOf(
                        Meeting(3, 3),
                        Meeting(3, 4),
                        Meeting(1, 3)
                    ),
                    3
                )
            )
        }
    }
}
