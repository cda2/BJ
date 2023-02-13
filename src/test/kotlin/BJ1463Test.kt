import org.assertj.core.api.Assertions.*
import org.junit.jupiter.api.*
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.params.*
import org.junit.jupiter.params.provider.CsvSource

class BJ1463Test {
    private val solution = BJ1463::solution

    @ParameterizedTest
    @CsvSource("2, 1", "10, 3", "4, 2", "3, 1", "1, 0", "1000000, 19", delimiter = ',')
    fun `백준 1463 테스트`(n: Int, expected: Int) {
        assertEquals(expected, solution(n))
    }
}
