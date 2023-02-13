import java.util.stream.Stream
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.api.*
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.params.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ18870Test {
    val solution = BJ18870::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 18870 테스트`(arr: List<Int>, expected: List<Int>) {
        assertEquals(expected, solution(arr))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    listOf(2, 4, -10, 4, -9),
                    listOf(2, 3, 0, 3, 1)
                ),
                Arguments.of(
                    listOf(1000, 999, 1000, 999, 1000, 999),
                    listOf(1, 0, 1, 0, 1, 0)
                ),
            )
        }
    }
}
