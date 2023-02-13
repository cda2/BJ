import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.CsvSource

class BJ1697Test {
    val solution = BJ1697::solution

    @ParameterizedTest
    @CsvSource("5,17,4")
    fun `백준 1697 테스트`(n: Int, k: Int, expected: Int) {
        assertEquals(expected, solution(n, k))
    }
}
