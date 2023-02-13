import java.util.stream.Stream
import org.junit.jupiter.api.*
import org.junit.jupiter.params.*

import org.junit.jupiter.api.Assertions.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class BJ1620Test {
    val solution = BJ1620::solution

    @ParameterizedTest
    @MethodSource("testData")
    fun `백준 1620 테스트`(pokemons: List<String>, questions: List<String>, expected: List<String>) {
        assertThat(solution(pokemons, questions)).isEqualTo(expected)
    }

    companion object {
        @JvmStatic
        fun testData(): Stream<Arguments> {
            return Stream.of(
                Arguments.of(
                    arrayListOf(
                        "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
                        "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
                        "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata",
                        "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu"
                    ), arrayListOf(
                        "25", "Raichu", "3", "Pidgey", "Kakuna"
                    ), arrayListOf(
                        "Pikachu", "26", "Venusaur", "16", "14"
                    )
                )
            )
        }
    }
}
