import kotlin.math.sqrt

object BJ1025 {
    class Pos(val row: Int, val col: Int, val table: List<List<Int>>) {
        fun isValid(): Boolean {
            return row in table.indices && col in table[0].indices
        }

        fun getVal(): Int {
            return table[row][col]
        }

        fun nextPos(rowGap: Int, colGap: Int): Pos {
            return Pos(row + rowGap, col + colGap, table)
        }

        override fun toString(): String {
            return "Pos(row=$row, col=$col, val=${getVal()}"
        }

        override fun equals(other: Any?): Boolean {
            return other is Pos && other.row == row && other.col == col
        }

        override fun hashCode(): Int {
            var result = row
            result = 31 * result + col
            return result
        }
    }

    fun solution(table: List<List<Int>>): Int {
        val n = table.size
        val m = table[0].size
        var max = -1

        val calculatedSet = hashSetOf<Int>()

        for (i in 0 until n) {
            for (j in 0 until m) {

                Pos(i, j, table).getVal().run {
                    if (!calculatedSet.contains(this)) {
                        max = maxVal(this, max)
                        calculatedSet.add(this)
                    }
                }

                for (rowGap in -i until n - i) {
                    for (colGap in -j until m - j) {
                        if (rowGap == 0 && colGap == 0) continue

                        var curPos = Pos(i, j, table)
                        var nextPos = Pos(i, j, table)
                        val arr = mutableListOf(curPos.getVal())

                        while (nextPos.isValid()) {
                            nextPos = curPos.nextPos(rowGap, colGap)
                            if (!nextPos.isValid()) break
                            arr.add(nextPos.getVal())
                            curPos = nextPos

                            val concat = concatNumber(arr)
                            if (calculatedSet.contains(concat)) continue
                            calculatedSet.add(concat)

                            // check remain is 0
                            max = maxVal(concat, max)
                        }
                    }
                }
            }
        }

        return max
    }

    private fun concatNumber(arr: MutableList<Int>) = arr.joinToString("").toInt()

    private fun maxVal(concatNum: Int, max: Int): Int {
        var answer = max
        val concatSqrt = sqrt(concatNum.toDouble())
        if ((concatSqrt - concatSqrt.toInt()) == 0.0) {
            answer = maxOf(answer, concatNum)
        }
        return answer
    }

    private fun solve() {
        val (n, _) = readln().split(" ").map { it.toInt() }
        val table = mutableListOf<List<Int>>()
        repeat(n) { table.add(readln().trim().run { this.toCharArray().map { it.digitToInt() } }) }
        println(solution(table))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
