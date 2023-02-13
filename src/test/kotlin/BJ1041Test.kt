import BJ1041.solution
import java.util.stream.Stream
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ1041Test {

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 1041 테스트`(n: Long, dice: List<Int>, expected: Long) {
        assertEquals(expected, solution(n, dice))
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(2L, listOf(1, 2, 3, 4, 5, 6), 36),
                Arguments.of(3L, listOf(1, 2, 3, 4, 5, 6), 69),
                Arguments.of(1000000L, listOf(50, 50, 50, 50, 50, 50), 250000000000000),
                Arguments.of(10L, listOf(1, 1, 1, 1, 50, 1), 500))
        }
    }
}
