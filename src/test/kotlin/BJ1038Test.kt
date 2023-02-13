import BJ1038.solution
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.params.*
import org.junit.jupiter.params.provider.CsvSource

class BJ1038Test {

    @ParameterizedTest
    @CsvSource(value = arrayOf("18,42", "0,0", "500000,-1"))
    fun `백준 1038 테스트`(input: Int, expected: Long) {
        assertEquals(expected, solution(input))
    }
}
