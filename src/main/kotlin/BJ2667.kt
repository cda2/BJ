object BJ2667 {
    fun solution(n: Int, map: Array<IntArray>): List<Int> {
        data class Pos(val y: Int, val x: Int) {
            private fun around(): List<Pos> {
                return listOf(
                    Pos(y - 1, x),
                    Pos(y + 1, x),
                    Pos(y, x - 1),
                    Pos(y, x + 1),
                )
            }

            fun getAround(): List<Pos> {
                return around().filter { it.isValid() && !it.isVisited() }
            }

            fun isValid(): Boolean {
                return y in 0 until n && x in 0 until n && map[y][x] != 0
            }

            fun isVisited(): Boolean {
                return map[y][x] == 0
            }

            fun visit() {
                map[y][x] = 0
            }
        }

        var group: Int = 0
        val countMap = mutableMapOf<Int, Int>()
        for (yPos in 0 until n) {
            for (xPos in 0 until n) {
                val startPos = Pos(yPos, xPos)
                if (!startPos.isValid() || startPos.isVisited()) {
                    continue
                }
                group++
                val nextPosSet = mutableSetOf<Pos>()
                nextPosSet.add(startPos)
                startPos.visit()
                var count = 0
                while (nextPosSet.isNotEmpty()) {
                    val cur = nextPosSet.first()
                    nextPosSet.remove(cur)
                    cur.visit()
                    count++
                    nextPosSet.addAll(cur.getAround())
                }
                countMap[group] = count
            }
        }

        return (1..group).map { countMap[it]!! }
    }

    fun solve() {
        val bufferedReader = System.`in`.bufferedReader()
        val n = bufferedReader
                .readLine()
                .toInt()
        val map = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            val line = bufferedReader
                    .readLine()
                    .trim()
            for (j in 0 until n) {
                map[i][j] = line[j] - '0'
            }
        }
        val answer = solution(n, map).sorted()
        println(answer.size)
        answer.forEach { println(it) }
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
