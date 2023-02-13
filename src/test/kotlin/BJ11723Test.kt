import java.util.stream.Stream
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.api.*
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.params.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ11723Test {
    val solution = BJ11723

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 11723 테스트`(input: List<String>, expected: List<Int>) {
        val commandExecutor = BJ11723.CommandExecutor()
        assertEquals(expected, input
                .map { commandExecutor.execute(it) }
                .filterIsInstance<Int>())
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    listOf(
                        "add 1",
                        "add 2",
                        "check 1",
                        "check 2",
                        "check 3",
                        "remove 2",
                        "check 1",
                        "check 2",
                        "toggle 3",
                        "check 1",
                        "check 2",
                        "check 3",
                        "check 4",
                        "all",
                        "check 10",
                        "check 20",
                        "toggle 10",
                        "remove 20",
                        "check 10",
                        "check 20",
                        "empty",
                        "check 1",
                        "toggle 1",
                        "check 1",
                        "toggle 1",
                        "check 1",
                    ),
                    listOf(
                        1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0
                    )
                )
            )
        }
    }
}
