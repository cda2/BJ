object BJ2178 {
    fun solution(n: Int, m: Int, board: Array<IntArray>): Int {
        data class Pos(val y: Int, val x: Int, val count: Int) {
            private fun getSimpleAround(): List<Pos> {
                return listOf(
                    Pos(y - 1, x, count + 1),
                    Pos(y + 1, x, count + 1),
                    Pos(y, x - 1, count + 1),
                    Pos(y, x + 1, count + 1),
                )
            }

            fun getAround(): List<Pos> {
                return getSimpleAround().filter { it.isValid() }
            }

            fun isValid(): Boolean {
                return y in 0 until n && x in 0 until m && board[y][x] == 1
            }

            fun isEnd(): Boolean {
                return y == n - 1 && x == m - 1
            }
        }

        val countMap: Array<IntArray> = Array(n) { IntArray(m) { 100000 } }
        val queue = ArrayDeque<Pos>()
        queue.add(Pos(0, 0, 1))
        countMap[0][0] = 1

        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            if (cur.isEnd()) {
                return cur.count
            }

            for (next in cur.getAround()) {
                if (next.count < countMap[next.y][next.x]) {
                    queue.add(next)
                    countMap[next.y][next.x] = next.count
                }
            }
        }

        // unreachable
        return -1
    }

    fun solve() {
        val bufferedReader = System.`in`.bufferedReader()
        val (n, m) = bufferedReader
                .readLine()
                .split(" ")
                .map { it.toInt() }
        val board = Array(n) { IntArray(m) }
        for (i in 0 until n) {
            val line = bufferedReader
                    .readLine()
                    .trim()
            for (j in 0 until m) {
                board[i][j] = line[j] - '0'
            }
        }
        println(solution(n, m, board))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
