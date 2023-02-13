import java.util.stream.Stream
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.api.*
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.params.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ7662Test {
    val solution = BJ7662::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 7662 테스트`(commands: List<String>, expected: Any) {
        assertEquals(expected, solution(commands))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    arrayListOf(
                        "I 16",
                        "I -5643",
                        "D -1",
                        "D 1",
                        "D 1",
                        "I 123",
                        "D -1",
                    ),
                    "EMPTY"
                ),
                Arguments.of(
                    arrayListOf(
                        "I -45",
                        "I 653",
                        "D 1",
                        "I -642",
                        "I 45",
                        "I 97",
                        "D 1",
                        "D -1",
                        "I 333",
                    ),
                    "333 -45"
                ),
                Arguments.of(
                    arrayListOf(
                        "I 36", "I 37", "I 38", "D 1", "D 1", "I 39", "I 40", "D -1", "D -1"
                    ),
                    "40 40"
                ),
                Arguments.of(
                    arrayListOf(
                        "I 5", "D -1", "I 4",
                    ),
                    "4 4"
                ),
                Arguments.of(
                    arrayListOf(
                        "I 1",
                        "I 2",
                        "I 3",
                        "D -1",
                        "D -1",
                        "I -1",
                        "I -2",
                        "I -3",
                        "D 1",
                    ),
                    "-1 -3"
                ),
                Arguments.of(
                    arrayListOf(
                        "I 100",
                        "I 100",
                        "D 1",
                    ),
                    "100 100"
                ),
                Arguments.of(
                    arrayListOf(
                        "I 5",
                        "I 3",
                        "I 7",
                        "I 6",
                        "D 1",
                        "D -1",
                        "D -1",
                    ),
                    "6 6"
                ),
                Arguments.of(
                    arrayListOf(
                        "D 1",
                        "I 1207",
                        "I 3471",
                        "I 3574",
                        "I -5575",
                        "D -1",
                        "D 1",
                        "D 1",
                        "D -1",
                    ),
                    "EMPTY"
                ),
                Arguments.of(
                    arrayListOf(
                        "D -1",
                        "D -1",
                        "I 8088",
                        "D 1",
                        "I 5585",
                        "I 9097",
                        "I -6416",
                        "D 1",
                        "D -1",
                    ),
                    "5585 5585"
                ),
                Arguments.of(
                    arrayListOf(
                        "I 9",
                        "I 7",
                        "I 9",
                        "I 6",
                        "I 7",
                        "I 7",
                        "I 9",
                        "D -1",
                        "D 1",
                        "I 8",
                        "D 1",
                        "D 1",
                    ),
                    "8 7"
                )
            )
        }
    }
}
