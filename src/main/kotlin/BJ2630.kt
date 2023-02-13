object BJ2630 {
    data class Pos(val y: Int, val x: Int)
    data class Area(val start: Pos, val end: Pos) {
        fun divide(): List<Area> {
            val midY = (start.y + end.y) / 2
            val midX = (start.x + end.x) / 2
            return listOf(
                Area(start, Pos(midY, midX)),
                Area(Pos(start.y, midX + 1), Pos(midY, end.x)),
                Area(Pos(midY + 1, start.x), Pos(end.y, midX)),
                Area(Pos(midY + 1, midX + 1), end)
            )
        }
    }

    class Board(val map: Array<IntArray>) {
        private fun isAllSame(area: Area): Boolean {
            val first = map[area.start.y][area.start.x]
            for (y in area.start.y..area.end.y) {
                for (x in area.start.x..area.end.x) {
                    if (map[y][x] != first) {
                        return false
                    }
                }
            }
            return true
        }

        fun getCount(
            area: Area = Area(
                Pos(0, 0), Pos(map.size - 1, map.size - 1)
            ),
        ): Pair<Int, Int> {
            if (isAllSame(area)) {
                return if (map[area.start.y][area.start.x] == 0) {
                    Pair(1, 0)
                } else {
                    Pair(0, 1)
                }
            }

            var whiteCount = 0
            var blueCount = 0
            for (subArea in area.divide()) {
                val (white, blue) = getCount(subArea)
                whiteCount += white
                blueCount += blue
            }
            return Pair(whiteCount, blueCount)
        }
    }

    fun solution(board: Array<IntArray>): Pair<Int, Int> {
        return Board(board).getCount()
    }

    fun solve() {
        val n = readln().toInt()
        val board = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            val line = readln()
                    .split(" ")
                    .map { it.toInt() }
            for (j in 0 until n) {
                board[i][j] = line[j]
            }
        }
        val (white, blue) = solution(board)
        println(white)
        println(blue)
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
